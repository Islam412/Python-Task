#Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
#input
try:
    start=int(input('Enter start number please: '))
    end=int(input('Enter end number please: '))
except(ValueError):
    print("Ennter int num.....")
#output
for x in range(start,end):
    for y in range(start,end):
        print(f'{x}X{y}={x*y}')
    print('______________________________________')
