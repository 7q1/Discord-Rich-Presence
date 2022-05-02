import os
import config
from config import *
try:
    import pypresence
except:
    os.system("pip install pypresence")
try:
    import colorama
except:
    os.system("pip install colorama")
from pypresence import Presence as pre
from colorama import *
import time
os.system("cls")
# HyperLink
def myLink(url, label=None):
    if label is None: 
        label = url
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, url, label)

BA = (F"""{Fore.CYAN}

╔══════╗  ╔════════╗      ╔═╗
╚════╗ ║  ║ ╔════╗ ║     ╔  ║
    ╔╝╔╝  ║ ║ ╔╗ ║ ║   ╔═╝  ║
   ╔╝╔╝   ╚╗  ╔╗  ╔╝   ╚═╝  ║  
  ╔╝╔╝     ╚═╗  ╔═╝         ╚═╗
  ╚═╝        ╚══╝     ╚══════╝{Fore.RESET}  {Fore.MAGENTA}{myLink("https://github.com/7q1", "GitHub.")}{Fore.RESET}\n""")

while 1:
    try:
        appId = config.appId
        richPresence = pre(appId) 
        richPresence.connect()
        os.system('cls||clear')
        print("Discrd Rich Presence By:\n"); print(BA)


        # <!------  Config ------ >
        details = config.details
        state = config.state
        large_image = config.large_image
        small_image = config.small_image
        large_text = config.large_text
        # <!------ /Config ------ >

        # Display .
        print(F'''
        [{Fore.YELLOW}>{Fore.RESET}] Details     {Fore.RED}->{Fore.RESET} [{details}]
        [{Fore.YELLOW}>{Fore.RESET}] State       {Fore.RED}->{Fore.RESET} [{state}]
        [{Fore.YELLOW}>{Fore.RESET}] Large_image {Fore.RED}->{Fore.RESET} [{large_image}]
        [{Fore.YELLOW}>{Fore.RESET}] Small_image {Fore.RED}->{Fore.RESET} [{small_image}]
        [{Fore.YELLOW}>{Fore.RESET}] Large_text  {Fore.RED}->{Fore.RESET} [{large_text}]
        ''')

        # Updating Rich Presence.
        richPresence.update(details=details,
                    state=state,
                    large_image=large_image,
                    small_image=small_image,
                    large_text=large_text,
                    start=time.time())

        print(F"\n[{Fore.GREEN}+{Fore.RESET}] Rich Presence Running.")
        time.sleep(9*900)
    except pypresence.exceptions.DiscordNotFound:
        print("[+] Waiting for client to connect to discord. ")
        time.sleep(3)
        os.system('cls||clear')

# Looping time sleep so the script keep on running.

# <!-- Null -->
