from pprint import pprint

ip_dict = {}

with open("sh_ip_int_br.txt") as f:
    for line in f:
        columns = line.split()
        # print(columns)
        if columns and columns[0][-1].isdigit():
            intf = columns[0]
            ip = columns[1]
            ip_dict[intf] = ip


pprint(ip_dict)
