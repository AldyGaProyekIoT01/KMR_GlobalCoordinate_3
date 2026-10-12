import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class OdomToGlobal(Node):
    def __init__(self):
        super().__init__('odom_to_global')
        self.pub = self.create_publisher(
            Twist, '/global_coordinate/input', 10)
        self.sub = self.create_subscription(
            Odometry, '/odom', self.callback, 10)

    def callback(self, msg):
        twist = Twist()
        twist.linear.x = msg.twist.twist.linear.x
        twist.angular.z = msg.twist.twist.angular.z
        self.pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = OdomToGlobal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
