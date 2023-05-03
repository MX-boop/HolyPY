
import string

def ListOffset(Amt: int):
    for i in range(len(Letters)):
        Offset_Index = (i + Amt) % len(Letters)
        Offset_List.append(Letters[Offset_Index])



print("Welcome To Decoder")
print("Please Enter Your Key List")
Key_List = (input()).split()

for i in range(len(Key_List)):
    Key_List[i] = int(Key_List[i])

print("Please Enter Your Encoded String")
Encoded_List = (input()).split()


Decoded_List = []
Letters = list(string.ascii_lowercase)
Offset_List = []
WordTemp = ''
Decoded_Final = ''

for i in range(len(Encoded_List)):
    ListOffset(Amt= -(Key_List[i]))
    for b in range(len(Encoded_List[i])):
        WordTemp = WordTemp + (Offset_List[Letters.index((Encoded_List[i])[b])])
    Offset_List = []
    Decoded_List.append(WordTemp)
    WordTemp = ''

for i in range(len(Decoded_List)):
    Decoded_Final += Decoded_List[i]

print(Decoded_Final)