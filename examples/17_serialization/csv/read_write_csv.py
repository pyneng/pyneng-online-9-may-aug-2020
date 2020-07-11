import csv

with open("rib.table.lg.ba.ptt.br-BGP.csv") as f, open("result.csv", "w") as dest:
    read = csv.DictReader(f)
    keys = "status,network,netmask,nexthop,metric,locprf,weight,path,origin".split(",")
    wr = csv.DictWriter(dest, fieldnames=keys)
    wr.writeheader()
    for index, line in enumerate(read):
        # print(dict(line))
        if line["nexthop"] == "200.219.145.23":
            wr.writerow(line)
