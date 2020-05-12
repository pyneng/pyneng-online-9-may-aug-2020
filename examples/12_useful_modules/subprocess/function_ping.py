
import subprocess


def ping_ip(ip):
    result = subprocess.run(f"ping -c 2 {ip}", shell=True,
                             encoding='utf-8')
    print(result.returncode)
    if result.returncode == 0:
        return True
    else:
        return False


print(ping_ip('8.8.8.8'))
