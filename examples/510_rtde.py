from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from rtde_io import RTDEIOInterface

from compas.robots import Configuration


def get_config(ip="127.0.0.1"):
    # Create UR Client
    ur_r = RTDEReceive(ip)

    # Read value of joints
    robot_joints = ur_r.getActualQ()

    # Print received values
    config = Configuration.from_revolute_values(robot_joints)
    return config


def move_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    ur_c.moveJ(config.joint_values, speed, accel, nowait)


def movel_to_joints(config, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)
    ur_c.moveL_FK(config.joint_values, speed, accel, nowait)


def send_trajectory(configs, speed, accel, nowait, ip="127.0.0.1"):
    # speed rad/s, accel rad/s^2, nowait bool
    ur_c = RTDEControl(ip)

    for config in configs:
        ur_c.moveJ(config.joint_values, speed, accel, nowait)


def get_digital_io(signal, ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    return ur_r.getDigitalOutState(signal)


def set_digital_io(signal, value, ip="127.0.0.1"):
    io = RTDEIOInterface(ip)
    io.setStandardDigitalOut(signal, value)


def set_tool_digital_io(signal, value, ip="127.0.0.1"):
    io = RTDEIOInterface(ip)
    io.setToolDigitalOut(signal, value)


def get_tcp_pose(ip="127.0.0.1"):
    ur_r = RTDEReceive(ip)
    tcp = ur_r.getActualTCPPose()
    return tcp


if __name__ == "__main__":
    ip = "192.168.0.10"
    ur_c = RTDEControl(ip)
    tcp = ur_c.getTCPOffset()
    # tcp = [-0.0016567930579185486, 9.985990618588403e-05, 0.07716625928878784]
    print (tcp)

    cfg = get_config(ip)
    print(cfg.joint_values)
