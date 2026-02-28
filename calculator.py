#
#   Calculator Project
#

#-----------------------------------------------------------
def menu ():
    print("1. Enter an expression (number operator number): ")
    print("2. Quit the program")
#-----------------------------------------------------------
def parse(expr):
    expr.strip()
    if("+" in expr):
        index = expr.find("+")
        operator = "+"
    elif("-" in expr):
        index = expr.find("-")
        operator = "-"
    elif("*" in expr):
        index = expr.find("*")
        operator = "*"
    elif ("/" in expr):
        index = expr.find("/")
        operator = "/"
    else:
        return "Invalid expression"

    firstNumber = expr[0:index]
    firstNumoer = firstNumber.strip()
    secondNumber = expr[index+1: len(expr)]
    secondNumber = secondNumber.strip()

    if (firstNumber.isnumeric() and secondNumber.isnumeric()):
        return [firstNumber, operator, secondNumber]
    else:
        return "Invalid expression"


#-----------------------------------------------------------
def calculate(list1):
    if (list1[1] == "+"):
        return float(list1[0]) + float(list1[2])
    elif(list1[1]=="-"):
        return float(list1[0]) - float(list1[2])
    elif(list1[1]=="*"):
        return float (list1[0]) * float(list1[2])
    elif(list1[1]=="/"):
        if float (list1[2])== 0:
            return "ERROR you cannot divide by zero"
        else:
            return float (list1[0]) / float(list1[2])

def solving():
    expression = str(input("Enter an expression: "))
    parsed_expression = parse(expression)
    while (parsed_expression == "Invalid expression"):
        print("Invalid expression")
        expression = str(input("Enter an expression: "))
        parsed_expression = parse(expression)
    else:
        result = calculate(parsed_expression)
        print("RESULT: " , result)
               

#-----------------------------------------------------------
def main():
    while (True):
        menu()
        option = str(input("Enter an option: "))
        if (option == "1"):
            expression = str(input("Enter an expression: "))
            parsed_expression = parse(expression)
            if (parsed_expression == "invalid expression"):
                print ("Invalid expression")
            else:
                result = calculate (parsed_expression)
                print("Result: ", result)

                anotherOp = input(" Do you want to do another operation?")
                if anotherOp != ("yes" or "y" or "y" or "Yes" or "YES"):
                    break
                elif(option == "2"):
                    break
                else:
                    print("ERROR: please reenter your option")



#-----------------------------------------------------------

main()
















    
    
