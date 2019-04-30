import os
import time
from random import randint
from colorama import init, Fore, Back, Style

init(convert=True)

os.system("music_Workers.bat")

for i in range(1,45):
    print('')

red = Fore.RED + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT

def addSpaces(a):
    while a > 0:
        print(' ', end='')
        a -= 1
def newLineWithSleep():
    time.sleep(0.3)
    print('\n', end='')

def spanners():
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,263):
        if i in (23,47,71,95,119,143,167,191,215,239,263):
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in (1,52,69,193,210,244):
            print(red + '/', end='')
        elif i in (21,49,66,196,213,258):
            print(green + '\\', end='')
        elif i in (50,51,67,68,194,195,211,212):
            print(green + '=', end='')
        elif i in (24,25,29,41,45,46,74,75,87,88,98,99,115,
                           116,122,123,133,134,146,147,163,164,170,
                                   171,185,186,216,220,221,233,234,238):
            print(green + '|', end='')
        elif i == 81:
            print(cyan + 'HAPPY', end='')
        elif i == 128:
            print(yellow + 'WORKERS', end='')
        elif i == 178:
            print(magenta + 'DAY', end='')
        else:
            print(' ', end='')

def hammer():
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,347):
        if i in (28,57,86,115,144,173,202,231,260,289,318,347):
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in range(8,20) or i in range(95,107):
            print(red + '_', end='')
        elif i in range(273,277):
            print(red + '#', end='')
        elif i in (36,49,65,74,94,107,129,130,158,159,187,188,216,217,245,246):
            print(green + '|', end='')
        elif i == 70:
            print(cyan + 'HAPPY', end='')
        elif i == 196:
            print(yellow + 'WORKERS', end='')
        elif i == 319:
            print(magenta + 'DAY', end='')
        else:
            print(' ', end='')

def broom1():
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,63):
        if i in (7,15,23,31,39,47,55,63):
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in (49,50,52,53):
            print(red + '_', end='')
        elif i in (3,11,19,27,35,43,51) or i in range(56,63):
            print(green + '|', end='')
        else:
            print(' ', end='')

def broom2():
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,55):
        if i in (6,13,20,27,34,41,48,55):
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in (36,39):
            print(red + '_', end='')
        elif i in (42,43):
            print(red + '/', end='')
        elif i in (46,47):
            print(red + '\\', end='')
        elif i in (2,3,9,10,16,17,23,24,30,31,37,38,44,45) or i in range(49,55):
            print(green + '|', end='')
        else:
            print(' ', end='')


def crossWheel():
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,71):
        if i in (11,23,35,47,59,71):
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in (5,25,26,27,31,32,33,37,38,39,43,44,45,65):
            print(red + '_', end='')
        elif i in (16,18,28,30,36,46,52,54,64,66):
            print(green + '|', end='')
        elif i == 41:
            print(green + 'o', end='')
        else:
            print(' ', end='')


def shovel():
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,80):
        if i in (8,17,26,35,44,53,62,71,80):
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in (46,47,50,51,74,75,76,77):
            print(red + '_', end='')
        elif i in (3,4,12,13,21,22,30,31,39,40,48,49,54,61,63,70):
            print(green + '|', end='')
        elif i == 73:
            print(green + '\\', end='')
        elif i == 78:
            print(green + '/', end='')
        else:
            print(' ', end='')

def programmer():
    Left_Spaces = randint(8, 80)
    addSpaces(Left_Spaces)
    for i in range(0,249):
        if i in (24,49,74,99,124,149,174,199,224,249):
            newLineWithSleep()
            addSpaces(Left_Spaces)
        elif i in range(1,21) or i in range(101,121) or i in range(153,160) or i in range(161,168):
            print(red + '_', end='')
        elif i in (178,180,182,184,186,188,190,192,203,205,207,209,
                              211,213,215,217,228,230,232,234,236,238,240,242):
            print(green + '_', end='')
        elif i in (25,37,50,70,75,93,100,121,135,160,177,179,181,
                           183,185,187,189,191,193,202,204,206,208,210,212,
                                   214,216,218,222,227,229,231,233,235,237,239,241,243):
            print(green + '|', end='')
        elif i in (223,246):
            print(green + '\\', end='')
        elif i in (221,248):
            print(green + '/', end='')
        elif i == 32:
            print(cyan + 'Programmer', end='')
        elif i == 53:
            print(yellow + 'No', end='')
        elif i == 85:
            print(magenta + 'Life', end='')
        else:
            print(' ', end='')

while 1:
    spanners()
    newLineWithSleep()
    newLineWithSleep()
    newLineWithSleep()
    hammer()
    newLineWithSleep()
    newLineWithSleep()
    newLineWithSleep()
    broom1()
    newLineWithSleep()
    newLineWithSleep()
    newLineWithSleep()
    broom2()
    newLineWithSleep()
    newLineWithSleep()
    newLineWithSleep()
    crossWheel()
    newLineWithSleep()
    newLineWithSleep()
    newLineWithSleep()
    shovel()
    newLineWithSleep()
    newLineWithSleep()
    newLineWithSleep()
    programmer()
    newLineWithSleep()
    newLineWithSleep()
    newLineWithSleep()

    print('\n', end='') # By Mohammad Hashem
