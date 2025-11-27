print('recoding coffees files.')

filename = 'coffee_menu.txt'
coffee_file01 = open(file=filename, mode='wt', encoding='utf-8')
print(type(coffee_file01))

coffees = ['Americano', 'CaffeLatte', 'Capuchino', 'VanillaLatte', 'Mocha']

for coffee in coffees:
    message = f'Todays recommendation is {coffee}\n'
    coffee_file01.write(message)
# end for

coffee_file01.close()

coffee_file02 = open(filename, mode='at', encoding='utf-8')

for idx in range(len(coffees)):
    if idx % 2 == 0:
        message = f'The 1st Coffee {coffees[idx]} has a deep flavor\n'
    else:
        message = f'Having enjoy with creamy flavor with 2nd Coffee {coffees[idx]}\n'
    # end if

    coffee_file02.write(message)
# end for

coffee_file02.close()

for idx in range(1, 6):
    filename = "coffee" + str(idx).zfill(2) + ".txt"
    coffee_file = open(file=filename, mode='wt', encoding='utf-8')
    coffee_file.write(f'It is {filename} file.')
    coffee_file.close()
# end for

coffees = ['Americano', 'CaffeLatte', 'Capuchino', 'VanillaLatte', 'Mocha']

for coffee in coffees:
    filename = coffee + ".txt"
    coffee_file = open(file=filename, mode='wt', encoding='utf-8')
    coffee_file.write('A text file for coffee ' + coffee + ' information')
    coffee_file.close()
# end for

with open(file = 'coffee_test.txt', mode='wt', encoding='utf-8') as testfile:
    testfile.write('checkout\n')
    testfile.write('first\n')
    testfile.write('second\n')

    print('Welcome to the coffee shop!', file = testfile)
# end with


