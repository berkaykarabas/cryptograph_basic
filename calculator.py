# calculator

# add
def add(n1, n2):
    return n1 + n2


# substraction
def substract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


dictionary_math = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculate():
    num1 = int(input("What is your first number."))
    calculator_finish = True

    while calculator_finish:

        for operation in dictionary_math:
            print(operation)
        operation_symbols = input("Which operation do you want to select?")
        if operation_symbols == "+":
            dictionary_math["+"]
        elif operation_symbols == "-":
            dictionary_math["-"]
        elif operation_symbols == "*":
            dictionary_math["*"]
        elif operation_symbols == "/":
            dictionary_math["/"]
        else:
            print("Please enter valid symbol")
        num2 = int(input("What is your second number."))
        calculation_function = dictionary_math[operation_symbols]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbols} {num2} = {result}")
        continue_calculation = input("Do you wanna calculate more with your answer ? 'y' or 'n'.")
        if continue_calculation == "y":
            num1 = result

        elif continue_calculation == "n":
            calculator_finish = True
            calculate()


calculate()