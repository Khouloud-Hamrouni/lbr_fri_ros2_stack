import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/khamrouni/lbr-stack/src/lbr_fri_ros2_stack/install/lbr_moveit'
