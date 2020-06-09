from pprint import pprint

result = {}
output = ""

with open("sh_ip_interface.txt") as f:
    for line in f:
        words = line.split()
        if "line protocol is" in line:
            intf = words[0]
        elif "Internet address" in line:
            ip = words[-1]
        elif "MTU is" in line:
            mtu = words[2]
            output += f"{intf:20}{ip:20}{mtu:5}\n"

with open("intf_ip_mtu.txt", "w") as f:
    f.write(output)

