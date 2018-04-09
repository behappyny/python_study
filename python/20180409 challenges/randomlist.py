import random
def make_random_list1(size):
    result = []
    for i in range(size):
        result.append(random.randint(0,100))
    return result 

result = make_random_list1(10)
print(result)
