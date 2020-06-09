
with open("sh_ip_int_br.txt") as f:
    for line in f:
        columns = line.split()
        if columns and columns[0][-1].isdigit():
            intf = columns[0]
            ip = columns[1]
            print(f"{intf:20}{ip:15}")
