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

BA = ("""

╔══════╗  ╔════════╗      ╔═╗
╚════╗ ║  ║ ╔════╗ ║     ╔  ║
    ╔╝╔╝  ║ ║ ╔╗ ║ ║   ╔═╝  ║
   ╔╝╔╝   ╚╗  ╔╗  ╔╝   ╚═╝  ║  
  ╔╝╔╝     ╚═╗  ╔═╝         ╚═╗
  ╚═╝        ╚══╝     ╚══════╝\n""")
print("Discrd Rich Presence By:\n"); print(f"{Fore.BLUE}{BA}{Fore.RESET}")
appId = config.appId 
richPresence = pre(appId) 
richPresence.connect()

# <!------ Config ------ >
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

# Looping time sleep so the script keep on running.
while 1:
    time.sleep(1)

# <!-- Null -->
