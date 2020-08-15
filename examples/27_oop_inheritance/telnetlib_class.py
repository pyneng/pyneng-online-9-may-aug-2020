import telnetlib
import time
from pprint import pprint


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


class BaseTelnet:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username")
        self._telnet.write(to_bytes(username))
        self._telnet.read_until(b"Password")
        self._telnet.write(to_bytes(password))
        time.sleep(1)
        self._telnet.read_very_eager()

    def _send_command(self, command):
        self._telnet.write(to_bytes(command))
        time.sleep(1)
        output = self._telnet.read_very_eager()
        return output.decode("utf-8")

    def close(self):
        self._telnet.close()


class CiscoBaseTelnet(BaseTelnet):
    def __init__(
        self, ip, username, password, enable=None, disable_paging=True
    ):
        super().__init__(ip, username, password)

        self._telnet.write(b"enable\n")
        self._telnet.read_until(b"Password")
        self._telnet.write(to_bytes(enable))
        self._telnet.read_until(b"#")
        if disable_paging:
            self._telnet.write(b"terminal length 0\n")
        self._telnet.read_until(b"#")

    def send_show_command(self, command):
        self._telnet.write(to_bytes(command))
        output = self._telnet.read_until(b"#").decode("utf-8")
        return output


class CiscoIosTelnet(CiscoBaseTelnet):
    pass
