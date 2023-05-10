import sys
import os
import time

Running = True

def clear():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

def PrintList(coords: list):
    for a in range(10):
        for b in range(20):
            if (f"{b}, {a}") in coords:
                print("\033[33m#\033[0m", end="")
            else:
                print(" ", end = "")
        print()

SlopeCoords = []
Ycoord = ""

def PrintSlope(slope: int):
    for i in range(10):
        Ycoord = slope*i
        SlopeCoords.append(f"{i}, {Ycoord}")
        Ycoord = ""
    PrintList(coords = SlopeCoords)

LightBlubOff = f"""
           ______
       .-~~^^^^^^~~-.
     .'              '.
    '                  '
   ;                    ;
   |                    |
   |                    |
   ;                    ;
    \                  /
     '._           _.'
        '▄▄▄▄▄▄▄▄▄'
         :▒▒▒▒▒▒▒:
         :▀║▀▀▀║▀:
           ╚╦═╦╝
"""

LightBlubOnn = f"""
           \033[33m______
       .-~~^^^^^^~~-.
     .'##############'.
    '##################'
   ;####################;
   |####################|
   |####################|
   ;####################;
    \##################/
     '._###########_.'\033[0m
        '▄▄▄▄▄▄▄▄▄'
         :▒▒▒▒▒▒▒:
         :▀║▀▀▀║▀:
           ╚╦═╦╝
"""
Coords =[]

for i in range(0, 10):
    Coords.append(f"12, {10 - i}")
    Coords.append(f"14, {10 - i}")
    clear()
    print(LightBlubOff)
    PrintList(coords = Coords)
    time.sleep(0.5)

clear()

def Message1():
    print(LightBlubOnn)

    print("""
    On the first of May, 1893 the World's Columbian Exposition was opened to the public.
    The at its peak, the fair had over 700,000 visiters on a single day. Opon many other
    expositions at the event, it was one of the first public showings of the use of elec
    tricity in a house-hold setting. The event featured many interiors equiped with edis
    ion bulbs to illuminate the fair. One of the major expositions included a AC inducti
    on motor invented by Nikola Tesla. The World's Fair took place at the tail end of th
    e War of currants, a battle between AC (Alternating Current) and DC (Direct Current)
    """)

    print()
    print("""
    <--Nikola Tesla                                                   War Of Currents-->
    """)

Pointer = True

while Running == True:
    clear()
    Message1()
    if Pointer:
        print("    ", end = "")
        for i in range(15):
            print("\033[036m#\033[0m", end = "")
    else:
        for i in range(70):
            print(" ", end = "")
        for i in range(18):
            print(f"\033[036m#\033[0m", end = "")
    
    print()

    user_input = input("Enter 'E' to end the loop: ")

    if user_input == "E": #If The User Enters E The loop ends -> moves to selected option
        break
    else:
        if Pointer: # Else Toggles Pointer
            Pointer = False
        else:
            Pointer = True

clear()

if Pointer:
    print("""
    #thing abt nic tesla
    """)
    PrintSlope(slope = 2)
else:
    print("""
    #thing abt war of currents
    """)
    PrintSlope(slope = 0.5)

FinalCoords = [(5, 5)]

while Running:
    UsrXcrd = int(FinalCoords[0])[1]
    UsrYcrd = int(FinalCoords[0])[4]
    PrintList(coords = FinalCoords)
    FinalCoords = []
    print()
    print("WSAD")
    UsrControl = input

    if UsrControl == "w": #Changes Usr Cords For WSAD input
        UsrYcrd += -1
    elif UsrControl == "s":
        UsrYcrd += 1
    elif UsrControl == "d":
        UsrXcrd += 1
    elif UsrControl == "a":
        UsrXcrd += -1

    FinalCoords.append(f"{UsrXcrd}, {UsrYcrd}")
    clear()