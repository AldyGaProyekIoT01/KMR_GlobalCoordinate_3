"""Estimate global x, y, theta from body linear and angular velocity inputs."""
import math
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D, Twist

class GlobalCoordinateEstimator(Node):
    def __init__(self):
        super().__init__('global_coordinate_estimator')
        self.declare_parameter('initial_x', 0.0)
        self.declare_parameter('initial_y', 0.0)
        self.declare_parameter('initial_theta', 0.0)
        self.declare_parameter('publish_rate', 20.0)
        self.x = float(self.get_parameter('initial_x').value)
        self.y = float(self.get_parameter('initial_y').value)
        self.theta = float(self.get_parameter('initial_theta').value)
        rate = float(self.get_parameter('publish_rate').value)
        if rate <= 0.0:
            rate = 20.0
            self.get_logger().warning('publish_rate harus positif; menggunakan 20 Hz.')
        self.v_b = 0.0
        self.omega = 0.0
        self.last_update = time.monotonic()
        self.create_subscription(Twist, '/global_coordinate/input', self.input_callback, 10)
        self.pose_pub = self.create_publisher(Pose2D, '/global_coordinate/pose', 10)
        self.velocity_pub = self.create_publisher(Twist, '/global_coordinate/velocity', 10)
        self.create_timer(1.0 / rate, self.update_pose)
        self.get_logger().info('Global Coordinate Estimator siap.')
        self.get_logger().info('Input: /global_coordinate/input (linear.x=V_b, angular.z=omega)')
        self.get_logger().info('Output: /global_coordinate/pose dan /global_coordinate/velocity')

    def input_callback(self, msg):
        self.v_b = float(msg.linear.x)
        self.omega = float(msg.angular.z)

    def update_pose(self):
        now = time.monotonic()
        dt = max(0.0, min(now - self.last_update, 0.25))
        self.last_update = now
        # Integrasi Euler sesuai persamaan Global Coordinate pada materi.
        self.x += self.v_b * math.cos(self.theta) * dt
        self.y += self.v_b * math.sin(self.theta) * dt
        self.theta += self.omega * dt
        self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))
        pose = Pose2D()
        pose.x, pose.y, pose.theta = self.x, self.y, self.theta
        self.pose_pub.publish(pose)
        vel = Twist()
        vel.linear.x = self.v_b * math.cos(self.theta)
        vel.linear.y = self.v_b * math.sin(self.theta)
        vel.angular.z = self.omega
        self.velocity_pub.publish(vel)

def main(args=None):
    rclpy.init(args=args)
    node = GlobalCoordinateEstimator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
