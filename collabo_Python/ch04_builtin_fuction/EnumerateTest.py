fruits = ['사과', '감', '오렌지', '한라봉', '바나나']

for (idx, value) in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (idx, value) # %d는 decimal값 입력란, %s는 string값 입력란
    print(message) # 인덱스와 내용을 가지고 튜플 형태로 반환
# end for
print('-'*30) # 파이썬에서 문자를 곱하면 그 문자를 곱한 수만큼 반복합니다.

for (idx, value) in enumerate(fruits, start=1): # start=1는 인덱싱을 0이 아닌 1부터 하겠다는 의미입니다.
    message = '%d번째 품목은 \'%s\'입니다.' % (idx, value)
    print(message)
# end for
print('-'*30)

for item in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (item[0], item[1])
    print(message)
# end for
print('-'*30)

print('* 기호는 가변 매개 변수로 인식이 되며, 내부적으로 tuple로 처리됩니다.')
for item in enumerate(fruits):
    # message = '{}번째 값 : {}'.format(item[0], item[1])
    message = '{}번째 값 : {}'.format(*item) # (*item) 이렇게 적용하면 자동적으로 튜플로 인식합니다.
    print(message)
# end for
print('-'*30)