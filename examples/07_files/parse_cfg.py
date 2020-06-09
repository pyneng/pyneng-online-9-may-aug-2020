from pprint  import pprint

result = {}

with open("cfg.txt") as f:
    for line in f:
        words = line.split()
        if line.startswith("interface"):
            interface = words[-1]
        elif line.startswith(" ip address"):
            ip = words[-2]
            print(interface, ip)
