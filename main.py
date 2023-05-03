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
print("1--QuantumTool")
print("2--Mad Libs")
print("3--Random Fact")
print("4--Friend")
print("5--Guessing Game")
print("6--Pig Latin Translater")
print("7--Donut")
print("8--Encoder")
print("9--Decoder")
print()
print("10--Exit")
userinput = int(input("What Game Would You Like To Play(Number)"))
if userinput == 1:
    call(["python3", "Games/QuantumTool.py"])
elif userinput == 2:
    call(["python3", "Games/MadLibs.py"])
elif userinput == 3:
    call(["python3", "Games/RandomFact.py"])
elif userinput == 4:
    call(["python3", "Games/Friend.py"])
elif userinput == 5:
    call(["python3", "Games/GuessingGame.py"])
elif userinput == 6:
    call(["python3", "Games/PigLatinTranslater.py"])
elif userinput == 7:
    call(["python3", "Games/Donut.py"])
elif userinput == 8:
    call(["python3", "Games/Encoder.py"])
elif userinput == 9:
    call(["python3", "Games/Decoderr.py"])
elif userinput == 10:
    print("Exiting, Thanks For Playing")
