import re
# 메타문자 치트시트 -> 이론문서 p.211~212

print('알파벳 3개 + 숫자 2개로 구성되어 있는 항목 확인')
mylist01 = ['abc12', 'abcd12', 'xy345', 'pq678', 'abcd1']

# ^와 $를 명시하면 전체 완전 일치, 명시하지 않으면 부분 일치하는 문자열을 확인합니다.
regEx = '^[a-zA-Z]{3}[0-9]{2}$' # 정규 표현식을 적용할 때는 띄어쓰기나 콤마 없이 나열해야 합니다.
pattern = re.compile(regEx)
# print(type(pattern)) <class 're.Pattern'>

result01 = [] # 결과를 저장할 리스트

for item in mylist01:
    if pattern.match(item): # 조건에 충족하면
        result01.append(item)
    # end if
# end for
print('결과01 : %s' % result01)
print('-'*30)

print('file + 영문자 최소 2개 이상 + .png') # 데이터 처리 가공 시 사용
print('주의 : 점(.)은 임의의 한 문자(줄바꿈 제외), (\.)은 .기호를 의미합니다.') # 데이터 처리 가공 시 사용
mylist02 = ['filea.png', 'fileab.png', 'fileabc.png', 'file.png', 'file99.png', 'filexyzXpng']

regEx = '^file[a-zA-Z]{2,}\.png$'
pattern = re.compile(regEx)

result02 = []

for item in mylist02:
    if pattern.match(item):
        result02.append(item)
    # end if
# end for
print('결과02 : %s' % result02)
print('-'*30)

def extract_by_regex(data, regExpr):
    # 정규식 regExpr를 사용하여 data에서 조건을 충족하는 항목만 리스트로 반환해 줍니다.
    pattern = re.compile(regExpr)
    result = []
    for bean in data:
        if pattern.match(bean):
            result.append(bean)
        # end if
    # end for

    return result
# end def

print('패턴을 함수로 제작하여 적용하기')
print('b로 시작하고, g로 끝나는데 둘 사이에 e가 2번 이상 반복')
mylist03 = ['beg', 'beeg', 'beeeg', 'bg']

regEx = '^b(e){2,}g$'
result03 = extract_by_regex(mylist03, regEx)
print('결과03 : %s' % result03)
print('-'*30)

print('숫자로 시작(0 제외)하고, 이후에 알파벳이 1개 이상인 항목')
mylist04 = ['1a', '2abc', '9xyz', '0ab']

regEx = '^[1-9][a-zA-Z]+$' # + 기호는 최소 1번 이상
result04 = extract_by_regex(mylist04, regEx)
print('결과04 : %s' % result04)
print('-'*30)

print('hello 또는 hi로 시작하는 항목들 찾기')
mylist05 = ['hello123', 'hi99', 'hey77', 'hello']

regEx = '^(hello|hi).*$' # hello, hi
result05 = extract_by_regex(mylist05, regEx)
print('결과05 : %s' % result05)
print('-'*30)