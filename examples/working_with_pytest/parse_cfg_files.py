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


def test_get_intf_ip_from_cfg():
    cfg = "config_sw1.txt"
    result = get_intf_ip_from_cfg(cfg)
    assert type(result) == dict, "Функция должна возвращать словарь"
    assert len(result) == 1
    assert result == {"Vlan100": "10.0.100.1"}

def test_get_intf_ip_from_cfg_second_cfg():
    cfg = "config_r1.txt"
    result = get_intf_ip_from_cfg(cfg)
    assert type(result) == dict, "Функция должна возвращать словарь"
    assert len(result) == 3
    assert result == {"Loopback": "10.1.1.1"}
