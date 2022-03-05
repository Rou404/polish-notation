# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin and my colleague
from tabulate import tabulate

output = []
operator = []
evaluation = []
operator_value = {"!": 3, "|": 1, "&": 2, "-": 2, "(": 0, ")": 0, "=": 2}


def tableformer(x, operator, evaluation):
    aux = []
    aux.append(x)
    aux.append(" ".join(operator))
    aux.append(" ".join(evaluation))
    output.append(aux)

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
        tableformer(" ", operator, evaluation)

def logictopolishconverter(y):
    expression = [x for x in y]
    expression = expression[::-1]

    for x in expression:
        match x:
            case "!":
                if operator:
                    remove(x)
                operator.append(x)
            case "&":
                if operator:
                    remove(x)
                operator.append(x)
            case "|":
                if operator:
                    remove(x)
                operator.append(x)
            case "-":
                if operator:
                    remove(x)
                operator.append(x)
            case "=":
                if operator:
                    remove(x)
                operator.append(x)
            case ")":
                operator.append(x)
            case "(":
                while operator and operator[-1] != ")":
                    tableformer(x, operator, evaluation)
                    evaluation.append(operator.pop())
                    x = " "
                tableformer(" ", operator, evaluation)
                operator.pop()
            case _:
                evaluation.append(x)
        tableformer(x, operator, evaluation)
    computefinal()
    aux = [" ", "Result is: ", "".join(evaluation[::-1])]
    output.append(aux)
    print(tabulate(output, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

logictopolishconverter("!(!A|!B)")