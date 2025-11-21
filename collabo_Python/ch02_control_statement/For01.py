total = 0
for i in range(1, 10+1):
    total += i
# end for
print('총합01 : %d' % total)

total = 0
for i in range(1, 101, 3):
    total += i
# end for
print('총합02 : %d' % total)

total = 0
for i in range(97, 1, -5):
    total += i
# end for
print('총합03 : %d' % total)

total = 0
for i in range(1, 96+1, 5):
    total += i**2
# end for
print('총합04 : %d' % total)

total = 0
for i in range(1, 5+1):
    total += i*(i+1)
# end for
print('총합05 : %d' % total)