from pprint  import pprint

files = ["config_r1.txt", "config_sw1.txt", "config_sw2.txt"]

output = []

for filename in files:
    with open(filename) as f:
        for line in f:
            words = line.split()
            if "hostname" in line:
                host = words[-1]
            elif line.startswith("interface"):
                interface = words[-1]
            elif line.startswith(" ip address"):
                ip = words[-2]
                output.append([host, interface, ip])
            elif "router ospf" in line or "alias" in line:
                break

pprint(output)
