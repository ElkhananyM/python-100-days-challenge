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

proceed_or_refresh = "n"
while True:
    if proceed_or_refresh == "n":
        print("\n" * 20)
        print(art.logo)
        fnum = float(input("What's the first number?: "))
    op = input("+\n-\n*\n/\nPick an operation: ")
    snum = float(input("What's the second number?: "))
    result = operations[op](fnum, snum)
    print(f"{fnum} {op} {snum} = {result}")
    proceed_or_refresh = input(f"Type 'y' to continue calculating with {result},"
                               f" or type 'n' to start a new calculation: ")
    fnum = result
