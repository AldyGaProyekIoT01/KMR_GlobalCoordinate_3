# Global Coordinate Estimator (ROS 2 Jazzy)

Paket mandiri untuk mengestimasi koordinat global robot dari nilai input body velocity. Nama paket dan file tidak menggunakan nama package proyek sebelumnya.

## Persamaan
- x_dot = V_b cos(theta)
- y_dot = V_b sin(theta)
- theta_dot = omega
- Integrasi numerik memakai interval waktu aktual.

## Instalasi
Ekstrak folder `global_coordinate_estimator` ke `~/ros2_ws/src/`, sehingga file `package.xml` berada di `~/ros2_ws/src/global_coordinate_estimator/package.xml`.

```bash
cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build --packages-select global_coordinate_estimator
source install/setup.bash
ros2 run global_coordinate_estimator global_coordinate_estimation
```

## Input
Topic `/global_coordinate/input`, tipe `geometry_msgs/msg/Twist`:
- `linear.x` = V_b dalam m/s
- `angular.z` = omega dalam rad/s

Gerak lurus:
```bash
ros2 topic pub --rate 10 /global_coordinate/input geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"
```

Rotasi di tempat (hentikan publisher sebelumnya dengan Ctrl+C):
```bash
ros2 topic pub --rate 10 /global_coordinate/input geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.5}}"
```

## Output
```bash
ros2 topic echo /global_coordinate/pose
ros2 topic echo /global_coordinate/velocity
```
- `/global_coordinate/pose`: `geometry_msgs/msg/Pose2D` dengan x, y (meter), theta (radian).
- `/global_coordinate/velocity`: `geometry_msgs/msg/Twist` dengan kecepatan global pada linear.x/linear.y dan omega pada angular.z.

Posisi awal default x=0, y=0, theta=0. Parameter dapat diubah melalui `-p initial_x:=... -p initial_y:=... -p initial_theta:=... -p publish_rate:=20.0`.

Catatan: node ini memperkirakan posisi dari input kecepatan (open-loop); tidak menggerakkan robot Gazebo dan tidak membaca odometri aktual. Pastikan input publisher aktif untuk memperbarui estimasi.
