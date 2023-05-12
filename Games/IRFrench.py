from subprocess import call

print("Welcome To The French Classroom")
print("What Would You Like To Learn About")

print("1--IR verb conjugations")

usr_input = input("What Is You Selection")

if usr_input == "1":
    print("Sounds Good!")
    call(["python3", "Games/FrenchGames/IRverbs.py"])