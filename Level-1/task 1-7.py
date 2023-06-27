'''
8. Create a function that takes x,y and prints all the number that can be divide by y from x to 100
'''
for x in range(0, 101):
    if (x % 2) and (x % 3): 
        print("2, 3: ", x)
    elif x % 2 == 0: 
        print("2: ", x)
    elif x % 3 == 0: 
        print("3: ", x)
