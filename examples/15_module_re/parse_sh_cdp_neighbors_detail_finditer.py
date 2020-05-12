import re
from pprint import pprint


def parse_cdp(filename):
    cdp = {}

    regex = (
        r"Device ID: (?P<device>\S+)" # имя устройства
        r"|IP address: (?P<ip>\S+)"
        r"|Platform: (?P<platform>.+),"
        r"|Cisco IOS Software, (?P<ios>.+),"
    )

    with open(filename) as f:
        matches = re.finditer(regex, f.read())
        for match in matches:
            #print(match.groups())
            last = match.lastgroup
            value = match.group(last)
            #print(f"Lastgroup = {last:10}, {value}")
            if last == "device":
                device = value
                cdp[device] = {}
            else:
                cdp[device][last] = value

    return cdp


pprint(parse_cdp("sh_cdp_neighbors_sw1.txt"))

