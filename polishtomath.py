#This module computes the value of the expression in the polish format
expression = [x for x in input()]
expression = expression[::-1]

def isoperator(token):
    if token in ['+','-','*','/','^','%']:
        return True
    else:
        return False

def polishtoinfix(exp):
    polishstack = []
    for token in expression:
        if not isoperator(token):
            polishstack.append(token)
        else:
            aux = "(" + polishstack.pop() + token + polishstack.pop() + ")"
            polishstack.append(aux)
    return polishstack.pop()

print("Result is:",polishtoinfix(expression))


