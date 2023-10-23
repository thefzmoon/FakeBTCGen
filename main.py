import time
import random
import string
import os
from colorama import init, Fore
init(convert=True)


wallet = input(Fore.WHITE + "Enter your btc wallet address: ")

x = 8

print ("...")
time.sleep (0.7)
print ("...")
time.sleep (0.7)
print ("...")
time.sleep (0.7)
print ("...")
time.sleep (0.7)

print (Fore.WHITE + "Starting...")

tries = 0

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

while(True):
    if tries <= random.randint(5000, 10000):
        print(Fore.CYAN + "[-]" + Fore.RED + " bc1" + id_gen() + Fore.CYAN + " | Invalid |  " + "0.0000 BTC")
        tries += 1
    else:  # chance to get fake btc
        print(Fore.CYAN + "[-]" + Fore.GREEN + " bc1" + id_gen() + Fore.GREEN + " |  Valid  |  " + str(
            round(random.uniform(0, 2), 4)), "BTC")
        print(Fore.WHITE + "Withdrawing to the wallet " + wallet)
        time.sleep(10)
        tries = 0
        print(Fore.WHITE + "Done!")
        time.sleep(60)
