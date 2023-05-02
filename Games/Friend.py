#NOT MINE
#from https://www.geeksforgeeks.org/python-create-simple-animation-for-console-based-application/

import subprocess
import time
import sys
import os
  
def load_animation():
  
    load_str = "waiting for friend..."
    ls_len = len(load_str)
 
    animation = "|/-\\"
    anicount = 0
      
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 10):
          
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
    
print("ERROR: 404: friend not found")

time.sleep(2)
if input("Would you like to restart. [Y,N]: ") == "Y":
    subprocess.call(["python3", "../main.py"])
else:
    print("Have a good day! PS: I will be your friend! :)")