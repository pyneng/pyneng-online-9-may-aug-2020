from pprint  import pprint



def get_intf_ip_from_cfg(filename):
    output = {}
    with open(filename) as f:
        for line in f:
            words = line.split()
            if line.startswith("interface"):
                interface = words[-1]
            elif line.startswith(" ip address"):
                ip = words[-2]
                output[interface] = ip
    return output


files = ["config_r1.txt", "config_sw1.txt", "config_sw2.txt"]

all_data = {}

for file in files:
    host = file.split(".")[0].split("_")[-1]
    result = get_intf_ip_from_cfg(file)
    pprint(result)
    all_data[host] = result

print("####################")
pprint(all_data)
