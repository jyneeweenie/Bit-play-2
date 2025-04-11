# Program to check if user number inputs are equal without using any comparison operator
def checkIfSame(number1, number2):
# user XOR operator as a^a is always 0
    if ((number1 ^ number2) != 0):
        print("Numbers are not equal")
    else:
        print("Both numbrs are equal")
# Taking input
number1 = int(input("Enter your first number to compare : "))
number2 = int(input("Enter your first number to compare : "))
checkIfSame(number1, number2)