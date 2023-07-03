'''
4. Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional
programming]
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
#normal list
name=[]
for n in Names:
    if n.count('a')>=2:
        name.append(n)
print(name)
print("_____________________________________________________________")

#list comprehension
name1=[n for n in Names if n.count('a')>=2]
print(name1)
print("_____________________________________________________________")

#functional programming
def search_letter(n):
    if n.count('a')>=2:
        return n
name3= filter(search_letter,Names)
print(list(name3))
print("_____________________________________________________________")

