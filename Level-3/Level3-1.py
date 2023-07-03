'''
10.Build a countdown calculator. Write some code that can take two dates as input, and
then calculate the amount of time between them
'''
start=input("Enter first Year  dd/mm/yy >>") ;end=input("Enter secound Year . dd/mm/yy >>")
start=start.split("/") ; end=end.split("/")
difference={'Day':int(end[0]) - int(start[0]),'Month':int(end[1])-int(start[1]),'year':int(end[-1])-int(start[-1])}
print(difference)
