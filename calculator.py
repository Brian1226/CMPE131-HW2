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
 
  number1 = float(input("Enter the first number: "))
  number2 = float(input("Enter the second number: "))
  operator = input("Enter the operation: ")
  print(calculator(number1, number2, operator))
  next = input("Do you wish to exit: ")

  while(next == "n"):
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter the operation: ")
    print(calculator(number1, number2, operator))
    next = input("Do you wish to exit: ")

    if next == "y":
      break
    

