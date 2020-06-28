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
    match = re.finditer(regex, f.read(), re.DOTALL | re.MULTILINE)
    for m in match:
        device = m.group("device")
        params = m.groupdict()
        del params["device"]
        result[device] = params

pprint(result, width=60)
