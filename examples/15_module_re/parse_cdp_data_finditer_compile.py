import re
from pprint import pprint


regex = re.compile((
    r"^Device ID: (?P<device>\S+)"
    r".*?"
    r"^ +IP address: (?P<ip>\S+)\n"
    r"^Platform: (?P<platform>.+?),"
    r".*?"
    r", Version (?P<ios>\S+),"),
    re.DOTALL | re.MULTILINE
)

result = {}
with open("sh_cdp_neighbors_sw1.txt") as f:
    match = regex.finditer(f.read())
    for m in match:
        device = m.group("device")
        params = m.groupdict()
        del params["device"]
        result[device] = params

pprint(result, width=60)
