import re
from pprint import pprint


regex = (
    r"^Device ID: (?P<device>\S+)"
    r".*?"
    r"^ +IP address: (?P<ip>\S+)\n"
    r"^Platform: (?P<platform>.+?),"
    r".*?"
    r", Version (?P<ios>\S+),"
)

result = {}
with open("sh_cdp_neighbors_sw1.txt") as f:
    match = re.findall(regex, f.read(), re.DOTALL | re.MULTILINE)
    for m in match:
        device, ip, platform, ios = m
        result[device] = {"ip": ip, "platform": platform, "ios": ios}

pprint(result, width=60)
