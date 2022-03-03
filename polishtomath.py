#This module computes the value of the expression in the polish format

def isoperator(token):
    if token in ['+','-','*','/','^','%']:
        return True
    else:
        return False

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
    print("Result is:",polishstack.pop())


