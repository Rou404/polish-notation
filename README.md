# Generation and evaluation of Polish notation

---

### Polish notation (prefix) is a mathematical notation in which operators precede their operands, in contrast to the more common infix notation, in which operators are placed between operands.

---

### Why polish notation?

The idea is simply to have a parenthesis-free notation that makes each equation shorter and easier to parse in terms of defining the evaluation priority of the operators.

---

## Converting infix to prefix.

Converting infix to prefix is done by making use of two stacks, one for the operators and one for the operands.

1. For every term in expression
    1. If it’s an operand
        1. Push to evaluation stack.
    2. If it’s an operator
        1. While the stack is not empty and the last operator’s precedence is equal or higher than the term
            1. Pop the operator from the operator stack
            2. Compute the operation between the last two operands in the evaluation stack
            3. Push the result back in the evaluation stack
        2. Push operator to operator stack
    3. If it’s “(”
        1. Push to operator stack
    4. If it’s “)”
        1. While the last operator in the stack is not equal to “(”
            1. Pop the operator from the operator stack
            2. Compute the operation between the last two operands in the evaluation stack
            3. Push the result back in the evaluation stack
        2. Pop the operand from the stack
2. While the operand is not empty 
    1. Pop the operator from the operator stack
    2. Compute the operation between the last two operands in the evaluation stack
    3. Push the result back in the evaluation stack
3. Evaluation contains only one element, being the expression in prefix form.

---

```python
# This is an optional project for Formal Languages and Automata Theory 2022
# Done by Stegeran Darius Cosmin
from tabulate import tabulate

operator = []
evaluation = []
operator_value = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 1, ")": 1, "^": 3}

def compute(x):
    while operator_value[operator[-1]] > operator_value[x]:
        evaluation.append(operator[-1])
        operator.pop()
        if len(operator) < 2:
            break

def computefinal():
    for x in operator[::-1]:
        evaluation.append(x)
        operator.pop()
        tableformer(" ", operator, evaluation)

def mathtopolishconverter(y):
    expression = [x for x in y]
    expression = expression[::-1]

    for x in expression:
        match x:
            case "+":
                if operator:
                    compute(x)
                operator.append(x)
            case "-":
                if operator:
                    compute(x)
                operator.append(x)
            case "*":
                if operator:
                    compute(x)
                operator.append(x)
            case "/":
                if operator:
                    compute(x)
                operator.append(x)
            case "%":
                if operator:
                    compute(x)
                operator.append(x)
            case "^":
                if operator:
                    compute(x)
                operator.append(x)
            case ")":
                operator.append(x)
            case "(":
                while operator and operator[-1] != ")":
                    evaluation.append(operator.pop())
                    x = " "
                operator.pop()
            case _:
                evaluation.append(x)
    computefinal()
```

```python
mathtopolishconverter(A^(B*C)%(D/E-F+G)
+---------+------------------+---------------------------+
| Token   | Operator Stack   | Evaluation Stack          |
+=========+==================+===========================+
| )       | )                |                           |
+---------+------------------+---------------------------+
| G       | )                | G                         |
+---------+------------------+---------------------------+
| +       | ) +              | G                         |
+---------+------------------+---------------------------+
| F       | ) +              | G F                       |
+---------+------------------+---------------------------+
| -       | ) + -            | G F                       |
+---------+------------------+---------------------------+
| E       | ) + -            | G F E                     |
+---------+------------------+---------------------------+
| /       | ) + - /          | G F E                     |
+---------+------------------+---------------------------+
| D       | ) + - /          | G F E D                   |
+---------+------------------+---------------------------+
| (       | ) + - /          | G F E D                   |
+---------+------------------+---------------------------+
|         | ) + -            | G F E D /                 |
+---------+------------------+---------------------------+
|         | ) +              | G F E D / -               |
+---------+------------------+---------------------------+
|         | )                | G F E D / - +             |
+---------+------------------+---------------------------+
| %       | %                | G F E D / - +             |
+---------+------------------+---------------------------+
| )       | % )              | G F E D / - +             |
+---------+------------------+---------------------------+
| C       | % )              | G F E D / - + C           |
+---------+------------------+---------------------------+
| *       | % ) *            | G F E D / - + C           |
+---------+------------------+---------------------------+
| B       | % ) *            | G F E D / - + C B         |
+---------+------------------+---------------------------+
| (       | % ) *            | G F E D / - + C B         |
+---------+------------------+---------------------------+
|         | % )              | G F E D / - + C B *       |
+---------+------------------+---------------------------+
| ^       | % ^              | G F E D / - + C B *       |
+---------+------------------+---------------------------+
| A       | % ^              | G F E D / - + C B * A     |
+---------+------------------+---------------------------+
|         | %                | G F E D / - + C B * A ^   |
+---------+------------------+---------------------------+
|         |                  | G F E D / - + C B * A ^ % |
+---------+------------------+---------------------------+
|         | Result is:       | %^A*BC+-/DEFG             |
+---------+------------------+---------------------------+

```

---

# Converting prefix to infix

Converting prefix to infix is done quite easily, since there are no paratheses. Although the end result is quite messy.

1. For every token in expression
    1. If the token is an operator
        1. Pop two elements
        2. Push operation of the two elements between paratheses
    2. If the token is negation
        1. Pop one element and add negation
        2. Push to stack
    3. If the token is an operand
        1. Push to stack

```python

def isoperator(token):
    if token in ['+', '-', '*', '/', '^', '%', '&', '|', '-', '=']:
        return True
    else:
        return False

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

```

```python

+---------+---------------------------+
| Token   | Evaluation Stack          |     polishtoinfix(%^A*BC+-/DEFG)
+=========+===========================+
| G       | G                         |
+---------+---------------------------+
| F       | G F                       |
+---------+---------------------------+
| E       | G F E                     |
+---------+---------------------------+
| D       | G F E D                   |
+---------+---------------------------+
| /       | G F (D/E)                 |
+---------+---------------------------+
| -       | G ((D/E)-F)               |
+---------+---------------------------+
| +       | (((D/E)-F)+G)             |
+---------+---------------------------+
| C       | (((D/E)-F)+G) C           |
+---------+---------------------------+
| B       | (((D/E)-F)+G) C B         |
+---------+---------------------------+
| *       | (((D/E)-F)+G) (B*C)       |
+---------+---------------------------+
| A       | (((D/E)-F)+G) (B*C) A     |
+---------+---------------------------+
| ^       | (((D/E)-F)+G) (A^(B*C))   |
+---------+---------------------------+
| %       | ((A^(B*C))%(((D/E)-F)+G)) |
+---------+---------------------------+
| Result  | ((A^(B*C))%(((D/E)-F)+G)) |     From A^(B*C)%(D/E-F+G)
+---------+---------------------------+
					
```

### Computing prefix

Takes the same steps as converting to infix, but calculates the operation between elements.

```python

def polishcalculator(exp):
    expression = [x for x in exp.split()]
    expression = expression[::-1]
    stack = []
    for token in expression:
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
```
