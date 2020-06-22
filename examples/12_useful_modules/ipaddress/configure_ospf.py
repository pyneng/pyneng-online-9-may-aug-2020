import ipaddress

private_ip_list = []

with open("config_r1.txt") as f:
    for line in f:
        words = line.split()
        if line.startswith(" ip address"):
            ip = ipaddress.ip_address(words[-2])
            if not ip.is_global:
                private_ip_list.append(str(ip))
print(private_ip_list)

for ip in private_ip_list:
    print(f" network {ip} 0.0.0.0 area 0")
