import time
import subprocess

print("Welcome To Pig Latin Translater")
print("Please enter the sentances you would like to translate")
UserInput = input("(Words)")
FinOutput = ""

Word_List = UserInput.split()

Vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]

for i in range(len(Word_List)):
    while not any(item in (Word_List[i])[0] for item in Vowels):
        Word_List[i] = Word_List[i][len(Word_List[i]) - (len(Word_List[i])-1):]
    
    Word_List[i] = (Word_List[i]+"ay")
    FinOutput = FinOutput + Word_List[i]+" "
print(FinOutput)

time.sleep(2)
if input("Would you like to restart. [Y,N]: ") == "Y":
    subprocess.call(["python3", "../main.py"])