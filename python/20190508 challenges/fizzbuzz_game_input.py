a = input('숫자를 입력해주세요')
# input()은 소괄호 안의 내용을 화면에 표시하고 사용자가 입력한 내용을 문자열로 받는 것 

a = int(a)
# 문자열을 숫자열로 변환하기 위해 필요한 함수 
if a % 15 == 0:
    print('FizzBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')