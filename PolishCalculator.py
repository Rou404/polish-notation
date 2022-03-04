from tabulate import tabulate

def polishcalculator(exp):
    expression = [x for x in exp.split()]
    expression = expression[::-1]
    stack = []
    final = []
    copy = []
    copy.extend(expression[::-1])
    operation = []
    for token in expression:
        auxiliary = []
        match token:
            case "+":
                aux = stack.pop() + stack.pop()
                stack.append(aux)
            case "-":
                aux = stack.pop() - stack.pop()
                stack.append(aux)
            case "*":
                aux = stack.pop() * stack.pop()
                stack.append(aux)
            case "/":
                aux = stack.pop() / stack.pop()
                stack.append(float("{:.2f}".format(aux)))
            case "%":
                aux = stack.pop() % stack.pop()
                stack.append(aux)
            case "^":
                a = stack.pop()
                b = stack.pop()
                if a < 0:
                    aux = -a ** b
                else:
                    aux = a ** b
                stack.append(float("{:.2f}".format(aux)))
            case _:
                stack.append(int(token))
        auxiliary.append(token)
        auxiliary.append(" ".join(copy))
        auxiliary.append(" ".join([str(x) for x in stack][::-1]))
        final.append(auxiliary)
        copy.pop()

    print(tabulate(final, headers=["Token", "Expression", "Result"], tablefmt="grid"))
    print("Result is:",stack.pop())

polishcalculator("- ^ / -10 3 4 5")