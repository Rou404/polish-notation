# This is an optional project for Formal Languages and Automata Theory 2021-2022.
# Done by Stegeran Darius Cosmin
# You need to use python3.10 or higher in order to work since switch statements were added only in 3.10


#Initialization of lists

expression = [x for x in "b*(c-d)"]
expression = expression[::-1]                           #List reversed 
operator = []                                           #Operator Stack
evaluation = []                                         #Evaluation stack
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2}       #Dictionary holding priority values for the oprands
print(expression)
print("input  operators  evaluation")
for x in expression:
    match x:
        case "+":                                       #For + and - it's quite redundant since there is no smaller value than 1 in priority
            operator.append(x)
        case "-":
            operator.append(x)
        case "*":
            if operator:
                while operator_value[operator[-1]] > operator_value[x]:       #in the * case it checks for smaller values in the operand stack
                    operator.pop()                                            # and pops them into the evaluation stack
            operator.append(x)
        case "/":
            if operator:
                while operator_value[operator[-1]] > operator_value[x]:        #same for / 
                    operator.pop()
            operator.append(x)
        case ")":
            operator.append(x)
        case "(":
            for x in operator[::-1]:
                while x != ")":
                    operator.pop()
                    evaluation.append(x)
                    break
            operator.pop()
        case _:
            evaluation.append(x)
    print(x, "  ", operator, "   ", evaluation)
for x in operator:
    evaluation.append(x)
    operator.pop()
    print("    ", operator, "   ", evaluation)

