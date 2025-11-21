coffees = ['바닐라라떼', '카페라떼', '고구마라떼']
price = [1000, 2000, 3000, 4000]

# zip()
for item in zip(coffees, price):
    print(item)
# end for

mylist = list(zip(coffees, price))
print(mylist) # 원소가 3개이며 각각이 tuple로 되어있는 list

mydict = dict(mylist)
print(mydict) # 원소가 3개이며 각각이 tuple로 되어있는 dict

# sorted()
print('key를 사용한 오름차순 정렬')
result = sorted(mydict.keys())
print(result)

print('key를 사용한 내림차순 정렬')
result = sorted(mydict.keys(), reverse=True)
print(result)

print('value를 사용한 오름차순 정렬')
result = sorted(mydict.values())
print(result)

print('value를 사용한 내림차순 정렬')
result = sorted(mydict.values(), reverse=True)
print(result)

print('value를 사용한 내림차순 정렬하되, 품목 이름 출력')
result = sorted(mydict, key =mydict.get, reverse=True)
print(result)

human = ['김철수', '홍길동', '박영희']
jumsu = [50, 60, 70]

mylist = list(zip(human, jumsu))
print(mylist)

mydict = dict(mylist)
print(mydict)

print('점수가 높은 사람 순부터 이름을 출력')
result = sorted(mydict, key=mydict.get, reverse=True)
print(result)