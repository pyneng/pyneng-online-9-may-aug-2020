import re
from pprint import pprint


def parse_cdp(filename):
    regex = (
        r"Device ID: (?P<device>\S+)"
        r"|IP address: (?P<ip>\S+)"
        r"|Platform: (?P<platform>\S+ \S+),"
        r"|Cisco IOS Software, (?P<ios>.+), RELEASE"
    )

    result = {}

    with open("sh_cdp_neighbors_sw1.txt") as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                last = match.lastgroup
                value = match.group(last)
                #print(f"Lastgroup = {last:10}, {value}")
                if last == "device":
                    device = value
                    result[device] = {}
                else:
                    result[device][last] = value

    return result


pprint(parse_cdp("sh_cdp_neighbors_sw1.txt"))
