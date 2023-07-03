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
def my_upper(Names):
    return Names.upper()
name2=map(my_upper,Names)
print(list(name2))
print("____________________________________________________________________")

