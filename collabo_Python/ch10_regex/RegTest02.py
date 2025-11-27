import re

print('===== 커피 데이터에서 숫자 찾기 =====')
coffee_info = '아메리카노 3500원입니다.'
regEx = '\d+'  # 숫자가 1개 이상
pattern = re.compile(regEx)

result = pattern.match(coffee_info)
print('match 결과 : %s' % result)
result = pattern.search(coffee_info)
print('search 결과 : %s' % result)
print(('-'*30))
# match와 search 함수 테스트


print('\n===== 특정 단어로 시작하는 커피 이름 찾기 =====')
print('latte로 시작하는 항목들')
coffee_list = ['latte123', 'mocha99', 'latte_special']
regEx = 'latte[a-z]*[0-9]*'   # latte로 시작하는 항목들
pattern = re.compile(regEx)

print('match 함수 실행 결과')
for coffee in coffee_list:
    if pattern.match(coffee):
        print('%s : True' % coffee)
    else:
        print('%s : False' % coffee)
    # end if

print('search 함수 실행 결과')
for coffee in coffee_list:
    if pattern.search(coffee):
        print('%s : True' % coffee)
    else:
        print('%s : False' % coffee)
    # end if
# match 함수 실행 결과
# search 함수 실행 결과


print('\n===== match 함수의 반환 결과는 Match 객체입니다. =====')
print('알파벳 소문자 또는 _가 1번 이상')
coffee_name = 'espresso_2500'
regEx = '([a-z]|_)+'  # 알파벳 소문자 또는 _가 1번 이상
pattern = re.compile(regEx)
result = pattern.match(coffee_name)

start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {coffee_name[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')


print('\n===== search 함수의 반환 결과 역시 Match 객체입니다. =====')
print('숫자 1번 이상')
order_info = '총 주문 금액은 4800원입니다.'
regEx = '[0-9]+'  # 숫자 1번 이상
pattern = re.compile(regEx)
result = pattern.search(order_info)

start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {order_info[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')
