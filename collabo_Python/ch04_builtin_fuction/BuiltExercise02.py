human = ['김철수', '홍길동', '박영희', '심수련', '유재민']

result = []

for idx, value in enumerate(human):
    if idx % 2 == 0:
        result.append(value)

print(result)
# end for

result = [value + '님' for idx, value in enumerate(human) if idx % 2 == 0]
print(result)