import random
import string

def ListOffset(Amt: int):
    for i in range(len(Letters)):
        Offset_Index = (i + Amt) % len(Letters)
        Offset_List.append(Letters[Offset_Index])



print("Welcome To Encoder")
print("Enter Message")
usermessage = input("(String)")

Word_List = usermessage.split()
Key_List = []
Encoded = []
Letters = list(string.ascii_lowercase)
Offset_List = []
WordTemp = ""
Word_Final = ""

for i in range(len(Word_List)):
    Key_List.append(random.randint(0, 26))
    ListOffset(Amt=Key_List[i])
    for b in range(len(Word_List[i])):
        WordTemp = WordTemp + (Offset_List[Letters.index((Word_List[i])[b])])
    Offset_List = []
    Encoded.append(WordTemp)
    WordTemp = ''

for i in range(len(Encoded)):
    Word_Final += Encoded[i]

print(Word_Final)
print(Key_List)
