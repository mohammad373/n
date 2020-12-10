# n

import os
import sys
import requests
import time
from colorama import Fore

os.system("clear")
my_list = []
print(Fore.GREEN + "Hello . i`m H - NWWB ;)  . If Your Enter The exit While Is Bread ;) ")
while True:
    q = input(Fore.GREEN + "Enter Your List ==> ")
    my_list.append(q)
    if q == "exit":
        break
    if q == "" or None :
        break
    
def __1__():
    time.sleep(2)
    os.system("clear")
    site = input(Fore.RED + "Pleass Enter Your Address Target ==>  ")
    if site == "" or None:
        time.sleep(2)
        print(Fore.RED + "Error : Your Target is None ;(")
        time.sleep(1)
        sys.exit()
    for i in my_list:
        target = "http://" + site + "/" + i
        r = requests.get(target)
        if r.status_code == 200:
            print(Fore.GREEN + target)
        else:
            print(Fore.RED + target)
__1__()
