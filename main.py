#                                                                               I N S T A  D O W N L O A D E R
# This tool allow you to download all media from an instagram account 
# Coded by Zenek (https://github.com/Zenek-Hastro)
# Version 1.2b (first build version 1.0b)

# ============================================================================================================================================================================= #
"""                                                                                 
                                                                                        REQUIREMENTS
 -Python (version 3.5 or >)
 -PIP3 
 -Instaloader
 -Colorama
""" 
# ============================================================================================================================================================================= #
""" 
                                                                                          GUIDE
 -Install   Python:        https://www.python.org/downloads/
 -Install   pip3:          https://pip.pypa.io/en/stable/installing/
 -Instal    Instaloader:   https://instaloader.github.io/installation.html
 -Install   Colorama:      https://pypi.org/project/colorama/
""" 
# ============================================================================================================================================================================= #
# ============================================================================================================================================================================= #
# ============================================================================================================================================================================= #
# Program Library                                                                                                                                                               #
import os                                                                                                                                                                       #
import time                                                                                                                                                                     #
from colorama import Fore, Style                                                                                                                                                #
from pathlib import Path                                                                                                                                                        #
# ============================================================================================================================================================================= #
# Definition & Declaration                                                                                                                                                      #
def clear(): os.system('cls') #Clear Console                                                                                                                                    #
def start(): os.system('start') #Open Console                                                                                                                                   #
                                                                                                                                                                                #
# ============================================================================================================================================================================= #
#                                                                                                                                                                               #
#                                                                       M A I N  -  F U N C T I O N                                                                             #
#                                                                                                                                                                               #
# ############################################################################################################################################################################# #

# Login System
clear()
user_login_status = 0  # check the log-in status
list_of_lists = [] # check users

IGlogin = input('Would you like login on instagram (y/n)? ').lower()

if (os.path.isfile("users.zk") and IGlogin.startswith('y')):
    LoadSession = input('We have found a session already opened! Would you like load it (y/n)?').lower()
    if LoadSession.startswith('y'):
        clear()
        f = open("users.zk", "r")
        account = f.read()
        user_login_status = 1
        os.system(f"instaloader --login {account}")
        
if (IGlogin.startswith('y') and user_login_status == 0):
    clear()
    account = input('Enter your instagram account> ')
    user_login_status = 1
    os.system(f"instaloader --login {account}")
    # Save currently session (only nickname, NO PASSWORD!)
    file_object = open("users.zk", "w")
    file_object.write(account)
    file_object.close

elif IGlogin.startswith('n'):
    clear()
    user_login_status = 0
    print(Fore.RED+"\t !!IF YOU DOESN'T LOGIN, YOU COULD NOT DOWNLOAD STORIES, HIGHLIGHTS AND PRIVATE ACCOUNT !!\n\n")

# ############################################################################################################################################################################# #

# Check For Updates 
users_update = input('Would you like check profiles updates from collected account (y/n)? ').lower()

if (users_update.startswith('y')):
    with open('account.zk', 'r') as f:
        account_list = [line.strip() for line in f]

    # Get list lenght
    length = len(account_list) 
    
    # Iterate in to the list 
    for i in range(length): 
        os.system(f"instaloader --fast-update --login={account} {account_list[i]}")

        # Clear Metadata 
        for root, dirs, files in os.walk(account_list[i]):
            for file in files:
                if file.endswith(".txt") or file.endswith(".xz"):
                    #print(os.path.join(root, file)) No need to print all files deleted. Uncomment for check it !
                    os.remove(os.path.join(root, file)) 

        print("\n\nUpdated: " +account_list[i]+ "\n")
        time.sleep(3) 

# ############################################################################################################################################################################# #

# Start Downloading System
clear()
name = input(Fore.WHITE+"Enter Profile Name To Download: ")

# Save Account (used for check the updates!)
with open('account.zk', 'r') as f:
    account_list = [line.strip() for line in f]

if(name in account_list):
  f.close
  print("\nALREADY ON THIS LIST!\n")
  time.sleep(5)
else:
    f.close
    file_object = open("account.zk", "a")
    file_object.write(name + "\n")
    file_object.close
    print("\nAdded " +name+" to account.zk!\n")


if (user_login_status == 0):
    os.system(f"instaloader {name} ") # CALL WITHOUT LOGIN (NO PARAMETERS, ONLY MAIN PICTURES PROFILE)

elif (user_login_status == 1):

    os.system(f"instaloader --stories --highlights --tagged --igtv --login={account} {name}") # MAIN CALL WITH ALL PARAMETERS

else:
    print("CRITICAL ERROR")
    exit()

# ############################################################################################################################################################################# #
# Clear Console & Metadata
print("\n\nClearing Metadata & Information...\n")
time.sleep(3)


# Remove unnecessary files
for root, dirs, files in os.walk(name):
    for file in files:
        if file.endswith(".txt") or file.endswith(".xz"):
            #print(os.path.join(root, file)) No need to print all files deleted. Uncomment for check it !
            os.remove(os.path.join(root, file)) 

# ############################################################################################################################################################################# #

# Opening Downloaded Folder
path = name
path = os.path.realpath(path)
os.startfile(path)
# ==============================================================================================================================================================================#
