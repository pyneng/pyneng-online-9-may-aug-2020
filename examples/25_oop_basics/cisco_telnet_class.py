import telnetlib
import time


class CiscoTelnet:
    def __init__(
        self, ip, username, password, enable_password=None, disable_paging=True
    ):
        self.ip = ip
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self.telnet.write(username.encode("ascii") + b"\n")

        self.telnet.read_until(b"Password:")
        self.telnet.write(password.encode("ascii") + b"\n")
        if enable_password:
            self.telnet.write(b"enable\n")
            self.telnet.read_until(b"Password:")
            self.telnet.write(enable_password.encode("ascii") + b"\n")
        if disable_paging:
            self.telnet.write(b"terminal length 0\n")
        time.sleep(0.5)
        self.telnet.read_very_eager()

    def send_show_command(self, command):
        self.telnet.write(command.encode("ascii") + b"\n")
        time.sleep(1)
        output = self.telnet.read_very_eager().decode("ascii")
        self.check_errors(output)
        return output

    def close(self):
        self.telnet.close()

    def check_errors(self, command_output):
        if "Invalid input detected" in command_output:
            raise ValueError("Возникла ошибка Invalid input detected")

    def config_mode(self):
        self.telnet.write(b"conf t\n")
        time.sleep(0.5)
        return self.telnet.read_very_eager().decode("ascii")

    def exit_config_mode(self):
        self.telnet.write(b"end\n")
        time.sleep(0.5)
        return self.telnet.read_very_eager().decode("ascii")

    def send_config_commands(self, commands):
        # if type(commands) == str:
        #    commands = [commands]
        output = self.config_mode()
        for command in commands:
            self.telnet.write(command.encode("ascii") + b"\n")
            time.sleep(0.2)
        output += self.telnet.read_very_eager().decode("ascii")
        output += self.exit_config_mode()
        return output
