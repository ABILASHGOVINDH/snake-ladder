from time import sleep
from threading import *

class Hi(Thread):
    def run(self):
        for i in range(8):
         print("Hi")
         sleep(0.3)


class Hello(Thread):
    def run(self):
        for i in range(8):
         print("Hello")
         sleep(0.3)


s = Hi()
v = Hello()

s.start()
sleep(0.2)
v.start()

v.join()
s.join()
print("bye")