import ipaddress


class Network:
    def __init__(self, network):
        self.network = network
        address, mask = network.split("/")
        self.network_address = address
        self.mask = int(mask)
        self.bin_mask = "1" * self.mask + "0" * (32 - self.mask)

    def hosts(self):
        net = ipaddress.ip_network(self.network)
        return [str(ip) for ip in net.hosts()]

    def __repr__(self):
        return f"Network('{self.network}')"

    def __str__(self):
        return f"{self.network}"

    def __len__(self):
        return len(self.hosts())
