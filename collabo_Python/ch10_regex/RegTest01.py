import re

print('\n커피 이름 2개 문자 + 숫자 3개로 구성된 항목 찾기')
coffee_list01 = ['am123', 'la456', 'mo789', 'lat12']

regEx = '^[a-zA-Z]{2}[0-9]{3}$'
pattern = re.compile(regEx)

result01 = []

for coffee in coffee_list01:
    if pattern.match(coffee):
        result01.append(coffee)
    # end if
# end for
print('결과 01 : %s' % result01)
print('-'*30)

print('\n"c"로 시작하고 ".coffee"로 끝나며 숫자가 최소 2개 이상 포함된 항목 찾기')
coffee_list02 = ['c1.coffee', 'c12.coffee', 'c345.coffee', 'c9.coffee']

regEx = '^c[0-9]{2,}\.coffee$'
pattern = re.compile(regEx)

result02 = []

for coffee in coffee_list02:
    if pattern.match(coffee):
        result02.append(coffee)
    # end if
# end for
print('결과 02 : %s' % result02)
print('-'*30)


print('\n"c"와 "e" 사이에 "a"가 1번 이상 반복되는 항목 찾기')
coffee_list03 = ['ce', 'cae', 'caae', 'caaae']

regEx = '^c(a){1,}e$'
pattern = re.compile(regEx)

result03 = []

for coffee in coffee_list03:
    if pattern.match(coffee):
        result03.append(coffee)
    # end if
# end for
print('결과 03 : %s' % result03)
print('-'*30)