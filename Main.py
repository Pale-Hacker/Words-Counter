import os

# --- #


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Banner():
    Clear()
    print("""__          __           _                     _____                  _            
\ \        / /          | |                   / ____|                | |           
 \ \  /\  / /__  _ __ __| |___     ______    | |     ___  _   _ _ __ | |_ ___ _ __ 
  \ \/  \/ / _ \| '__/ _` / __|   |______|   | |    / _ \| | | | '_ \| __/ _ \ '__|
   \  /\  / (_) | | | (_| \__ \              | |___| (_) | |_| | | | | ||  __/ |   
    \/  \/ \___/|_|  \__,_|___/               \_____\___/ \__,_|_| |_|\__\___|_|   
                                                                                   
                                                                                   \nCreated By : Pale-Hacker\n""")

# --- #


Banner()

Text = input("Enter Text : ")

Words_Count = len(Text.split())
Letters_Count = sum(len(word) for word in Text.split())
Spaces_Count = Text.count(' ')

# --- #

Banner()

print("Number of Words :", Words_Count)
print("Number of Letters :", Letters_Count)
print("Number of Spaces :", Spaces_Count)

# --- #

input("\n\nPress \"Enter\" To Exit ! ")

# --- #
