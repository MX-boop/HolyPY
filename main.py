import subprocess

def run_game(game_file_path):
    subprocess.call(["python", game_file_path])

def display_game_options():
    print("Welcome To A Ton Of Games")
    print("Game Options")
    print("1--QuantumTool")
    print("2--Mad Libs")
    print("3--RandomFact")
    print()

def main():
    display_game_options()
    user_input = int(input("What Game Would You Like To Play (Enter the number): "))

    if user_input == 1:
        run_game("Games/QuantumTool.py")
    elif user_input == 2:
        run_game("Games/MadLibs.py")
    elif user_input == 3:
        run_game("Games/RandomFact.py")
    else:
        print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == '__main__':
    main()
