import string
import random

print("Please Enter Your String")
Usr_Str = input("Str: ")

Usr_List = Usr_Str.split()
Letters = list(string.ascii_letters)
Out_List = []
Temp_Str = []

def LetterOffset(Letter: str, OffsetAmt: int):
    return (Letters)[(Letters.index(Letter)) + OffsetAmt]

for a in range(len(Usr_List)): #Loops Every Word
    
    for b in range(len((Usr_List)[a])): #Every Word
        Temp_Str += LetterOffset(Letter = (Usr_List[a])[b], OffsetAmt = b)
    
    Out_List.append(Temp_Str)
    Temp_Str = ""

print(Out_List)