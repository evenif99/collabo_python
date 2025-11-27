filename = 'coffee_list.txt'
myencoding = 'utf-8'

myfile01 = open(file = filename, mode = 'rt' , encoding = myencoding)

while True:
    oneline = myfile01.readline().strip()
    if not oneline:
        print(oneline)
        break
    # end if
    print('[' + oneline + ']')
# end while

myfile01.close()

myfile02 = open(file=filename, mode = 'rt', encoding = myencoding)
sentences = [txt.strip() for txt in myfile02.readlines()]
print(sentences)
print()

myfile02.close()

myfile03 = open(file=filename, mode = 'rt', encoding = myencoding)
sentences = myfile03.read()

print(type(sentences))
print(sentences)
print()

myfile03.close()

print('finished')