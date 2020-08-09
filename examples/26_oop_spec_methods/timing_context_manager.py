import time


class RunningTime:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop = time.time()
        print(f"Время работы {round(self.stop - self.start, 3)}")


# In [4]: with RunningTime():
#    ...:     time.sleep(8)
#    ...:
# Время работы 8.008


# In [9]: with RunningTime():
#    ...:     with ConnectHandler(**r1) as ssh:
#    ...:         ssh.enable()
#    ...:         print(ssh.send_command("sh run | i hostname"))
#    ...:         print(ssh.send_command("sh clock"))
#    ...:
# hostname R1
# *11:07:10.374 UTC Sun Aug 9 2020
# Время работы 9.024
