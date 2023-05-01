from subprocess import call

print('Welcome To A Ton Of Games')
print("Game Options")
print()
print("1--QuantumTool")
print("2--Mad Libs")
print("3--RandomFact")
print("4--Friend")
print()
userinput = int(input("What Game Would You Like To Play(Number)"))
if userinput == 1:
    call(["python3", "Games/QuantumTool.py"])
elif userinput == 2:
    call(["python3", "Games/MadLibs.py"])
elif userinput == 3:
    call(["python3", "Games/RandomFact.py"])
elif userinput == 4:
    call(["python3", "Games/Friend.py"])
