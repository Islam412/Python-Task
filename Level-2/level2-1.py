'''1. Transform all names to uppercase using [normal list - list comprehension - functional programming]'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
#normal list
name=[]
for n in Names:
    name.append(n.upper())
print(name)
print("____________________________________________________________________")

#list comprehension
name1=[n.upper() for n in name]
print(name1)
print("___________________________________________________________________")

# - functional programming
def my_upper(name):
    return n.upper()
name2=list(map(my_upper,Names))
print(name2)


