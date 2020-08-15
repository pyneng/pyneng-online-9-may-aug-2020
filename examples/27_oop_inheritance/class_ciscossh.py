from netmiko import ConnectHandler


class CiscoSSH:
    def __init__(self, ip, username, password, secret, device_type):
        print("CiscoSSH __init__")
        self.ssh = ConnectHandler(
            host=ip,
            username=username,
            password=password,
            secret=secret,
            device_type=device_type,
        )

    def send_show_commands(self, command):
        prompt = self.ssh.find_prompt()
        output = self.ssh.send_command(command)
        return f"{prompt}{command}\n{output}"

