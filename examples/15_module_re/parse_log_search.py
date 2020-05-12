import re

regex = (r"vlan (?P<vlan>\d+) is flapping between "
         r"port (?P<port1>\S+) and port (?P<port2>\S+)")


ports = set()

with open('log.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan, port1, port2 = match.groups()
            ports.update({port1, port2})

print("Петля между портами {} в VLAN {}".format(", ".join(ports), vlan))
