def addition (number1 , number2):
    return number1 + number2

def substraction (number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def calculator(operation, number1 , number2):
    return operation(number1 , number2)

number1 = int(input("What's the value of the first number? : "))
number2 = int(input("What's the value of the second number? : "))
operation = int(input("What would you like me to do? press 0 for addition , 1 for substraction , 2 for multiplication and 3 for division : "))


if operation == 0 :
    print(calculator(addition , number1 , number2))

elif operation == 1 :
    print(calculator(substraction ,number1, number2))

elif operation == 2 :
    print(calculator(multiplication , number1 , number2))

elif operation == 3 :
    print(calculator(multiplication, number1 , number2))

else : 
    print("Wrong command")


