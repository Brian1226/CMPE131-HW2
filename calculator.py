def calculator(number1, number2, operator):
  """
  This function prints a result depending on number1, number2, and the inputted operator

  parameters:
  number1 : float
  number2 : float
  operator : "+", "-", "*", "/", "**", "//", "%"

  Example:
    number1: 10
    number2 : 10
    operator : "+"
    returns 20
  """
  if operator == "+":
    print(number1 + number2)
  elif operator == "-":
    print(number1 - number2)
  elif operator == "*":
    print(number1 * number2)
  elif operator == "/":
    print(number1 / number2)
  elif operator == "//":
    print(number1 // number2)
  elif operator == "**":
    print(number1 ** number2)
  elif operator == "%":
    print(number1 % number2)
  else:
    return False


def input_output():
  """
  This function takes user input for number1, number2, and operator. then it calls calculator()
  Then it asks if want to continue, otherwise the code stops running  

  number1 : int
  number2 : int
  operator : "+", "-", "*", "/", "**", "//", "%"
  "n" : continue asking
  "y" : exit 
  """

  number1 = input("Enter the first number: ")
  number1 = float(number1)
  number2 = input("Enter the second number: ")
  number2 = float(number2)
  operator = input("Enter the operation: ")
  print(calculator(number1, number2, operator))
  next = input("Do you wish to exit: ")

  #keeps on asking user if want to continue when unput is "n", and it stops running when input is "y"
  while(next == "n"):
    number1 = input("Enter the first number: ")
    number1 = float(number1)
    number2 = input("Enter the second number: ")
    number2 = float(number2)
    operator = input("Enter the operation: ")
    print(calculator(number1, number2, operator))
    next = input("Do you wish to exit: ")

    if next == "y":
      break
    
input_output()
  


