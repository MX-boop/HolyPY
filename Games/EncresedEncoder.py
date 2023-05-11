import string
from math import pi

print("Please Enter Your String")
Usr_Str = "Hai" + input("Str: ") #dummy wrd

Usr_List = Usr_Str.split()
Letters = list(string.ascii_letters)
Out_List = []
Temp_Str = []

def LetterOffset(Letter: str, OffsetAmt: int):
    return (Letters)[(Letters.index(Letter)) + OffsetAmt]

for a in range(len(Usr_List)): #Loops Every Word
    
    for b in range(len((Usr_List)[a])): #Every Letter

        Temp_Str += LetterOffset(Letter = (Usr_List[a])[b], OffsetAmt = int(pi[b+2]))
    
    Out_List.append(Temp_Str)
    Temp_Str = ""

for i in range(len(Out_List)-1):
    print(Out_List[i+1] + " ", end = "")