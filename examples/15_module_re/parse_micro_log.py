import re


regex = (
    r"Host (\S+) "
    r"in vlan (\d+) "
    r".+"
    r"port (\S+) and port (\S+)"
)


ports = set()

with open("log.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            host, vlan, port1, port2 = match.groups()
            ports.update([port1, port2])

print(ports)
