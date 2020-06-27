import re
from pprint import pprint

result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = line.split()[-1]
        elif line.startswith("Interface"):
            m = re.search(r"Port ID \(outgoing port\): (\S+)", line)
            r_intf = m.group(1)
        elif line.startswith("Cisco IOS Software"):
            regex = r", +Version +(.+?),"
            ios = re.search(regex, line).group(1)
            result[device] = (ios, r_intf)

pprint(result)
