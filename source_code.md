import string
import random
from time import sleep

print("Welcome to random WiFi Password generator_Console based Program")
sleep(1)
print("This program gives you strong password for your WiFi\nBy using uppercase, lowercase, digits and punctuation in "
      "the password")
sleep(1)
print("Please choose the length of the password :")
print("1.10")
print("2.20")
print("3.50")
print("4.100")
print("5.200")
print("Type 'info' for Info")
print("Type 'exit' to exit program")
for attempt in range(0,99):
    usr_input = usrinput = input("Enter input :")
    if usr_input in ("1"):
        def randomString(stringLength=10):
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            return ''.join(random.choice(letters) for i in range(stringLength))
        print(randomString())
    if usr_input in ("2"):
        def randomString(stringLength=20):
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            return ''.join(random.choice(letters) for i in range(stringLength))
        print(randomString())
    if usr_input in ("3"):
        def randomString(stringLength=50):
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            return ''.join(random.choice(letters) for i in range(stringLength))
        print(randomString())
    if usr_input in ("4"):
        def randomString(stringLength=100):
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            return ''.join(random.choice(letters) for i in range(stringLength))
        print(randomString())
    if usr_input in ("5"):
        def randomString(stringLength=200):
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            return ''.join(random.choice(letters) for i in range(stringLength))
        print(randomString())
    if usr_input == "info":
        print("This program was made by Linkachus17 using Python language!\nI make this program because of my "
              "creativity\nYou may ask : Why not use another program or Online service that gives you a random "
              "password too?\nThe answer : I am not stopping you to use another program that you think it's best for "
              "you.\nIf you use my program that means you appreciate my hard work and love my creativity.\nAnd yes "
              "maybe my program has limited feature than other program too.\nThanks to : Laken Jason Brion and Python "
              "Discord server for helping me to make this program!\nAlso check out my Youtube channel, it's not big "
              "channel still have a bit of subscriber.\nLink : https://m.youtube.com/channel/UC3GFQ0R21D7XYlN6tonrQIQ")
    if usr_input == "exit":
        print("Exiting program......")
        break
