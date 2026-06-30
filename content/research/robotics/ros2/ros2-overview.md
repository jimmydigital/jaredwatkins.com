---
title: "ROS 2 (Robot Operating System 2)"
date: 2026-06-26
lastmod: 2026-06-26
draft: false
description: "Open-source middleware framework for robot software development; the de facto standard for professional and research robotics; publish-subscribe communications, hardware abstraction, sensor drivers, and tooling built on DDS transport."
research_area: "robotics/ros2"
source_urls:
  - "https://docs.ros.org/en/rolling/index.html"
  - "https://design.ros2.org/"
  - "https://github.com/ros2/ros2"
  - "https://www.ros.org/about-ros/"
last_reviewed: 2026-06-26
stale_after_days: 180
related:
  - "robotics/ros2/picknik-robotics.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

ROS 2 (Robot Operating System 2) is an open-source middleware framework and tool ecosystem for robot software development. Despite the name, it is not an operating system — it is a communications layer, hardware abstraction framework, and development toolchain that runs on top of Linux, Windows, or macOS. ROS 2 provides the plumbing that lets individual software components (sensors, motion planners, perception systems, actuators) communicate with each other without custom integration work for each pairing. It is the de facto standard for professional and research robotics worldwide, with adoption spanning industrial arms, autonomous mobile robots, surgical systems, aerospace platforms, and agricultural machines.

## Key Facts

- **Initial release (ROS 1):** 2007 at Willow Garage; open-sourced 2010
- **ROS 2 first stable release:** Ardent Apalone, December 2017
- **Current LTS:** Jazzy Jalisco (released May 2024; Ubuntu 24.04 Noble); Humble Hawksbill (released May 2022; still in LTS support)
- **ROS 1 EOL:** May 2025 — Noetic Ninjemys was the final ROS 1 distribution
- **Maintainer:** Open Source Robotics Foundation (OSRF), now operating as the Open Source Robotics Alliance (OSRA)
- **License:** Apache 2.0 (core); individual packages may vary
- **Primary languages:** C++ (rclcpp) and Python (rclpy); also Rust (unofficial), Java (partial)
- **Transport:** Data Distribution Service (DDS) — default implementations: Fast DDS (eProsima), Cyclone DDS (Eclipse), Connext DDS (RTI, commercial)
- **Key differentiation from ROS 1:** Real-time capability, security (DDS-SECURITY), multi-robot support, no single master process, Windows support, Python 3

## What It Is / How It Works

### The Core Abstraction: Nodes, Topics, Services, and Actions

ROS 2 is built around four communication primitives that form the protocol-level vocabulary of every ROS 2 system:

**Nodes** are the fundamental unit of computation — a single-purpose process that does one thing (reads a camera, runs a motion planner, controls a motor). A robot system is a graph of nodes. Each node runs as a separate OS process (or in a composed executor, as a shared-library component within a single process). The design principle is that nodes should be small, single-purpose, and replaceable.

**Topics** are anonymous publish-subscribe channels for streaming data. A node publishes sensor data to a topic; zero or more subscriber nodes consume it. Topics are typed — the message type is defined in a `.msg` file and code is generated for C++ and Python. There is no point-to-point addressing: the publisher and subscriber never directly reference each other, only the topic name and message type. This decoupling is the foundation of ROS 2's composability.

