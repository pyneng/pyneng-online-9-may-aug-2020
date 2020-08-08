import telnetlib
import time
from pprint import pprint


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


class CiscoTelnet:
    def __init__(self, ip, username, password, enable=None):
        self.ip = ip
        self.username = username
        self.password = password
        self.enable = enable

        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username")
        self._telnet.write(to_bytes(username))
        self._telnet.read_until(b"Password")
        self._telnet.write(to_bytes(password))
        if enable:
            self._telnet.write(b"enable\n")
            self._telnet.read_until(b"Password")
            self._telnet.write(to_bytes(enable))
            self._telnet.read_until(b"#", timeout=5)
        self._telnet.write(b"terminal length 0\n")
        self._telnet.read_until(b"#", timeout=5)
        time.sleep(3)
        self._telnet.read_very_eager()

    def send_show_command(self, command):
        output = self._send_line_wait(command)
        return output

    def config_mode(self):
        self._telnet.write(b"conf t\n")
        output = self._telnet.read_until(b"#", timeout=10).decode("utf-8")
        return output

    def exit_config_mode(self):
        self._telnet.write(b"end\n")
        output = self._telnet.read_until(b"#", timeout=10).decode("utf-8")
        return output

    def send_config_commands(self, commands):
        output = self.config_mode()
        if type(commands) == str:
            commands = [commands]
        for command in commands:
            self._telnet.write(to_bytes(command))
            output += self._telnet.read_until(b"#", timeout=10).decode("utf-8")
        output += self.exit_config_mode()
        return output

    def _send_line_wait(self, line, wait="#"):
        wait_b = wait.encode("utf-8")
        self._telnet.write(to_bytes(line))
        output = self._telnet.read_until(wait_b, timeout=10).decode("utf-8")
        return output

    def close(self):
        self._telnet.close()

