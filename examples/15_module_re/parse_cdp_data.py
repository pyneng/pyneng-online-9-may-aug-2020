import re
from pprint import pprint

result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = line.split()[-1]
            result[device] = {}
        elif "IP address" in line:
            ip = line.split()[-1]
            result[device]["ip"] = ip
        elif line.startswith("Platform"):
            regex = r"Platform: (.+?),"
            platform = re.search(regex, line).group(1)
            result[device]["platform"] = platform
        elif line.startswith("Cisco IOS Software"):
            regex = r", +Version +(.+?),"
            ios = re.search(regex, line).group(1)
            result[device]["ios"] = ios
        elif line.startswith("Interface"):
            regex = r": (\S+), +.+: (\S+)"
            m = re.search(regex, line)
            result[device]["port1"] = m.group(1)
            result[device]["port2"] = m.group(2)

pprint(result, width=120)


{"SW2": {"ios": "12.2(55)SE9",
         "ip": "10.1.1.2",
         "platform": "cisco WS-C2960-8TC-L"
        }}


result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = line.split()[-1]
        elif "IP address" in line:
            ip = line.split()[-1]
        elif line.startswith("Platform"):
            regex = r"Platform: (.+?),"
            platform = re.search(regex, line).group(1)
        elif line.startswith("Cisco IOS Software"):
            regex = r", +Version +(.+?),"
            ios = re.search(regex, line).group(1)
            result[device] = {"ios": ios, "ip": ip, "platform": platform}

pprint(result, width=120)
