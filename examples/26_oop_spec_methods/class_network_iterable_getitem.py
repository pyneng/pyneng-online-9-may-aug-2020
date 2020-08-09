import ipaddress


class Network:
    def __init__(self, network):
        self.network = network
        address, mask = network.split("/")
        self.network_address = address
        self.mask = int(mask)
        self.bin_mask = "1" * self.mask + "0" * (32 - self.mask)
        net = ipaddress.ip_network(self.network)
        self.hosts = (str(ip) for ip in net.hosts())

    def __repr__(self):
        return f"Network('{self.network}')"

    def __str__(self):
        return f"{self.network}"

    def __len__(self):
        print("__len__")
        return len(self.hosts())

    def __getitem__(self, index):
        print("Работает __getitem__")
        return self.hosts[index]
