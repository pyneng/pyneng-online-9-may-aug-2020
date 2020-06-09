from pprint import pprint

ip_dict = {}

with open("sh_ip_int_br.txt") as f:
    for line in f:
        columns = line.split()
        print(columns)
        try:
            intf = columns[0]
            if intf[-1].isdigit():
                ip = columns[1]
                ip_dict[intf] = ip
        except IndexError:
            pass


pprint(ip_dict)
