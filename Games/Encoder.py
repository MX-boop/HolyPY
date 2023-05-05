import random
import string

print("Welcome To Encoder")
print("Enter Message")
usermessage = input("(String)")

Word_List = usermessage.split()
Word_List2 = []
Key_List = []
Key_List2 = []
Encoded = []
Encoded2 = []
Letters = list(string.ascii_lowercase)

def ListOffset(Amt: int, Offset_List: list):
    for i in range(len(Letters)):
        Offset_Index = (i + Amt) % len(Letters)
        Offset_List.append(Letters[Offset_Index])

def CeaserCypher(Keys: list, Words: list, Output: list, Temp: str):
    for i in range(len(Words)):
        Keys.append(random.randint(0, 26))
        Offset_List = []
        ListOffset(Amt=Keys[i], Offset_List=Offset_List)
        for b in range(len(Words[i])):
            Temp = Temp + (Offset_List[Letters.index((Words[i])[b])])
        Output.append(Temp)
        Temp = ''

CeaserCypher(Keys=Key_List, Words=Word_List, Output=Encoded, Temp='')
for i in range(len(Encoded)):
    Word_List2.append((Encoded[i])[::-1])

CeaserCypher(Keys=Key_List2, Words=Word_List2, Output=Encoded2, Temp='')
Word_Final = " ".join(Encoded2)

print(Word_Final)
print(Key_List)
print(Key_List2)