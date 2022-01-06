import string
import random
from time import sleep



print("______ _    _______ _____  _____ _   _ \n"
"| ___ \ |  | |  _  \  __ \|  ___| \ | |\n"
"| |_/ / |  | | | | | |  \/| |__ |  \| |\n"
"|  __/| |/\| | | | | | __ |  __|| . ` |\n"
"| |   \  /\  / |/ /| |_\ \| |___| |\  |\n"
"\_|    \/  \/|___/  \____/\____/\_| \_/\n")
                                       
                                       


print("Welcome to PWDGEN\n")
sleep(3)
print("This program gives you strong password for your accounts\nBy using uppercase, lowercase, digits, punctuation, hexdigits and octdigits in "
    "the password")
sleep(3)
print("========================================================\n")
print("Use '914615' as input to show the info\nUse CTRL + C to terminate")
sleep(1)


def info():
    print("This program is made by Linkachus17 using Python3. This program is a revision of the older version of this program called Random WiFi Password Generator\n"
    "This program is open source, so you can freely change something on the code and contribute to me on Github. although there's better program than this so I don't force to contribute\n"
    "What's new on this revision? Basically just making the code much better, nothing is new here unless I decide to use GUI on this program instead of consolde based\n"
    "Anyway I used this number to show the info because I got no idea how am I going to like detect if the user input is integer nor string so..."
    "Here's your generated password anyway, and thanks for using this program~\n")


while True:

    usr_input = int(input("Enter the length of password (No limit): "))

    def randomString(stringLength=usr_input):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.hexdigits + string.octdigits
        return ''.join(random.choice(letters) for i in range(stringLength))
    
    if usr_input == 914615:
        info()
        sleep(10)
        print(randomString())
        sleep(1)
        print("\n\n")

    print(randomString())
    sleep(1)
    print("\n\n")

