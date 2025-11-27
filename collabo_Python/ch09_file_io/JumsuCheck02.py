myencoding = 'utf-8'

source = open(file = 'jumsu.txt', mode='rt', encoding=myencoding) # 읽어올 파일
destination = open(file='result.txt', mode='wt', encoding=myencoding) # 신규 생성할 파일

data = [item.strip() for item in source.readlines()]
print(data)

for bean in data:
    # print(type(bean))
    human = bean.split(',') # split 사용 시 원래 리스트 각 객체를 다시 나누어진 리스트로 제공
    # print(human)
    name = human[0]
    _gender = human[4].upper() # lower() 함수도 참고

    kor = float(human[1])
    eng = float(human[2])
    math = float(human[3])

    total = kor+eng+math
    average = total/3

    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'
    # end if

    # 표시 형식 : '이름/성별/총점/평균'
    sentences = '%s/%s/%.1f/%.2f\n' % (name, gender, total, average)
    print(sentences) # 출력이 잘못 되었을 때 1. 원본 데이터를 확인 2. 코딩을 확인
    # print(f'이름 : {name}\n성별 : {gender}\n국어 : {kor}\n영어 : {eng}\n수학 : {math}\n총점 : {total}\n평균: {average:.2f}')

    destination.write(sentences)
    # or print(sentences, file=destination) 사용해도 되지만 \n의 적용이 달라질 수 있음을 유의

# end for

source.close()
destination.close()

print('처리 작업이 완료 되었습니다.')