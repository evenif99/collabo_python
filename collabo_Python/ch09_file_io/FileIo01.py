print('recoding files.')

filename = 'mem.txt'
myfile01 = open(file=filename, mode='wt', encoding='utf-8')
print(type(myfile01))

members = ['James', 'Park', 'Grace', 'Andy']

for mem in members:
    message = f'Hello {mem}\n'
    myfile01.write(message)
# end for

myfile01.close() # close 작업을 진행하지 않으면 메모리에만 작업사항 저장되고 하드디스크에는 적용되지 않음

print(f'{filename} file generated')

print('add data in origin file.')
# at : 파일 마지막단에 새로운 파일이나 내용을 추가합니다.
myfile02 = open(file=filename, mode='at', encoding='utf-8')

for idx in range(len(members)):
    if idx % 2 == 0:
        message = f'Hello {members[idx]}, you are {idx}th cumstomer.\n'
    else:
        message = f'Welcome {members[idx]}, you are {idx}th cumstomer.\n'
    # end if

    myfile02.write(message)
# end for

myfile02.close()

print('make several files using repeat sentence')
print('filename : somefile01.txt ~ somefile10.txt')
for idx in range(1, 11):
    filename = "somefile" + str(idx).zfill(2) + ".txt"
    # print(filename)
    myfile = open(file=filename, mode='wt', encoding='utf-8')
    myfile.write(f'It is {filename} file.')
    myfile.close()
# end for

print('make a file using the names of members.')
members = ['James', 'Park', 'Grace', 'Andy']

for mem in members:
    filename = mem + ".txt"
    myfile = open(file=filename, mode='wt', encoding='utf-8')
    myfile.write('A text file for customer ' + mem)
    myfile.close()
# end for

print('Using the with syntax, the close() function is implicitly called.')
with open(file='test.txt', mode='wt', encoding='utf-8') as testfile: # with 구문을 사용하면 close() 함수 호출 불필요
    testfile.write('start phrase\n')
    testfile.write('abc\n')
    testfile.write('123\n')

    print('Hello world', file=testfile)
# end with