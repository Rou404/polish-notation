from tabulate import tabulate

def polishcalculator(exp):
    expression = [x for x in exp.split()]
    expression = expression[::-1]
    stack = []
    final = []
    copy = [expression]
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
                stack.append(aux)
            case "%":
                aux = stack.pop() % stack.pop()
                stack.append(aux)
            case "^":
                a = stack.pop()
                b = stack.pop()
                aux = pow(a, b)
                stack.append(aux)
            case _:
                stack.append(int(token))
        auxiliary.append(token)
        auxiliary.append(copy)
        auxiliary.append(" ".join(stack))
        print(stack)
        final.append(auxiliary)

    print(tabulate(final, headers=["Token", "Expression", "Result"], tablefmt="grid"))
    print("Result is:",stack.pop())

polishcalculator("- 100 200")
