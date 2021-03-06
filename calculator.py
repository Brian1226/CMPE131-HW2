def calculator(number1, number2, operator):
  if operator == "+":
    output = (number1 + number2)
  elif operator == "-":
    output = (number1 - number2)
  elif operator == "*":
    output = (number1 * number2)
  elif operator == "/":
    output = (number1 / number2)
  elif operator == "//":
    output = (number1 // number2)
  elif operator == "**":
    output = (number1 ** number2)
  elif operator == "%":
    output = (number1 % number2)
  return output


def input_output():
 
  number1 = input("Enter the first number: ")
  number1 = float(number1)
  number2 = input("Enter the second number: ")
  number2 = float(number2)
  operator = input("Enter the operation: ")
  print(calculator(number1, number2, operator))
  next = input("Do you wish to exit: ")

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
  
