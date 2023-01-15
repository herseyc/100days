
#Add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Dictionary of basic calculator functions
calc_functions = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

print("***Calculator***")

def calculator():
  num1 = float(input("What is your first number: "))
  should_continue = True
  for symbol in calc_functions:
    print(symbol)

  while should_continue:
    operation_symbol=input("Pick an operation: ")
    num2 = float(input("What is the next number: "))

    calc_f = calc_functions[operation_symbol]

    answer = calc_f(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ") == "y":
       num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