**Services** are synchronous request-reply RPCs between nodes. A client node sends a typed request; a server node returns a typed response. Services are appropriate for discrete, latency-sensitive operations (query a robot's current joint angles, trigger a calibration routine). They are defined in `.srv` files.

**Actions** are the asynchronous, long-running version of services. An action client sends a goal; the action server executes it, streaming feedback at configurable intervals, and eventually returns a result. Actions support preemption — the client can cancel a goal mid-execution. This makes them appropriate for motion goals (move the arm to this pose, drive to this location) where progress feedback and cancellation semantics matter. Defined in `.action` files.

### The DDS Transport Layer

ROS 2 replaced ROS 1's custom TCPROS/UDPROS transport with the Data Distribution Service (DDS) standard, a publish-subscribe middleware standard maintained by the Object Management Group (OMG). DDS provides:

- **Automatic peer discovery** — nodes find each other on the local network without a central broker or name server (contrast with ROS 1's `rosmaster`)
- **QoS (Quality of Service) policies** — configurable durability, reliability, deadline, liveliness, and history settings per publisher/subscriber pair
- **Security** — DDS-SECURITY provides authentication, access control, and encryption at the transport layer
- **Real-time guarantees** — DDS implementations are available for RTOS environments with deterministic scheduling

The `rmw` (ROS Middleware) abstraction layer allows the DDS implementation to be swapped at runtime without recompiling application code. Common implementations: Fast DDS (eProsima, default), Cyclone DDS (Eclipse/ADLINK), Connext DDS (RTI, commercial, used in safety-certified contexts).

### QoS Profiles — Protocol-Level Detail

QoS policies are set per publisher and per subscription. Incompatible QoS pairings silently result in no communication — a common source of debugging confusion for new users.

Key QoS settings:

| Policy | Options | Use Case |
|--------|---------|----------|
| **Reliability** | `RELIABLE` / `BEST_EFFORT` | Sensor streams often BEST_EFFORT for low latency; command channels RELIABLE |
| **Durability** | `VOLATILE` / `TRANSIENT_LOCAL` | TRANSIENT_LOCAL stores the last N messages for late-joining subscribers (useful for configuration topics) |
| **History** | `KEEP_LAST(N)` / `KEEP_ALL` | Controls queue depth |
| **Deadline** | Duration | Triggers a callback if no message received within the window |
| **Liveliness** | `AUTOMATIC` / `MANUAL_BY_TOPIC` | Detects dead publishers |

**Example — configuring a sensor publisher in C++:**

```cpp
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"

class LidarPublisher : public rclcpp::Node {
public:
  LidarPublisher() : Node("lidar_publisher") {
    // Best-effort QoS for sensor data: prioritize low latency over guaranteed delivery
    auto qos = rclcpp::QoS(rclcpp::KeepLast(10));
    qos.best_effort();
    qos.durability_volatile();

    publisher_ = this->create_publisher<sensor_msgs::msg::LaserScan>(
      "scan", qos);

    timer_ = this->create_wall_timer(
      std::chrono::milliseconds(50),  // 20 Hz
      std::bind(&LidarPublisher::publish_scan, this));
  }

private:
  void publish_scan() {
    auto msg = sensor_msgs::msg::LaserScan();
    msg.header.stamp = this->now();
    msg.header.frame_id = "laser_link";
    // ... populate scan data ...
    publisher_->publish(msg);
  }

  rclcpp::Publisher<sensor_msgs::msg::LaserScan>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};
```

**Example — subscribing with matched QoS in Python:**

```python
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from sensor_msgs.msg import LaserScan

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            depth=10
        )
        self.subscription = self.create_subscription(
            LaserScan, 'scan', self.scan_callback, qos)

    def scan_callback(self, msg):
        self.get_logger().info(
            f'Got scan: {len(msg.ranges)} points, '
            f'angle_min={msg.angle_min:.2f} rad')
```

### The Parameter System

ROS 2 has a first-class parameter system — nodes declare parameters with types and default values; they can be set at launch time, updated at runtime via services, and monitored for changes.

```python
class MyController(Node):
    def __init__(self):
        super().__init__('my_controller')
        # Declare with type and default
        self.declare_parameter('max_velocity', 0.5)
        self.declare_parameter('control_frequency', 50.0)

        # Register a callback for runtime changes
        self.add_on_set_parameters_callback(self.parameter_callback)

    def parameter_callback(self, params):
        for p in params:
            if p.name == 'max_velocity':
                self.get_logger().info(f'max_velocity updated to {p.value}')
        return rcl_interfaces.msg.SetParametersResult(successful=True)
```

Parameters can be set from the CLI:

```bash
ros2 param set /my_controller max_velocity 0.3
ros2 param get /my_controller max_velocity
ros2 param dump /my_controller  # dump all params to YAML
```

### Launch System

ROS 2's launch system allows entire robot configurations — multiple nodes, parameters, remappings — to be described in Python (or XML/YAML). Launch files are code, not static config.

```python
# launch/robot_bringup.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),

        Node(
            package='robot_base',
            executable='base_controller',
            name='base_controller',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'wheel_radius': 0.0762,
                'wheel_separation': 0.381,
            }],
        ),

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            name='lidar',
            remappings=[('/scan', '/front_scan')],  # remap topic names
            parameters=[{'serial_port': '/dev/ttyUSB0'}],
        ),

        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            parameters=[{'yaml_filename': '/maps/office.yaml'}],
        ),
    ])
```

### TF2 — The Transform System

`tf2` is the coordinate frame transform library central to all multi-link robot systems. Every physical entity in a robot system (base, joints, sensors, camera frames, end effectors) has a named coordinate frame. `tf2` maintains a time-buffered tree of transforms between frames, allowing any node to ask: "what is the position of the wrist frame relative to the world frame at time T?"

```python
import tf2_ros
from geometry_msgs.msg import TransformStamped

# Broadcaster: publish a transform (typically from URDF + joint states)
br = tf2_ros.TransformBroadcaster(self)
t = TransformStamped()
t.header.stamp = self.get_clock().now().to_msg()
t.header.frame_id = 'base_link'
t.child_frame_id = 'camera_link'
t.transform.translation.x = 0.1
t.transform.rotation.w = 1.0
br.sendTransform(t)

# Listener: look up a transform
tf_buffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tf_buffer, self)
try:
    transform = tf_buffer.lookup_transform(
        'world', 'gripper_tip', rclpy.time.Time())
except tf2_ros.LookupException:
    pass
```

## Where ROS 2 Sits in the Robot Control Stack

A complete robot system has five rough layers. ROS 2 spans the middle three:

```
┌─────────────────────────────────────────────────────┐
│  Mission / Task Planning (behavior trees, FSMs)     │  ← Application Layer
├─────────────────────────────────────────────────────┤
│  Autonomy: Navigation, Manipulation, Perception     │  ← ROS 2 packages
├─────────────────────────────────────────────────────┤
│  ROS 2 Middleware: Topics, Services, Actions, TF2  │  ← Core ROS 2
├─────────────────────────────────────────────────────┤
│  Hardware Abstraction: ros2_control, drivers        │  ← ROS 2 packages
├─────────────────────────────────────────────────────┤
│  Hardware: MCUs, motor drivers, sensors, actuators  │  ← Bare metal / RTOS
└─────────────────────────────────────────────────────┘
```

**Above ROS 2:** Mission execution frameworks (BehaviorTree.CPP, SMACH), fleet management systems (ROS 2 Fleet Manager, VDA 5050 bridges), and operator interfaces.

**Within ROS 2:** The major packages that ship with or integrate tightly with ROS 2 include Nav2 (navigation stack — path planning, costmaps, behavior trees for mobile robots), MoveIt 2 (manipulation planning for arms and end effectors), ros2_control (hardware interface abstraction for joints and actuators), micro-ROS (ROS 2 on MCUs — discussed below), and a large ecosystem of sensor drivers.

**Below ROS 2:** `ros2_control` hardware interfaces communicate via shared memory or serial protocols (EtherCAT, CANopen, Modbus, UART) with real-time controllers — often a separate MCU or FPGA running at kilohertz rates. ROS 2 itself runs on Linux with soft real-time characteristics; hard real-time control loops live below the ROS 2 layer.

### ros2_control — The Hardware Interface Protocol

`ros2_control` is the canonical abstraction for robot joints and actuators in ROS 2. It defines a standardized interface between high-level controllers (PID loops, trajectory followers, force controllers) and hardware-specific drivers. Hardware interfaces expose **state interfaces** (what the hardware reports: position, velocity, effort) and **command interfaces** (what the hardware accepts: position setpoint, velocity setpoint, effort setpoint).

A hardware plugin implements the `SystemInterface` base class:

```cpp
#include "hardware_interface/system_interface.hpp"

class MyMotorHardware : public hardware_interface::SystemInterface {
public:
  hardware_interface::CallbackReturn on_configure(
      const rclcpp_lifecycle::State & previous_state) override {
    // Open serial port, initialize motor driver
    return hardware_interface::CallbackReturn::SUCCESS;
  }

  hardware_interface::return_type read(
      const rclcpp::Time & time,
      const rclcpp::Duration & period) override {
    // Read encoder counts from hardware; write to state_interfaces_
    hw_positions_[0] = read_encoder() * 2 * M_PI / COUNTS_PER_REV;
    return hardware_interface::return_type::OK;
  }

  hardware_interface::return_type write(
      const rclcpp::Time & time,
      const rclcpp::Duration & period) override {
    // Write command_interfaces_ value to hardware
    send_position_command(hw_commands_[0]);
    return hardware_interface::return_type::OK;
  }
};
```

The controller manager loads controllers (e.g., `JointTrajectoryController`, `DiffDriveController`) and hardware plugins, then runs the `read → update → write` loop at the configured rate — typically 100–1000 Hz.

## Hardware ROS 2 Can Be Used With

ROS 2 runs on any hardware with a Linux kernel (or Windows, with limitations). The practical scope:

### Compute Platforms

| Platform | Notes |
|----------|-------|
| **x86-64 Linux** | Primary development target; Ubuntu 22.04 (Humble) and 24.04 (Jazzy) are the primary supported distributions |
| **ARM64 Linux** | Raspberry Pi 4/5, NVIDIA Jetson (Xavier, Orin), Qualcomm RB5; full support |
| **NVIDIA Jetson Orin** | Dominant onboard compute for professional robots; Isaac ROS provides GPU-accelerated ROS 2 packages (stereo depth, apriltag detection, ESS stereo, pose estimation) |
| **micro-ROS (MCUs)** | FreeRTOS, Zephyr, NuttX; stm32, ESP32, Raspberry Pi Pico; communicates with a full ROS 2 system via micro-ROS Agent over Serial, UDP, or USB |
| **Windows 10/11** | Supported but less common in production; primarily for simulation and development |
| **macOS** | Community-supported via Homebrew; not officially tier-1 |

### Robot Platforms with Vendor-Supported ROS 2 Drivers

The following represent platforms with strong, vendor-maintained ROS 2 integration:

**Mobile Robots / AMRs:**
- Clearpath Husky, Jackal, Ridgeback (Rockwell Automation) — reference platforms for outdoor robotics research
- iRobot Create 3 — designed from the ground up as a ROS 2-native educational platform; publishes odometry, IMU, battery, IR sensors as ROS 2 topics out of the box
- Turtlebot 4 (iRobot + Clearpath) — the canonical ROS 2 beginner platform
- Boston Dynamics Spot — ROS 2 wrapper available via community (spot_ros2); not vendor-maintained

**Industrial Arms:**
- Universal Robots (UR3e, UR5e, UR10e, UR16e, UR20, UR30) — ur_robot_driver, vendor-maintained; gold standard for ROS 2 arm integration
- Kinova Gen3 — vendor-maintained ROS 2 driver
- FANUC CRX/LR series — vendor-supported via FANUC/PickNik collaboration
- KUKA LBR iisy — vendor-supported ROS 2 driver
- Franka Robotics (FR3, formerly Panda) — libfranka 2.x with ROS 2 support

**Sensors:**
- Velodyne, Ouster, Hesai, Livox LiDARs — all have vendor or well-maintained community ROS 2 drivers
- Intel RealSense D400/L500 series — realsense-ros, vendor-maintained
- Stereolabs ZED 2/X — vendor-maintained; CUDA-accelerated depth + VIO pipeline
- Zivid 2/2+ structured-light cameras — vendor-maintained; Gold MoveIt integration
- Robotis Dynamixel servos — dynamixel_sdk and ros2_dynamixel_hardware

**Drones / Aerial:**
- PX4 Autopilot — px4_msgs + micro-ROS bridge; official ROS 2 integration
- ArduPilot — MAVROS2 bridge; large community
- Parrot Sphinx simulator — integrates with ROS 2

### micro-ROS: ROS 2 on Microcontrollers

micro-ROS extends the ROS 2 graph to resource-constrained MCUs (Cortex-M3/M4/M7, ESP32, RP2040). The MCU runs a micro-ROS client library communicating with a micro-ROS Agent running on the main Linux computer. The agent bridges the MCU's topics/services/actions into the full ROS 2 DDS graph.

**Example — ESP32 publishing IMU data via micro-ROS:**

```c
// micro-ROS on ESP32 (FreeRTOS / Arduino framework)
#include <micro_ros_arduino.h>
#include <rcl/rcl.h>
#include <rclc/rclc.h>
#include <sensor_msgs/msg/imu.h>

rcl_publisher_t publisher;
sensor_msgs__msg__Imu imu_msg;
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;
rcl_timer_t timer;

void timer_callback(rcl_timer_t * timer, int64_t last_call_time) {
  // Read IMU hardware registers
  imu_msg.header.stamp = rcl_clock_now();
  imu_msg.linear_acceleration.x = read_accel_x();
  imu_msg.angular_velocity.z = read_gyro_z();
  rcl_publish(&publisher, &imu_msg, NULL);
}

void setup() {
  set_microros_serial_transports(Serial);  // communicate over USB serial
  allocator = rcl_get_default_allocator();
  rclc_support_init(&support, 0, NULL, &allocator);
  rclc_node_init_default(&node, "imu_node", "", &support);
  rclc_publisher_init_default(&publisher, &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(sensor_msgs, msg, Imu), "imu");
  rclc_timer_init_default(&timer, &support, RCL_MS_TO_NS(10), timer_callback);
  rclc_executor_init(&executor, &support.context, 1, &allocator);
  rclc_executor_add_timer(&executor, &timer);
}

void loop() {
  rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100));
}
```

On the host Linux machine, run the agent:

```bash
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0
```

The IMU topic then appears in the ROS 2 graph like any other node:

```bash
ros2 topic echo /imu
```

## Non-Obvious / Creative Uses for ROS 2

ROS 2's publish-subscribe model, hardware abstraction, and visualization tools are general enough that they've been applied well outside traditional robotics:

**Laboratory Automation:** Automated liquid handling robots, microscope stages, mass spectrometers, and PCR machines use ROS 2 as the integration layer. OpenTrons liquid handling robots have community ROS 2 integrations. The node/topic model maps naturally to lab instrument control (publish a command, subscribe to measurement data).

**Agricultural Autonomy:** ROS 2 is the standard platform for autonomous tractors, field robots, and harvesting machines. Blue River Technology (John Deere), Naïo Technologies, and university precision agriculture programs all target ROS 2. Nav2 (the navigation stack) handles field traversal planning natively.

**Surgical Robotics:** Intuitive Surgical's research APIs, the Raven II open research surgical robot, and University of Washington's UWANG all use ROS 2. The action/feedback pattern maps well to surgical motion primitives (move to tissue, apply force, retract).

**Underwater ROVs and AUVs:** The Marine Robotics community uses ROS 2 extensively. ArduSub (underwater autopilot) has a ROS 2 interface. The MBARI (Monterey Bay Aquarium Research Institute) autonomous underwater vehicles run ROS 2.

**Satellite and Space Robotics:** NASA JPL, ESA, and JAXA research groups all use ROS 2 in ground testing. The Canadarm3 program (NASA Artemis) has documented ROS 2 prototyping. PickNik explicitly targets space robotics as a vertical. Astrobotic's CubeRover program uses ROS 2.

**Distributed Sensor Networks:** ROS 2's DDS transport works across LANs with no central broker. This makes it usable as a distributed sensor fusion bus — publishing data from distributed cameras, weather sensors, or flow meters onto a shared ROS 2 graph for a central processing node. Not its primary design target but functionally viable for low-to-medium data rate scenarios.

**Human Motion Capture / Physical Therapy:** ROS 2 is used in wearable exoskeleton and rehabilitation robot research to coordinate joint sensors, force feedback, and user interface elements across a body-worn sensor network.

**Cinematography Rigs:** Robotic camera platforms (cable-suspended cinema rigs, motorized camera sliders) have been built on ROS 2, using the trajectory execution and coordinate frame machinery to coordinate multi-axis moves synchronized to timecode.

## Key Packages and Ecosystem Layers

### Navigation — Nav2

Nav2 is the canonical navigation stack for mobile robots. It provides: global path planning (Dijkstra, A*, NavFn, Smac), local trajectory planning (DWB, RPP, MPPI controllers), costmap management (obstacle inflation, voxel layer, range sensor layer), behavior trees for recovery actions (spin in place, back up, wait), SLAM (Nav2 integrates with slam_toolbox), and localization (AMCL).

```bash
# Launch Nav2 with a pre-built map
ros2 launch nav2_bringup bringup_launch.py \
  map:=/maps/office.yaml \
  use_sim_time:=false

# Send a navigation goal programmatically via action
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose \
  '{pose: {header: {frame_id: map}, pose: {position: {x: 2.0, y: 1.5}, orientation: {w: 1.0}}}}'
```

### Manipulation — MoveIt 2

MoveIt 2 (maintained by PickNik Robotics) provides motion planning (OMPL, STOMP, PILZ, Cartesian planners), collision detection (FCL, Bullet), kinematics (KDL, TracIK, BioIK), grasp planning, and execution with trajectory tracking. It integrates with ros2_control for hardware execution.

```python
# Python MoveIt 2 motion planning example
from moveit.planning import MoveItPy

moveit = MoveItPy(node_name="moveit_py")
arm = moveit.get_planning_component("panda_arm")

# Set goal pose
from geometry_msgs.msg import PoseStamped
goal_pose = PoseStamped()
goal_pose.header.frame_id = "panda_link0"
goal_pose.pose.position.x = 0.5
goal_pose.pose.position.y = 0.0
goal_pose.pose.position.z = 0.5
goal_pose.pose.orientation.w = 1.0

arm.set_goal_state(pose_stamped_msg=goal_pose, pose_link="panda_hand")
plan_result = arm.plan()

if plan_result:
    moveit.execute(plan_result.trajectory, blocking=True)
```

### SLAM — slam_toolbox

`slam_toolbox` is the maintained SLAM package for ROS 2, replacing the older `gmapping` and `cartographer` packages for most use cases. It provides 2D lifelong mapping (continuously extending and updating a map across sessions), localization against existing maps, and serialization/deserialization of map poses.

### Simulation — Gazebo Harmonic / Gazebo Classic

The Gazebo simulator (now "Gazebo Harmonic" or "Gazebo Garden" — the project was renamed from Ignition Gazebo) is the primary ROS 2-integrated physics simulator. It uses the `ros_gz_bridge` to bridge Gazebo topics into the ROS 2 graph, allowing the same robot nodes to run against a simulator or physical hardware by swapping the hardware interface and setting `use_sim_time:=true`.

### Visualization — RViz2

RViz2 is the standard 3D visualization tool. It subscribes to ROS 2 topics and renders: laser scans, point clouds, camera images, TF frames, robot URDF models with joint state animation, Nav2 costmaps and paths, and marker arrays for custom visualizations. RViz2 is also a runtime introspection tool — the ability to add/remove displays, scrub through recorded bags, and inspect message content at runtime is central to the ROS 2 development workflow.

### Recording and Replay — ros2 bag

`ros2 bag` records any set of topics to a SQLite3 or MCAP file, preserving all message timestamps for exact replay. This is essential for debugging, data collection, and testing — record a robot run once, replay it offline against different processing algorithms.

```bash
# Record all topics
ros2 bag record -a -o my_robot_run

# Record specific topics
ros2 bag record /scan /odom /camera/color/image_raw -o sensor_capture

# Replay (publishes to the same topics at original rate)
ros2 bag play my_robot_run

# Inspect bag contents
ros2 bag info my_robot_run
```

## Best Practices

**Use Composition (rclcpp::Component) for production deployments.** Running each node as a separate OS process has overhead: IPC between nodes uses the DDS network stack even on localhost, adding latency and CPU load. Node composition lets multiple nodes run as shared libraries within a single process, communicating via in-process memory copies at full memory bandwidth. For high-frequency sensor data pipelines and closed-loop control, this can reduce latency by 10–100x.

**Lifecycle Nodes for system state management.** `rclcpp_lifecycle::LifecycleNode` provides a managed state machine (unconfigured → inactive → active → finalized) for hardware drivers and critical components. This allows orderly startup/shutdown sequencing and is required by ros2_control hardware interfaces.

**Use RELIABLE QoS for command channels; BEST_EFFORT for sensor streams.** A missed velocity command that causes the robot to continue at the last command is a safety issue. A dropped lidar scan is usually acceptable. The default QoS in ROS 2 is `RELIABLE` with `KEEP_LAST(10)` — this is appropriate for most non-sensor topics but adds queuing latency and retransmission overhead for high-rate sensor data.

**Pin to a Long-Term Support (LTS) distribution in production.** Jazzy Jalisco (Ubuntu 24.04, supported through May 2029) and Humble Hawksbill (Ubuntu 22.04, EOL May 2027) are the LTS choices. Non-LTS distributions release every six months and have shorter support windows. For production deployments, use LTS and plan migration cycles accordingly.

**Use `rosdep` and `colcon` consistently across development and CI.** `rosdep install --from-paths src --ignore-src -r -y` installs all declared package dependencies. `colcon build --symlink-install` builds the workspace with symlinks to Python source, allowing Python nodes to be edited without rebuilding. Consistent use of these tools avoids the "works on my machine" class of dependency drift.

**Separate robot description from behavior.** URDF/xacro files describe the physical robot (link geometry, joint limits, inertia, sensor placements). Keep these in a dedicated `_description` package separate from controller and application packages. This allows the same robot model to be used in simulation, visualization, and hardware contexts without modification.

**For real-time control, isolate the ros2_control loop from ROS 2 middleware.** The `ros2_control` controller manager runs the read/update/write loop in a dedicated thread. Use `chrt` (realtime scheduling policy) and CPU isolation (`isolcpus` kernel parameter) to pin this thread to a dedicated core. The DDS middleware threads should not compete with the control loop for CPU time.

## Limitations

**ROS 2 is not a real-time operating system and does not provide hard real-time guarantees.** The DDS middleware, dynamic memory allocation, and Linux scheduler jitter mean ROS 2 nodes have non-deterministic latency — typically acceptable at 50–500 Hz but not suitable for microsecond-precision control loops. Hard real-time control (kilohertz servo loops, laser interlock logic) belongs below the ROS 2 layer, on an MCU or RTOS.

**Steep learning curve.** A new user must simultaneously learn: the ROS 2 build system (colcon + ament), the DDS discovery model, C++ or Python node architecture, URDF, launch files, the TF2 transform system, and the specific packages for their robot domain (Nav2 for mobile, MoveIt for arms). The accumulated API surface is large and documentation quality is uneven.

**Package quality is inconsistent.** The ROS 2 ecosystem is a mix of carefully maintained packages (ros2_control, Nav2, MoveIt 2) and abandoned or minimally-tested community packages. Packages for specific hardware often lag behind the latest ROS 2 distribution. Always check the package's last commit date, CI status, and open issue count before depending on it.

**DDS discovery does not scale linearly to large fleets.** DDS peer discovery via multicast uses increasing network bandwidth as the number of nodes grows. In large multi-robot deployments (>20 robots on a shared LAN), DDS discovery overhead can saturate the network. Mitigations: ROS 2 domain IDs to partition discovery, DDS router/bridge configurations, or dedicated discovery servers.

**No built-in security model at the application layer.** DDS-SECURITY provides transport-layer security, but ROS 2 has no application-level access control, authentication, or capability model. Any node on the DDS domain can publish to any topic. In multi-tenant or public-facing robot deployments, this requires additional hardening (network segmentation, allowlists, Sros2 key infrastructure setup — which is complex and rarely deployed in practice).

**Windows support is functional but second-class.** Most robot hardware drivers assume Linux. Many packages have not been tested on Windows. Development and deployment on Linux (Ubuntu) is strongly recommended for anything beyond simulation.

**The ROS 1 → ROS 2 migration was a breaking change.** ROS 1 Noetic reached EOL May 2025. Systems built on ROS 1 require significant porting effort — the communications APIs, build system, and launch system are all different. Legacy industrial deployments with large ROS 1 codebases remain a real migration debt.

## Distributions and Support Lifecycle

| Distribution | Ubuntu Target | Release Date | EOL |
|-------------|---------------|--------------|-----|
| **Jazzy Jalisco** (LTS) | Ubuntu 24.04 | May 2024 | May 2029 |
| **Iron Irwini** | Ubuntu 22.04 | May 2023 | November 2024 |
| **Humble Hawksbill** (LTS) | Ubuntu 22.04 | May 2022 | May 2027 |
| **Galactic Geochelone** | Ubuntu 20.04 | May 2021 | November 2022 |
| **Foxy Fitzroy** (LTS) | Ubuntu 20.04 | June 2020 | May 2023 |

ROS 2 LTS distributions align with Ubuntu LTS releases and are supported for five years. Non-LTS distributions are supported for approximately eighteen months.

## Notable Developments

- **2025-05:** ROS 1 Noetic Ninjemys reached end-of-life. ROS 2 is now the only supported ROS distribution.
- **2024-05:** Jazzy Jalisco (LTS) released targeting Ubuntu 24.04; five-year support window to 2029.
- **2023:** Open Robotics reorganized; the ROS 2 project governance transitioned to the Open Source Robotics Alliance (OSRA), a broader community-governed structure.
- **2022-05:** Humble Hawksbill (LTS) released; became the most widely deployed ROS 2 distribution in production systems as of 2025.
- **2021:** ros2_control v1.0 released, replacing the ad-hoc hardware interface patterns of early ROS 2 and establishing the controller manager as the canonical hardware abstraction.
- **2020:** Nav2 (Navigation2) reached production readiness; replaced the ROS 1 navigation stack as the standard mobile robot navigation framework.
- **2019:** MoveIt 2 initial release (Alpha); began the multi-year migration of the ROS 1 MoveIt manipulation stack to ROS 2.
- **2017-12:** ROS 2 Ardent Apalone — first stable release. DDS transport, no rosmaster, real-time support foundations.

## Key Organizations

- **Open Source Robotics Foundation / Open Source Robotics Alliance (OSRF/OSRA)** — Stewards the core ROS 2 packages, build infrastructure, and release process. [openrobotics.org](https://openrobotics.org)
- **PickNik Robotics** — Primary commercial maintainer of MoveIt 2; largest single commercial contributor to the ROS 2 manipulation stack. See [PickNik entry]({{< relref "picknik-robotics.md" >}}).
- **Apex.AI** — Produces Apex.OS, a commercially supported, ASIL-certified distribution of ROS 2 for automotive and safety-critical applications. [apex.ai](https://www.apex.ai)
- **Canonical** — Produces Ubuntu Core with ROS 2 snap packaging; long-term support for embedded ROS 2 deployments. [ubuntu.com/robotics](https://ubuntu.com/robotics)
- **eProsima** — Develops Fast DDS (default DDS implementation) and Micro XRCE-DDS (the micro-ROS transport protocol). [eprosima.com](https://eprosima.com)

## Sources

- [ROS 2 Documentation (Rolling)](https://docs.ros.org/en/rolling/index.html)
- [ROS 2 Design Documentation](https://design.ros2.org/)
- [ROS 2 GitHub](https://github.com/ros2/ros2)
- [About ROS — ros.org](https://www.ros.org/about-ros/)
- [ros2_control Documentation](https://control.ros.org/rolling/index.html)
- [Nav2 Documentation](https://docs.nav2.org/)
- [MoveIt 2 Documentation](https://moveit.picknik.ai/)
- [micro-ROS Documentation](https://micro.ros.org/)
- [PickNik ROS 2 Hardware Ecosystem](https://picknik.ai/hardware-ecosystem/)
