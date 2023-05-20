from subprocess import call

import time
import sys
import os
  
def load_animation():
  
    load_str = "starting your console application..."
    ls_len = len(load_str)
 
    animation = "|/-\\"
    anicount = 0
      
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        time.sleep(0.075) 
                              
        
        load_str_list = list(load_str) 
          
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
  
if __name__ == '__main__': 
    load_animation()

print('Welcome To A Ton Of Games')
print("Game Options")
print()
print("1--Exit")
print()
print("2--QuantumTool")
print("3--Mad Libs")
print("4--Random Fact")
print("5--Friend")
print("6--Guessing Game")
print("7--Pig Latin Translater")
print("8--Donut")
print("9--Encoder")
print("10--Decoder")
print("11--History")
print("12--French Classroom")
print("13--Quad Problem Solver")
print("14--File Creator and Editor")
print()
print()
userinput = int(input("What Game Would You Like To Play(Number): "))
if userinput == 2:
    call(["python3", "Games/QuantumTool.py"])

elif userinput == 3:
    call(["python3", "Games/MadLibs.py"])

elif userinput == 4:
    call(["python3", "Games/RandomFact.py"])

elif userinput == 5:
    call(["python3", "Games/Friend.py"])

elif userinput == 6:
    call(["python3", "Games/GuessingGame.py"])

elif userinput == 7:
    call(["python3", "Games/PigLatinTranslater.py"])

elif userinput == 8:
    call(["python3", "Games/Donut.py"])

elif userinput == 9:
    call(["python3", "Games/Encoder.py"])

elif userinput == 10:
    call(["python3", "Games/Decoder.py"])

elif userinput == 11:
    call(["python3", "Games/History.py"])

elif userinput == 12:
    call(["python3", "Games/IRFrench.py"])

elif userinput == 13:
    call(["python3", "Games/QuadProblemSolver.py"])

elif userinput == 14:
    call(["python3", "Games/FunThing.py"])

elif userinput == 0:
    print("Okey, Sounds Good!")
    exit()

else:
    print("Not 100% Sure Thats An Option")