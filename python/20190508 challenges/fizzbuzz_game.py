a = 30
if a % 3 == 0:
    print('Fizz')
    # 배수란, 나누어 떨어지는 수. 3으로 나눠서 나머지가 0이면 3의 배수
    # 조건문 작성시 판정 순서에 유의할 것. 
elif a % 5 == 0:
    print('Buzz')
    # elif : ~는 아니지만, ~라면 
elif a % 15 == 0:
    print('FizzBuzz')
else:
    print('a')