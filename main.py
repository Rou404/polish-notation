from mathtopolish import mathtopolishconverter
from polishtomath import polishtoinfix
from PolishCalculator import polishcalculator

def driver():
    print("Please insert the number of the desired language: \n [1]Logical Connectives \n [2]Mathematical expression \n [3]Quit")
    x = int(input())
    if x == 1:
        print("logical output")
    elif x == 2:
        print("Would you like to convert from or to polish notation? \n [1]From polish notation \n [2]To polish notation \n [3]Calcualte polish")
        y = int(input())
        if y == 1:
            print("Please insert the expression in polish notation. Example: -+AB/*CD^EF")
            polishtoinfix(input())
        elif y == 2:
            print("Please insert the mathematical equation. The available characters are {-+/*%^()} \nExample: (A+B)-(C*D)/E^F")
            mathtopolishconverter(input())
        elif y == 3:
            print("Please insert the mathematical equation with spaces between characters: Example: - -100 200")
            polishcalculator(input())
    print("Would you like to try something else[Y/N]")
    if (str(input()) in "Yy"):
        driver()
driver()





