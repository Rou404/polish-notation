# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin and my colleague
from tabulate import tabulate

output = []
operator = []
evaluation = []
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 1, ")": 1, "^": 3, "%": 2}

def remove(x):
    while operator_value[operator[-1]] > operator_value[x]:
        evaluation.append(operator[-1])
        operator.pop()
        if len(operator) < 2:
            break

def computefinal():
    for x in operator[::-1]:
        evaluation.append(x)
        operator.pop()
        output.append([" ", " ".join(operator)," ".join(evaluation)])

def mathtopolishconverter(y):
    expression = [x for x in y.split()]
    expression = expression[::-1]
    lasttoken = " "
    for x in expression:
        match x:
            case "+":
                if operator:
                    remove(x)
                operator.append(x)
            case "-":
                if lasttoken.isalpha():
                    if operator:
                        remove(x)
                    operator.append(x)
                else:
                    y = "-"+evaluation.pop()
                    evaluation.append(y)
            case "*":
                if operator:
                    remove(x)
                operator.append(x)
            case "/":
                if operator:
                    remove(x)
                operator.append(x)
            case "%":
                if operator:
                    remove(x)
                operator.append(x)
            case "^":
                if operator:
                    remove(x)
                operator.append(x)
            case ")":
                operator.append(x)
            case "(":
                while operator and operator[-1] != ")":
                    output.append([x, " ".join(operator)," ".join(evaluation)])
                    evaluation.append(operator.pop())
                    x = " "
                output.append([" ", " ".join(operator)," ".join(evaluation)])
                operator.pop()
                continue
            case _:
                evaluation.append(x)
        output.append([" ", " ".join(operator)," ".join(evaluation)])
    computefinal()
    output.append([" ", "Result is: ", " ".join(evaluation[::-1])])
    print(tabulate(output, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

mathtopolishconverter("-100 + -10 / 2")
