print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")

operator = input("1. add\n2. subtract\n3. multiply\n4. divide\nwhat would you like to do? (1/2/3/4):\n")

def getOperator():
    global operator
    if operator in ["1", "2", "3", "4"]:
        print("success")
    else:
        operator = input("not a valid option, please try again:\n")
        getOperator()

getOperator()
