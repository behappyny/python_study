a = input('숫자를 입력해주세요')
a = int(a)

if a % 15 == 0:
    print ('fizbuzz')
elif a % 3 == 0:
    print('fizz')
elif a % 5 == 0:
    print('buzz')
else :
    print(a)