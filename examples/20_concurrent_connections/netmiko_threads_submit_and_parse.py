from pprint import pprint
from datetime import datetime
import logging
import yaml
import time
import re
from itertools import repeat
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from concurrent.futures import ThreadPoolExecutor, as_completed
import random


logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    format='%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show_command(device, show):
    start_msg = "===> {} Connection: {}"
    received_msg = "<=== {} Received:   {}"
    ip = device["host"]
    logging.info(start_msg.format(datetime.now().time(), ip))

    try:
        with ConnectHandler(**device) as ssh:
            time.sleep(random.random()*10)
            ssh.enable()
            result = ssh.send_command(show)
            logging.info(received_msg.format(datetime.now().time(), ip))
            return ip, result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        logging.warning(error)


def send_command_to_devices(devices, command, parse_command_func):
    result_dict = {}
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_list = []
        for device in devices:
            f = executor.submit(
                send_show_command, device, show=command
            )
            future_list.append(f)
        for future in as_completed(future_list):
            ip, out = future.result()
            result_dict[ip] = parse_command_func(out)
    return result_dict


def parse_sh_ip_int_br(output):
    regex = r"(\S+) +([\d.]+) +"
    intf_ip_dict = {}
    for match in re.finditer(regex, output):
        intf, ip = match.groups()
        intf_ip_dict[intf] = ip
    return intf_ip_dict


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    result_dict = send_command_to_devices(
        devices, "sh ip int br", parse_sh_ip_int_br
    )
    pprint(result_dict)
