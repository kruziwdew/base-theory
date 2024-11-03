import numpy as np

dice = int(input("What dice do you have (6/12)  "))
dice_range = range(1, dice)

rolls = int(input("Enter the number of the rolls  "))
results = np.random.choice(dice_range, size = rolls, replace =True)
print(results)