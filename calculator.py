""""
Gets user input of 2 integers and operators, and printing out result

calculator() takes 3 arguments:
number1
number2
operator : does operation if inputs are "+", "-", "*", "/", "//", "**", "%"

Returns:
output : result of oepration

Example:
number1 = 20
number2 = 10
operator = "+"
return output = 30

input_output() gets user input for for number1, number2, and operator. It calls on the calculator() to perform the math
Then it asks if want to coninue or exit program.

"n" = if user input "n", the program continues asking questions
"y" = program breaks / exit out

"""

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
    


