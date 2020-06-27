import re
from pprint import pprint


regex = (
    r"(?P<mac>\S+) +"  # мак адрес
    r"(?P<ip>\S+) +"  # ip адрес
    r"\d+ +\S+ +"  # lease, type
    r"(?P<vlan>\d+) +"  # vlan
    r"(?P<intf>\S+)"  # interface
)

result = []

with open("dhcp_snooping.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            result.append(match.group("intf", "vlan", "ip", "mac"))

pprint(result)
