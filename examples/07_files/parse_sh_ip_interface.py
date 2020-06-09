from pprint import pprint

result = {}

with open("sh_ip_interface.txt") as f:
    for line in f:
        words = line.split()
        if "line protocol is" in line:
            intf = words[0]
            result[intf] = {}
        elif "Internet address" in line:
            ip = words[-1]
            result[intf]["ip"] = ip
        elif "MTU is" in line:
            mtu = words[2]
            print(f"{intf:20}{ip:20}{mtu:5}")
            result[intf]["mtu"] = mtu
            #result[intf] = {"ip": ip, "mtu": mtu}


pprint(result)

{'Ethernet0/0': {'ip': '192.168.100.1/24', 'mtu': '1500'},
 'Ethernet0/1': {'ip': '192.168.200.1/24', 'mtu': '1500'},
 'Ethernet0/2': {'ip': '19.1.1.1/24', 'mtu': '1500'},
 'Ethernet0/3': {'ip': '192.168.230.1/24', 'mtu': '1500'},
 'Loopback0': {'ip': '4.4.4.4/32', 'mtu': '1514'}}
