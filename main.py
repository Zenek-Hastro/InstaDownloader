# This tool allow you to download all media from an instagram account 
# Coded by Zenek (https://github.com/Zenek-Hastro)
# Version 1.0b (first build version 1.0b)

# ===============================================================================================================================================================================
""" 
REQUIREMENTS
 -Python (version 3.5 or >)
 -PIP3 
 -Instaloader
 -Colorama
""" 
# ===============================================================================================================================================================================
""" 
GUIDE
 -Install   Python:        https://www.python.org/downloads/
 -Install   pip3:          https://pip.pypa.io/en/stable/installing/
 -Instal    Instaloader:   https://instaloader.github.io/installation.html
 -Install   Colorama:      https://pypi.org/project/colorama/
""" 
# ===============================================================================================================================================================================
# ===============================================================================================================================================================================
# ===============================================================================================================================================================================

# Program Library
import os
import time
import colorama
from colorama import Fore, Style
from pathlib import Path
from os import path

# ===============================================================================================================================================================================

# Definition & Declaration
def clear(): os.system('cls') #Clear Console
def start(): os.system('start') #Open Console

# ===============================================================================================================================================================================

# Login System
clear()
IGlogin = input('Would you like login on instagram (y/n)? ').lower()
if IGlogin.startswith('y'):
    clear()
    account = input('Enter your instagram account> ')
    os.system(f"instaloader --login {account}")
elif IGlogin.startswith('n'):
    clear()
    print(Fore.RED+"\t!IF YOU DOESN'T LOGIN, YOU COULD NOT DOWNLOAD ANY PRIVATE ACCOUNTS!\n\n")
else:
    clear()
    print("\n\nERROR: YOU MUST TYPE (y)/(n)!\n\n")
    exit()
    

# Start Downloading System
name = input(Fore.WHITE+"Enter Profile Name To Download: ")
os.system(f"instaloader {name}")


# Clear Console 
print("\n\nClearing Metadata & Information...\n")
#time.sleep(5)


# Clear Metadata
mydir = Path("""""", name)
filelist = [f for f in os.listdir(mydir) if f.endswith(".txt") or f.endswith(".xz")]
for f in filelist:
    os.remove(os.path.join(mydir, f))


# Opening Downloaded Folder
path = name
path = os.path.realpath(path)
os.startfile(path)
# ===============================================================================================================================================================================
