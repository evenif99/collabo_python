mylist = [10, -20, 30, -40, 50]

total = 0
for i in range(len(mylist)):
    value = mylist[i]
    total += abs(value)

print(total)
# end for

list = [abs(i) for i in mylist]
total = 0
for value in mylist:
    total += abs(value)

print(list)
print(total)