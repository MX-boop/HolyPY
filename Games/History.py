import sys
import os
import time

Running = True

def clear():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

def PrintXY(Xcrd: int, Ycrd: int):
    for a in range(10):
        for b in range(20):
            if Xcrd == b and Ycrd == a:
                print("\033[33m#\033[0m", end="")
            else:
                print(" ", end="")
        print()

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
    e War of currents, a battle between AC (Alternating Current) and DC (Direct Current)
    """)

    print()
    print("""
    <--Nikola Tesla                                                   War Of Currents-->""")

Pointer = True

def MessageSel():
    if Pointer:
        clear()
        print(LightBlubOnn)
        print("""
        Nikola Tesla was a Serbian-American inventer who is most well known for his con
        tribution to eletrical engineering in the late 1800's. Many of his inventions w
        ere featured at the World's Fair in Chicago. One of Tesla's most well know inve
        ntions is the Tesla Coil. The coil was used for creating high voltage but low c
        urrent electricity. The coil was essential in the development of wireless trans
        mitters. Technology that was pioneered by the Tesla coil is still widely used i
        n many long-range radio transmiters today.
        """)
        time.sleep(10)

    else:
        clear()
        print(LightBlubOnn)
        print("""
        The War of Currents was a battle between AC and DC that occurred in the mid to l
        ate 1800's. The two main combatants in the fight were Thomas Edison(DC) and Geor
        ge Westinghouse. Thomas was a american inventer who was the founder of the Ediso
        n Illuminating Company. The company was aimed at competing with the market domma
        nt gas lamps by creating less expensive DC lamps. The Westinghouse Electric Comp
        any was founded by George Westinghouse in 1884 and focused on using AC technolog
        ies to provide eletricity to a large amount of households and businesses. the tw
        o companys fought for space in the new eletricity market. Before the 1893 fair t
        here was a feirce compition to power the lights for the events which was eventua
        ly won by AC. After Edison left his company the world started to see the winding
        down of the War of Currents with AC as its victor. We can still see the products
        of the battle today as AC is used to almost every type of eletric application.
        """)
        time.sleep(10)

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

    user_input = input("Enter C To View Citations, Enter 'E' to Select: ")

    if user_input == "E": #If The User Enters E The loop ends -> moves to selected option
        MessageSel()
    elif user_input == "C":
        print("""
        "Alternating Current." World of Invention, Gale, 2006. Gale in Context: Middle 
        School, link.gale.com/apps/doc/CV1647500021/ 
        MSIC?u=mlin_m_brimaysch&sid=bookmark-MSIC&xid=afa8aebf. Accessed 9 May 
        2023
        
        "Tesla, Nikola." The Columbia Electronic Encyclopedia™, New York, NY, Columbia 
        University Press, 2023. Gale in Context: Middle School, link.gale.com/apps/ 
        doc/A69227246/MSIC?u=mlin_m_brimaysch&sid=bookmark-MSIC&xid=a3b3c363. 
        Accessed 11 May 2023.
        
        Therien, Tania. "The War of the Currents? In the 1880s, Two of the World's Most 
        Famous Inventors Went Head to Head in a Vicious Public Fight over 
        Electricity. the Prize Was the Chance to Light up the World." Ask, vol. 11, 
        no. 3, Mar. 2012, p. 14+. Gale in Context: Middle School, link.gale.com/ 
        apps/doc/A285436482/MSIC?u=mlin_m_brimaysch&sid=bookmark-MSIC&xid=1d8203f1. 
        Accessed 11 May 2023.
        """)

        time.sleep(10)

    else:
        Pointer = !(Pointer)
