import ipaddress

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def main():
    ip1 = "10.1.1.1"
    ip2 = "1.1.1"
    print(ip1, check_ip(ip1))
    print(ip2, check_ip(ip2))


if __name__ == "__main__":
    main()
