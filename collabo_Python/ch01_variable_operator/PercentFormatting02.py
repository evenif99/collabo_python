name = '김철수'
fruit = '사과'
gaesu = 8

myformat = '%s이(가) %s를 %d개 먹었습니다.'
print(myformat % (name, fruit, gaesu))

su01 = 4
su02 = 9
result = su01 * su02
print('%d 곱하기 %d는 %d입니다.' % (su01, su02, result))

a = 2.0
b = 3.0
# pow(a, b)는 a의 b제곱을 해주는 내장 함수입니다.
result = pow(a, b) # a ** b
print('%f의 %f 제곱은 %f입니다.' % (a, b, result))

print('%를 표현하려면 %%를 표시해야 합니다.')
rate = 0.4567
print('비율 : %f%%' % (100*rate))

su03 = -5
print('원본 : %d, 절대 값 : %d' % (su03, abs(su03)))