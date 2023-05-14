import math

print("Welcome to the Quadratic Problem Solver!")
print("Will you be solveing a word problem or equation?")
print("1. Word Problem")
print("2. Equation")

#could you fix the variable names to be more descriptive?
choice = input("Enter your choice: ")
word_problem = False
number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
equation_abc = []

if choice == "1":
    word_problem = True
elif choice == "2":
    word_problem = False
else:
    print("Invalid choice")
    exit()

def find_discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

def solve_equation(a, b, c):
    discriminant = find_discriminant(a, b, c)
    if discriminant < 0:
        print("No real solutions")
    elif discriminant == 0:
        print("One solution: " + str(-b / (2 * a)))
    else:
        print("Two solutions: " + str((-b + math.sqrt(discriminant)) / (2 * a)) + ", " + str((-b - math.sqrt(discriminant)) / (2 * a)))

def find_word_abc():
    print("Please enter you word problem")
    word_problem_usr = input("Enter your word problem: ")
    for i in range(len(word_problem_usr)):

        if word_problem_usr[i] in number_list:

            equation_abc.append(int(word_problem_usr[i]))

def main():
    if word_problem:
        find_word_abc()
        solve_equation(equation_abc[0], equation_abc[1], equation_abc[2])
    else:
        print("Please enter the coefficients of your equation")
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        solve_equation(a, b, c)

main()