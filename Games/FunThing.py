import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

usrstring = ""
usrtemp = "enter command: "

def UsrString():
    global usrstring

    while True:
        clear()
        print("This is you editor")
        print("Type :help for help")
        print("Type :clear to clear the text")
        print()
        print(usrstring)
        usrtemp = input("")
        if usrtemp == "exit":
            exit()
        elif usrtemp == ":help":
            print("figure it out yourself")
        elif usrtemp == ":clear":
            usrstring = ""
        elif usrtemp == ":cls":
            exit()
        elif usrtemp == ":nl":
            usrstring += "\n"
        elif usrtemp == ":enter":
            return usrstring
        else:
            usrstring += usrtemp

        usrtemp = ""

print("What is the name of the file you want to create?")
filename = input("")
print("What is the file extension?")
fileext = input("")

file = open(filename + "." + fileext, "w")
usrstring = file
file.seek(0)
file.write(UsrString())
file.close()

print("File created")
print("Press enter to exit")
input("")