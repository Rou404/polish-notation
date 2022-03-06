from tabulate import tabulate

stack = []
final = []

def tableformer(token, operator):
    auxiliary = []
    auxiliary.append(token)
    auxiliary.append(" ".join(operator))
    auxiliary.append(" ".join([str(x) for x in stack]))
    final.append(auxiliary)

def neg(a):
    if a == 1:
        return 0
    return 1

def lor(a,b):
    if a == 0 and b == 0:
        return 0
    return 1

def land(a ,b):
    if a or b:
        return 1
    return 0

def lto(a ,b):
    if a == 0 and b:
        return 0
    return 1

def equal(a,b):
    if a == b:
        return 1
    return 0

def polishlogicalcalculator(exp):
    expression = [x for x in exp]
    expression = expression[::-1]
    stack = []
    final = []
    for token in expression:
        match token:
            case "!":
                a = stack.pop()
                stack.append(neg(a))
            case "|":
                a = lor(stack.pop(), stack.pop())
                stack.append(a)
            case "&":
                a = land(stack.pop(), stack.pop())
                stack.append(a)
            case "-":
                a = lto(stack.pop(), stack.pop())
                stack.append(a)
            case "=":
                a = equal(stack.pop(), stack.pop())
                stack.append(a)
            case _:
                stack.append(int(token))
        auxiliary = [token, " ".join([str(x) for x in stack])]
        final.append(auxiliary)
    final.append(["Result is: ", stack.pop()])
    print(tabulate(final, headers=["Token", "Result"], tablefmt="grid"))

polishlogicalcalculator("-&!|110=10")