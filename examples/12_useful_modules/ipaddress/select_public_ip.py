import ipaddress
import click


public_ip_map = {}

with open("config_r1.txt") as f:
    for line in f:
        words = line.split()
        if line.startswith("interface"):
            intf = words[-1]
        elif line.startswith(" ip address"):
            ip = ipaddress.ip_address(words[-2])
            if ip.is_global:
                public_ip_map[intf] = str(ip)
print(public_ip_map)




