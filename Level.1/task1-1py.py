#Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in the x,y range
x, y = int(input("Please input two integer numbers: ")), int(input("Please input two integer numbers: "))

even_list = []
odd_list = []

for n in range(x+1, y):
    if n%2 == 0: 
        even_list.append(n)
    else: 
        odd_list.append(n)


# print lists
print(f"Even Numbers: {even_list}")
print(f"Odd Numbers: {odd_list}")
  
