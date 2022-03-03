from mathtopolish import mathtopolishconverter

def runner():
    print("Please insert the number of the desired language: \n [1]Logical Connectives \n [2]Mathematical expression \n [3]Quit")
    x = int(input())
    if x == 1:
        print("logical output")
    elif x == 2:
        print("Please insert the mathematical equation. Example: (A+B)-(C*D)/E^F")
        mathtopolishconverter(input())
        print("Would you like to try something else[Y/N]")
        if (str(input()) in "Yy"):
            runner()

runner()



