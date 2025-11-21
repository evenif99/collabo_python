# list comprehension을 활용한 문제
# 평균 이상 점수를 받은 학생 수 출력하기 sum, len 사용
scores = [55, 80, 92, 45, 68, 88]  # 평균 이상이면 '우수'
avg = sum(scores) / len(scores)
mylist01 = [one for one in scores if one >= avg]
print(mylist01)
print(f'평균 이상 학생 수 : {len(mylist01)}명')

# 나이가 18세 이상인 사람만 추출하여 몇 명인지 출력
ages = [12, 17, 18, 20, 35, 15]
mylist02 = [one for one in ages if one >= 18]
print(mylist02)
print(f'성인 인원 : {len(mylist02)}명')

# 양수만 골라서 개수 출력하기
numbers = [-5, 3, 0, 7, -2, 10, -8]
mylist03 = [one for one in numbers if one > 0]
print(mylist03)
print (f'양수 개수 : {len(mylist03)}개')

# 짝수만 골라서 출력 및 개수 표시
data = [1, 4, 7, 10, 13, 16]
mylist04 = [one for one in data if one%2 == 0]
print(mylist04)
print(f'짝수 개수 : {len(mylist04)}개')

# 이름 리스트에서 3글자 이상인 이름만 추출
names = ["유나", "철수", "민지", "Tom", "Ann", "Jennifer"]
mylist05 = [one for one in names if len(one) >= 3]
print(mylist05)
print(f'3글자 이상 이름 수 : {len(mylist05)}명')
