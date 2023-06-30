from subprocess import call

import time, sys, os
  
def load_animation():
  
    load_str = "starting your console application..."
    ls_len = len(load_str)
 
    animation = "|/-\\"
    anicount = 0 # Animation Count
      
    counttime = 0 # Timer - how long animation been running 
      
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

GameDick = {
    {
        "Name": "Exit",
        "Id": "1",
        "File": "Games/Exit.py"
    },
    {
        "Name": "QuantumTool",
        "Id": "2",
        "File": "Games/QuantumTool.py"
    },
    {
        "Name": "Mad Libs",
        "Id": "3",
        "File": "Games/MadLibs.py"
    },
    {
        "Name": "Random Fact",
        "Id": "4",
        "File": "Games/RandomFact.py"
    },
    {
        "Name": "Friend",
        "Id": "5",
        "File": "Games/Friend.py"
    },
    {
        "Name": "Guessing Game",
        "Id": "6",
        "File": "Games/GuessingGame.py"
    },
    {
        "Name": "Pig Latin Translater",
        "Id": "7",
        "File": "Games/PigLatinTranslater.py"
    },
    {
        "Name": "Donut",
        "Id": "8",
        "File": "Games/Donut.py"
    },
    {
        "Name": "Encoder",
        "Id": "9",
        "File": "Games/Encoder.py"
    },
    {
        "Name": "Decoder",
        "Id": "10",
        "File": "Games/Decoder.py"
    },
    {
        "Name": "History",
        "Id": "11",
        "File": "Games/History.py"
    },
    {
        "Name": "French Classroom",
        "Id": "12",
        "File": "Games/IRFrench.py"
    },
    {
        "Name": "Quad Problem Solver",
        "Id": "13",
        "File": "Games/QuadProblemSolver.py"
    },
    {
        "Name": "File Creator and Editor",
        "Id": "14",
        "File": "Games/FunThing.py"
    }
}

print('Welcome To A Ton Of Games')
print("Game Options\n")

for i in GameDick:
    print(i["Id"] + "--" + i["Name"])
    
print("\n")
UserInput = int(input("What Game Would You Like To Play(Number): "))

for i in GameDick:
    if UserInput == i["Id"]:
        call(["python3", ["File"]])
    else:
        print("Not 100% Sure Thats An Option")
