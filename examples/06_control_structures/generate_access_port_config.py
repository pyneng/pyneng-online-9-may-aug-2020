access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access = {"0/12": 10, "0/14": 11, "0/16": 17, "0/17": 150}

for intf, vlan in access.items():
    print(f"interface {intf}")
    for command in access_template:
        if command.endswith('access vlan'):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")

