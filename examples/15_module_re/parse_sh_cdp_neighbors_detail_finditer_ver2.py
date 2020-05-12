import re
from pprint import pprint


def parse_cdp(filename):
    regex = (
        r"Device ID: (?P<device>\S+)"
        r".*?"
        r"IP address: (?P<ip>\S+)\n"
        r"Platform: (?P<platform>.+?),"
        r".*?"
        r"Cisco IOS Software, (?P<ios>.+?),"
    )

    result = {}

    with open(filename) as f:
        match_iter = re.finditer(regex, f.read(), re.DOTALL)
        for match in match_iter:
            device = match.group("device")
            groupdict = match.groupdict()
            del groupdict["device"]
            result[device] = groupdict

    return result


pprint(parse_cdp("sh_cdp_neighbors_sw1.txt"))
