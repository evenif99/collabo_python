import json

filename = 'humans.json'

myfile = open(file=filename, mode='rt', encoding='utf-8')
mystring = myfile.read()
print(type(mystring))
myfile.close()

print('loads 함수는 문자열을 읽어서 dict 타입으로 변환해 줍니다.')
jsonData = json.loads(mystring)
print(type(jsonData))
print(jsonData)

memberList = dict()

for one in jsonData:
    name = one['name']
    hobby = one['hobby']
    address = one['address']
    blood = one['blood']
    ssn = one['ssn']
