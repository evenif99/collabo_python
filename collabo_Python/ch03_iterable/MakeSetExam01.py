coffees = set()

coffees.add('아메리카노')
coffees.add(100)
coffees.add(True)
coffees.add('아메리카노') # 같은 데이터를 중복해서 넣으면 데이터 개수는 1개로 치부합니다.

coffees.clear()

coffees.add('아메리카노')
coffees.add('에스프레소')
coffees.add('믹스커피')
coffees.add('카페라떼')

newItems = ['콜드브루', '고구마라떼', '디카페인커피']
coffees.update(newItems) # list같은 여러 정보를 추가하는 경우에는 update 사용

# 집합은 순서가 없으므로, 인덱싱/슬라이싱 불가능
# print(coffees[3])

findItem = '카푸치노'
boolean = findItem in coffees
print(f'{findItem} 존재여부 : {boolean}') # fstring

findItem = '마키아또'
if not findItem in coffees:
    coffees.add(findItem)
# end if

findItem = '믹스커피'
coffees.remove(findItem)

try:
    findItem = '바닐라라떼'
    coffees.remove(findItem)
except KeyError:
    print(f'{findItem}은(는) 목록에 존재하지 않습니다.')
# end try

# discard 메소드는 존재하지 않더라고 예외 없이 넘어갑니다.
coffees.discard('바닐라라떼')

#  집합은 순서가 없으므로, 어떤 데이터가 나올지는 예측할 수 없습니다.
popItem = coffees.pop()
print('pop()으로 제거된 요소 : ', popItem)

print('반복문을 사용한 출력')
for element in coffees:
    print(element)
# end for

print('자료형 타입 : ', end = '')
print(type(coffees))
print('요소 개수 : %d' % len(coffees))
print(coffees)

print('집합 연산')
store01 = set(['고구마라떼', '에스프레소', '아메리카노', '마키아또'])
store02 = set(['아메리카노', '마키아또', '카페라떼', '디카페인커피'])

print('첫번째 매장 품목 : %s' % store01)
print('두번째 매장 품목 : %s' % store02)

print('매장에서 판매 가능한 품목')
union_set = store01.union(store02)
print('합집합01 : %s' % union_set)

union_set = store01 | store02 # | 기호로 합집합 확인 가능
print('합집합02 : %s' % union_set)

print('두 매장에서 공통적으로 판매하는 품목')
intersection_set = store01.intersection(store02)
print('교집합01 : %s' % intersection_set)

intersection_set = store01 & store02 # & 기호로 교집합 확인 가능
print('교집합01 : %s' % intersection_set)

print('첫번째 매장에서만 판매하는 품목')
difference_set = store01.difference(store02)
print('차집합01 A-B : %s' % difference_set)

difference_set = store01 - store02 # - 기호로 차집합 확인 가능
print('차집합02 A-B : %s' % difference_set)

print('하나의 매장에서만 판매하는 품목들의 총합')
symmetric_difference_set = store01.symmetric_difference(store02)
print('차집합들의 합집합 : %s' % symmetric_difference_set)

symmetric_difference_set = store01 ^ store02 # ^기호로 각 차집합들의 합집합을 확인 가능
print('차집합들의 합집합 : %s' % symmetric_difference_set)

print('부분 연산')
super_set = set(['고구마라떼', '에스프레소' ,'아메리카노' ,'마키아또'])
sub_set_01 = set(['아메리카노' ,'마키아또']) # super_set의 부분집합
sub_set_02 = set(['바닐라라떼' ,'마키아또'])

boolean = sub_set_01.issubset(super_set)
if boolean:
    print('집합01은 슈퍼 집합의 부분 집합입니다.')
else:
    print('집합01은 슈퍼 집합의 부분 집합이 아닙니다.')
# end if

boolean = sub_set_02.issubset(super_set)
if boolean:
    print('집합02은 슈퍼 집합의 부분 집합입니다.')
else:
    print('집합02은 슈퍼 집합의 부분 집합이 아닙니다.')
# end if

boolean = super_set.issuperset(sub_set_01)
if boolean:
    print('super_set은 sub_set_01의 상위 집합입니다')
else:
    print('super_set은 sub_set_01의 상위 집합이 아닙니다')
# end if

boolean = super_set.issuperset(sub_set_02)
if boolean:
    print('super_set은 sub_set_02 상위 집합입니다')
else:
    print('super_set은 sub_set_02 상위 집합이 아닙니다')
# end if