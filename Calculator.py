print("WELCOME TO THE CALCULATOR\nWhere claculation is fun")

def Calculator():
    def addition(n1, n2):
        return n1 + n2
    def subtraction(n1, n2):
        return n1 - n2
    def multiplication(n1, n2):
        return n1 * n2
    def modulo(n1, n2):
        return n1 % n2
    def division(n1, n2):
        return n1 / n2
    def exponential(n1, n2):
        return n1 ** n2

    operations = {"+": addition, "-": subtraction, "*": multiplication,
              "%": modulo, "/": division, "**": exponential }
    n1 = float(input("Enter your first number: "))
    
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("Enter your secont number: "))
        answer = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        choice = input(f"Would you like to continue the calculation with {answer}, yes/no: ").lower()
        if choice == "yes":
            n1 = answer
            continue
        else:
            should_continue = False
            print("\n" * 4)
            Calculator()

Calculator()