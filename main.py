import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
#print(operations["*"](4,8))
def calculator():
    print(art.logo)
    should_accumlate = True
    num1 = float(input("what is the first number?: "))

    while should_accumlate:


        for symbol in operations:
            print(symbol)
        operation_symbols = input("Pick an operation: ")

        num2 = float(input("what is the second number?: "))
        answer = operations[operation_symbols](num1, num2)
        print(f"{num1} {operation_symbols} {num2} {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calulation:")

        if choice == "y":
            num1 = answer

        else:
            should_accumlate = False
            print("\n" * 20)
            calculator()

calculator()