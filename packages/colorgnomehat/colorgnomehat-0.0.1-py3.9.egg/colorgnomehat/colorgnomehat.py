#hello I'm Rigved, I'm ten years old, you might be wondering what this code is well it is used to add color in variables and other stuff. 
#so while this if you see the word 'None' please ignore it


from colorama import Fore, Back, Style
from colorama.initialise import init

init()

def red(r, var):
    red = Fore.RED + var
    print(red)

def green(r, var):
    green = Fore.GREEN + var
    print(green)

def yellow(r, var):
    yellow = Fore.YELLOW + var
    print(yellow)

def black(r, var):
    black = Fore.BLACK + var
    print(black)

def blue(r, var):
    blue = Fore.BLUE + var
    print(blue)

def cyan(r, var):
    cyan = Fore.CYAN + var
    print(cyan)

