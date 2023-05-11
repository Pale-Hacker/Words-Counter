import os
import pyshorteners

# --- #

s = pyshorteners.Shortener()

# --- #


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Banner():
    Clear()
    print(""" _    _ _____  _                    _____ _                _                       
| |  | |  __ \| |                  / ____| |              | |                      
| |  | | |__) | |        ______   | (___ | |__   ___  _ __| |_ ___ _ __   ___ _ __ 
| |  | |  _  /| |       |______|   \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
| |__| | | \ \| |____              ____) | | | | (_) | |  | ||  __/ | | |  __/ |   
 \____/|_|  \_\______|            |_____/|_| |_|\___/|_|   \__\___|_| |_|\___|_|   
                                                                                   
Created By : Pale-Hacker\n""")

# --- #


Banner()
E_URL = input("Enter URL : ")

# --- #

try:
    Banner()

    print("Old URL :", E_URL)
    print("\nNew URL :", s.tinyurl.short(E_URL))
except:
    print("Error !")
    exit()

# --- #

input("\n\nPress \"Enter\" To Exit ! ")

# --- #
