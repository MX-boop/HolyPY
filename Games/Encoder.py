import random
import string

print("Use Enhanced Encryption? [Y,N]")
if input("[Y,N]") == "Y":
    print("Please Enter Agreed Opponent Base")
    Base = int(input("(Smaller Prime Number): "))
    print("Please Enter Agreed Opponent Larger Prime")
    Prime = int(input("(Larger Prime Number): "))
    print("Please Pick A Secret Number")
    BobsNum = int(input("(Integer): "))
    BigBob = (Base ** BobsNum) % Prime
    print("Please Exchange Numbers With The Person You Want To Talk To")
    print("Your Number: " + str(BigBob))
    print("Please Enter Your Contact's Number: ")
    AlicesNum = int(input("(Integer): "))
    MasterKey = (AlicesNum ** BobsNum) % Prime
else:
    print("Okay")
    MasterKey = 1

print("Welcome To Encoder")
print("Enter Message")
usermessage = input("(String): ")

Word_List = usermessage.split()
Key_List = []
Encoded = []
Letters = list(string.ascii_letters)

def ListOffset(Amt: int, Offset_List: list):
    for i in range(len(Letters)):
        Offset_Index = (i + Amt) % len(Letters)
        Offset_List.append(Letters[Offset_Index])

def CeaserCypher(Keys: list, Words: list, Output: list,):

    StartLenWords = len(Words)
    Temp = ""
    Temp2 = ""

    for i in range(StartLenWords): #Loops Through Every Word

        if len(Keys) < len(Words): #Adds to Keys if Needed
            Keys.append(random.randint(0, len(Letters)))

        Offset_List = [] #Creates a dummy list for offsets

        ListOffset(Amt=Keys[i], Offset_List=Offset_List) #Creates a Offseted list for the word

        for b in range(len(Words[i])):
            Temp = Temp + Offset_List[Letters.index(Words[i][b])] #Loops Through Every Letter to ceaser Cypher

        Output.append(Temp) #Adds the word to the output
        Temp = '' #Resets the Temp

for i in range(MasterKey):

    TempList = []

    CeaserCypher(Keys=Key_List, Words=Word_List, Output=Encoded)

    Word_List = []

    for b in range(len(Encoded)):
        Word_List.append(Encoded[b]) #Sets Word List To Encoded

    Encoded = []

    for b in range(len(Word_List)):
        TempList.append(Word_List[b][::-1])

    Word_List = []

    for b in range(len(TempList)):
        Word_List.append(TempList[b])

Word_Final = ""

for i in range(len(Word_List)):
    Word_Final += Word_List[i] + " "

print(Word_Final)
print(Key_List)