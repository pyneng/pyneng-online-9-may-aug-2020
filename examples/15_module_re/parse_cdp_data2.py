import re
from pprint import pprint


regex = (
    r"Device ID: (?P<device>\S+)"
    r"|IP address: (?P<ip>\S+)"
    r"|Platform: (?P<platform>.+?),"
    r"|, +Version +(?P<ios>.+?),"
    r"|Interface: (?P<port1>\S+), +.+: (?P<port2>\S+)"
)

result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            group_name = match.lastgroup
            if group_name == "device":
                device = match.group("device")
                result[device] = {}
            elif group_name == "port2":
                result[device]["port1"] = match.group("port1")
                result[device]["port2"] = match.group("port2")
            else:
                value = match.group(group_name)
                result[device][group_name] = value

pprint(result, width=60)
