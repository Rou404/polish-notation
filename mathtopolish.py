# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin and my colleague

from tabulate import tabulate

expression = [x for x in "d*(c+d)"]
expression = expression[::-1]
operator = []
evaluation = []
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 1, ")": 1, "^": 3}
print("Expression evaluating: "+" ".join(expression))
output = []
count = 1

def remove(x):
    while operator_value[operator[-1]] > operator_value[x]:
        evaluation.append(operator[-1])
        operator.pop()
        if len(operator) < 2:
            break

for x in expression:
    aux = []
    match x:
        case "+":
            if operator:
                remove(x)
            operator.append(x)
        case "-":
            if operator:
                remove(x)
            operator.append(x)
        case "*":
            if operator:
                remove(x)
            operator.append(x)
        case "/":
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
            for y in operator[::-1]:
                if y == ")":
                    break
                else:
                    evaluation.append(y)
                    operator.pop()
            operator.pop()
        case _:
            evaluation.append(x)
    aux.append(x)
    aux.append(" ".join(operator))
    aux.append(" ".join(evaluation))
    output.append(aux)
for x in operator[::-1]:
    aux = []
    evaluation.append(x)
    operator.pop()
    aux.append(x)
    aux.append(" ".join(operator))
    aux.append(" ".join(evaluation))
    output.append(aux)

print(tabulate(output, headers = ["Token", "Operator Stack", "Evaluation Stack"], tablefmt="grid"))

print("Final result in polish notation = "," ".join(evaluation[::-1]))


