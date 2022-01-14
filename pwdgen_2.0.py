import string
import random
from time import sleep



def menu_combination():
    print("1.Letters only (Uppercase, Lowercase and punctuation)")
    print("2.Digits only")
    print("3.Letters (Uppercase, Lowercase and punctuation) and Digits")
    print("4.About...")



def splash_screen():

    print("______ _    _______ _____  _____ _   _ \n"
    "| ___ \ |  | |  _  \  __ \|  ___| \ | |\n"
    "| |_/ / |  | | | | | |  \/| |__ |  \| |\n"
    "|  __/| |/\| | | | | | __ |  __|| . ` |\n"
    "| |   \  /\  / |/ /| |_\ \| |___| |\  |\n"
    "\_|    \/  \/|___/  \____/\____/\_| \_/\n")
                                        
                                        


    print("Welcome to PWDGEN\n")
    sleep(1)
    print("This program gives you strong password for your accounts\nBy using uppercase, lowercase, digits, punctuation, hexdigits and octdigits in "
        "the password")
    sleep(2)
    print("========================================================\n")
    print("Use CTRL + C to terminate\n")
    sleep(1)

splash_screen()


def main_code():
    menu_combination()
    user_input = int(input("Enter input : "))
    if user_input == 1:                     #Letter only
        def menu_1():
            user_length = int(input("Enter password length limit (Max 64) : "))
            def randomLetters(stringLength=user_length):
                letters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
                return ''.join(random.choice(letters) for i in range(stringLength))
            if user_length > 64:
                print("Length reached max limit! please lower the length...")
                sleep(2)
                menu_1()
            else:
                print("\n", randomLetters(), "\n")
                menu_1()
        menu_1()

    elif user_input == 2:                   #Digits only
        def menu_2():
            user_length = int(input("Enter password length limit (Max 64) : "))
            def randomDigits(stringLength=user_length):
                digit = string.digits
                return ''.join(random.choice(digit) for i in range(stringLength))
            if user_length > 64:
                print("Length reached max limit! please lower the length...")
                sleep(2)
                menu_2()
            else:
                print("\n", randomDigits(), "\n")
                menu_2()
        menu_2()

    elif user_input == 3:                   #Mixed
        def menu_3():
            user_length = int(input("Enter password length limit (Max 64) : "))
            def randomString(stringLength=user_length):
                letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
                return ''.join(random.choice(letters) for i in range(stringLength))
            if user_length > 64:
                print("Length reached max limit! please lower the length...")
                sleep(2)
                menu_3()
            else:
                print("\n", randomString(), "\n")
                menu_3()
        menu_3()

    elif user_input == 4:                   #About, what else do you expect?
        def info():
            print("\nThis program is made by Linkachus17 using Python3. This program is a revision of the older version of this program called Random WiFi Password Generator\n"
            "This program is open source, so you can freely change something on the code and contribute to me on Github. although there's better program than this so I don't force to contribute\n"
            "What's new on this revision? Basically just making the code much better, nothing is new here unless I decide to use GUI on this program instead of consolde based\n"
            "Anyway I used this number to show the info because I got no idea how am I going to like detect if the user input is integer nor string so..."
            "Here's your generated password anyway, and thanks for using this program~\n")
        info()
        sleep(2)
        main_code()

    else:
        print("There is only 4 options :)\n")
        sleep(1)
        main_code()

main_code()
