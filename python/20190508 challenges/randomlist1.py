import random
#숫자를 무작위로 만드는 함수, randint // 사용을 위해선 import문으로 외부 프로그램 random을 불러와야 함 
def make_random_list1(size):
    result = []

    for v in range(size):
        result.append(random.randint(0,100))
    return result 

#확인

result = make_random_list1(10)
print(result)

result = make_random_list1(20)
print(result)