import telnetlib
import time


def connect(ip, username, password, enable_password=None, disable_paging=True):
    telnet = telnetlib.Telnet(ip)
    telnet.read_until(b"Username:")
    telnet.write(username.encode("ascii") + b"\n")
    telnet.read_until(b"Password:")
    telnet.write(password.encode("ascii") + b"\n")
    if enable_password:
        telnet.write(b"enable\n")
        telnet.read_until(b"Password:")
        telnet.write(enable_password.encode("ascii") + b"\n")
    if disable_paging:
        telnet.write(b"terminal length 0\n")
    time.sleep(0.5)
    telnet.read_very_eager()
    return telnet


def send_show_command(connection, command):
    connection.write(command.encode("ascii") + b"\n")
    time.sleep(1)
    output = connection.read_very_eager().decode("ascii")
    check_errors(output)
    return output


def check_errors(command_output):
    if "Invalid input detected" in command_output:
        raise ValueError("Возникла ошибка Invalid input detected")


def send_config_commands(connection, commands):
    connection.write("conf t".encode("ascii") + b"\n")
    for command in commands:
        connection.write(command.encode("ascii") + b"\n")
        time.sleep(0.2)
    output += telnet.read_very_eager().decode("ascii")
    connection.write("end".encode("ascii") + b"\n")
    return output


if __name__ == "__main__":
    r1 = connect("192.168.100.1", "cisco", "cisco", "cisco")
    sh_ip_int_br = send_show_command(r1, "sh ip int br")
    print(sh_ip_int_br)
