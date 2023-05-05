print("Does Not Work")
import string

def ListOffset(Amt: int, Offset_List: list):
    Letters = list(string.ascii_lowercase)
    for i in range(len(Letters)):
        Offset_Index = (i + Amt) % len(Letters)
        Offset_List.append(Letters[Offset_Index])

def CeaserDecrypter(Key: int, Encrypted_Word: str):
    Offset_List = []
    Decrypted_Word = ''
    ListOffset(Amt=Key, Offset_List=Offset_List)
    for b in range(len(Encrypted_Word)):
        Decrypted_Word += string.ascii_lowercase[Offset_List.index(Encrypted_Word[b])]
    return Decrypted_Word

def Decrypter(Encoded: list, Key_List: list):
    Decoded = []
    for i in range(len(Encoded)):
        Key = Key_List[-i-1] # reverse order of keys
        Decoded_Word = CeaserDecrypter(Key=Key, Encrypted_Word=Encoded[i][::-1]) # reverse order of words
        Decoded.append(Decoded_Word)
    return ' '.join(Decoded[::-1]) # reverse order of final message

Keys1 = input("Enter Your First Key List").split