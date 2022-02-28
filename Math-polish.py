# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin

expression = [x for x in "(A+B)*C/E-F"]
expression = expression[::-1]
operator = []
evaluation = []
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2}
print(expression)
print("input  operators  evaluation")
for x in expression:
    match x:
        case "+":
            operator.append(x)
        case "-":
            operator.append(x)
        case "*":
            if operator:
                while operator_value[operator[-1]] > operator_value[x]:
                    operator.pop()
            operator.append(x)
        case "/":
            if operator:
                while operator_value[operator[-1]] > operator_value[x]:
                    operator.pop()
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
    print(x, "  ", operator, "   ", evaluation)

for x in operator[::-1]:
    evaluation.append(x)
    operator.pop()
    print("[]", " ", operator, "   ", evaluation)

print("Final result in polish notation = ","".join(evaluation[::-1]))



