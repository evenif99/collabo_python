odd, even = 0, 0 # 튜플은 괄호 생략 후 ,로 각 변수 값 지정

i = 1
while i < 11:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    # end if

    i += 1
# end while

print('홀수의  총합 : %d' % odd)
print('짝수의  총합 : %d' % even)