import pytest
import task_27_2c
import task_27_2a
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_27_2c, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    r1 = task_27_2c.MyNetmiko(**first_router_from_devices_yaml)
    assert isinstance(
        r1, CiscoIosSSH
    ), "Класс MyNetmiko должен наследовать CiscoIosSSH"
    check_attr_or_method(r1, method="send_command")
    r1.send_command("sh ip int br", strip_command=False)
    r1.disconnect()
