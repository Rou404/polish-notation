from tabulate import tabulate

output = []

def isoperator(token):
    if token in ['+','-','*','/','^','%']:
        return True
    else:
        return False

def tableformer(x, evaluation):
    aux = []
    aux.append(x)
    aux.append(" ".join(evaluation))
    output.append(aux)

def polishtoinfix(exp):
    expression = [x for x in exp]
    expression = expression[::-1]
    polishstack = []
    for token in expression:
        if not isoperator(token):
            polishstack.append(token)
        else:
            aux = "(" + polishstack.pop() + token + polishstack.pop() + ")"
            polishstack.append(aux)
        tableformer(token, polishstack)
    tableformer("Result", polishstack)

    print(tabulate(output, headers=["Token", "Evaluation Stack"], tablefmt="grid"))

polishtoinfix("--a-aab")
