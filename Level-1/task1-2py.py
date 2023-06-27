'''2. Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y'''

x=int(input("Enter frist number: "))
y=int(input("Enter second number: "))
for z in range(0,101):
    if z%x==0 and z%y==0:
        print(z)
