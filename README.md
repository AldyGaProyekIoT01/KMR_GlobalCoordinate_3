# KMR_GlobalCoordinate_3
## Program Estimasi Global Coordinate

Cara menjalankan program dari awal

Persiapan
Buka terminal Ubuntu, lalu jalankan:

### Terminal 1

cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch robin_bringup my_robot_gazebo.launch.py

**Tunggu sampai Gazebo terbuka dan robot robin muncul. Biarkan terminal ini tetap berjalan.**


### Terminal 2
Buka terminal baru, kemudian jalankan:

source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run global_coordinate_estimator global_coordinate_estimation

**Biarkan terminal ini tetap berjalan.**


### Terminal 3
Buka terminal baru, kemudian jalankan:

source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run global_coordinate_estimator odom_to_global

**Biarkan terminal ini tetap berjalan.**


### Terminal 4
Buka terminal baru, kemudian jalankan:

source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 topic echo /global_coordinate/pose

**Koordinat x, y, dan theta akan ditampilkan.**


### Terminal 5
Buka terminal baru, kemudian jalankan:

source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 topic echo /global_coordinate/pose

**menghitung kecepatan global menggunakan nilai θ yang sudah diperbarui pada setiap siklus.**


### Terminal 6

Di terminal baru, jalankan perintah untuk 

**bergerak maju:**

ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.2}, angular: {z: 0.0}}"

**Berbelok:**

ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 0.0}, angular: {z: 0.5}}"
