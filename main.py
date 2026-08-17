from time import sleep
from os import system

text = "Hello there I have been waiting for this since a long time"
system("cls")

for t in text:
    print(t, end="", flush=True)
    sleep(0.1)


print()