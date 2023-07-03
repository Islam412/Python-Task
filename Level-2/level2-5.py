'''
5. Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
#normal list
name=[]
for n in Names:
    name.append(len(n))
print(name)
print("___________________________________________________________")


#list comprehension
name1=[len(n) for n in Names]
print(name1)
print("___________________________________________________________")

#functional programming
def my_len(n):
    return len(n)
name3=map(my_len,Names)
print(list(name3))
print("___________________________________________________________")
