from subprocess import call

print('Welcome To A Ton Of Games')
print("Game Options")
print()
print("1--QuantumTool")
print("2--Mad Libs")
print("3--RandomFact")
print()
userinput = int(input("What Game Would You Like To Play(Number)"))
if userinput == 1:
    call(["python", "Games/QuantumTool.py"])
elif userinput == 2:
    call(["python", "Games/MadLibs.py"])
elif userinput == 3:
    call(["python", "Games/RandomFact.py"])
