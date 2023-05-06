symbols = ["+", "-", "*", "/"]
operator = input("1. add\n2. subtract\n3. multiply\n4. divide\nwhat would you like to do? (1/2/3/4): ")

def getOperator():
    global operator, firstNumber, secondNumber
    if operator in ["1", "2", "3", "4"]:

        firstNumber = input("first number: ")
        secondNumber = input("second number: ") 

        operator = symbols[int(operator)-1]
        print(eval(f"{firstNumber} {operator} {secondNumber}"))

        if operator == 1:
            print(firstNumber)

    else:
        operator = input("not a valid option, please try again: ")
        getOperator()

getOperator()
