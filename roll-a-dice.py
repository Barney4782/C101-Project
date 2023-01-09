import random

response= input("press y to roll, or n to exit: ")


def diceFunc(response):
    while response=="y":
        no = random.randint(1, 6)
        if(no==1):
            print("[-----]")
            print("[--0--]")
            print("[-----]")
        elif(no==2):
            print("[0----]")
            print("[-----]")
            print("[----0]")
        elif(no==3):
            print("[0----]")
            print("[--0--]")
            print("[----0]")
        elif(no==4):
            print("[0---0]")
            print("[-----]")
            print("[0---0]")
        elif(no==5):
            print("[0---0]")
            print("[--0--]")
            print("[0---0]")
        else:
            print("[0---0]")
            print("[0---0]")
            print("[0---0]")
        response=""
        response= input("press y to roll again, or n to exit: ")
    print("Thanks of using the virtual dice!")
diceFunc(response)
    
    



