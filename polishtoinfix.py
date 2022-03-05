from tabulate import tabulate

output = []

def isoperator(token):
    if token in ['+', '-', '*', '/', '^', '%', '&', '|', '-', '=']:
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
        if isoperator(token):
            aux = "(" + polishstack.pop() + token + polishstack.pop() + ")"
            polishstack.append(aux)
        elif token == "!":
            aux = "!"+polishstack.pop()
            polishstack.append(aux)
        else:
            polishstack.append(token)

        tableformer(token, polishstack)
    tableformer("Result", polishstack)

    print(tabulate(output, headers=["Token", "Evaluation Stack"], tablefmt="grid"))

polishtoinfix("-|!A-&BCD!|=EFG")
