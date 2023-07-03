'''
3. Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional
programming]
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha','mm','oto']
name=[]
for n in Names:
    if n[0]=='t':
        name.append(n)
print(name)
print("___________________________________________________________________________")

#list comprehension
name1=[n for n in Names if n[0]=='t']
print(name1)
print("____________________________________________________________________________")


#functional programming
def search(n):
    if n[0]=='t':
        return (n)
name3=filter(search,Names)
print(list(name3))
print("____________________________________________________________________________")
