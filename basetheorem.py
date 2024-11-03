def findprobab(a,b):
    if a ==1:
        proba= 0.2
        if b==1:
            probag = 0.85
        elif b ==2:
            probag = 0.15
        else:
            print("Invalid Choice") 
        proba_b = proba*probag
        print("Both the events occuring tgt = ", proba_b)
        print("Probablity of b given a  ", probag)
    elif a ==2 :
        proba= 0.8
        if b==1:
            probag = 0.02
        elif b ==2:
            probag = 0.98
        else:
            print("Invalid Choice") 
        proba_b = proba*probag
        print("Both the events occuring tgt = ", proba_b)
        print("Probablity of b given a  ", probag)

print("lets calculate the probablity, enter your choice:  ")
a = int(input("Does the person have a sterp throat \n 1. yes \n 2. no "))
b = int(input("Does the person test positive \n 1. yes \n 2. no "))
findprobab(a,b)


