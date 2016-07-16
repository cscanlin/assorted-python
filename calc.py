def MainMenu() :
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Quit")
    checkOperation = str(raw_input("enter the number of the option you wish to choose : "))
    if checkOperation == "1" :
        addFunction()
    elif checkOperation == "2" :
        subFunction()
    elif checkOperation == "3" :
        multFunction()
    elif checkOperation == "4" :
        divFunction()
    elif checkOperation == "5" :
        print("program end")
    else :
        print("wrong input")
def addFunction() :
              num1 = float(input("enter 1st num : "))
              num2 = float(input("enter 2nd num : "))
              result = num1 + num2
              print("Result --> " + str(result))
              MainMenu()
def subFunction() :
              num1 = float(input("enter 1st num : "))
              num2 = float(input("enter 2nd num : "))
              result = num1 - num2
              print("Result --> " + str(result))
              MainMenu()
def multFunction() :
              num1 = float(input("enter 1st num : "))
              num2 = float(input("enter 2nd num : "))
              result = num1 * num2
              print("Result --> " + str(result))
              MainMenu()
def divFunction() :
              num1 = float(input("enter 1st num : "))
              num2 = float(input("enter 2nd num : "))
              result = num1 / num2
              print("Result --> " + str(result))
              MainMenu()

MainMenu()
