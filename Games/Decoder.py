import string



print("Welcome To Decoder")
print("Enter Message")
usermessage = input("(String): ")

MasterKey = int(input("Please Enter The Master Key"))
Word_List = usermessage.split()
Key_List = (input("Please Enter You Key List")).split()
Decoded = []
Letters = list(string.ascii_letters)

for i in range(len(Key_List)):
    Key_List[i] = int("-" + str(Key_List[i]))#I Know This Is Ugly

def ListOffset(Amt: int, Offset_List: list):
    for i in range(len(Letters)):
        Offset_Index = (i + Amt) % len(Letters)
        Offset_List.append(Letters[Offset_Index])

def CeaserCypher(Keys: list, Words: list, Output: list,):

    StartLenWords = len(Words)
    Temp = ""
    Temp2 = ""

    for i in range(StartLenWords): #Loops Through Every Word

        Offset_List = [] #Creates a dummy list for offsets

        ListOffset(Amt=Keys[i], Offset_List=Offset_List) #Creates a Offseted list for the word

        for b in range(len(Words[i])):
            Temp = Temp + Offset_List[Letters.index(Words[i][b])] #Loops Through Every Letter to ceaser Cypher

        Output.append(Temp) #Adds the word to the output
        Temp = '' #Resets the Temp

for i in range(MasterKey):

    TempList = []

    CeaserCypher(Keys=Key_List, Words=Word_List, Output=Decoded)

    Word_List = []

    for b in range(len(Decoded)):
        Word_List.append(Decoded[b]) #Sets Word List To Encoded

    Decoded = []

    for b in range(len(Word_List)):
        TempList.append(Word_List[b][::-1])

    Word_List = []

    for b in range(len(TempList)):
        Word_List.append(TempList[b])

Word_Final = ""

for i in range(len(Word_List)):
    Word_Final += Word_List[i] + " "

print(Word_Final)