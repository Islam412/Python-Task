'''
2. Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional
programming]
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha','mm']
#normal list
name=[]
for n in Names:
    if 'a' in n:
       name.append(n)
print(name)
print("_______________________________________________")

#list comprehension
name1=[n for n in Names if 'a' in n]
print(name1)
print('_______________________________________________')

#functional programming
def search(n):
    if 'a' in n:
        return n
name2=map(search,Names)
print(list(name2))
name3=filter(search,Names)
print(list(name3))
