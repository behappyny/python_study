def game369(i):
    if i % 3 == 0 :
        return '바보'
    elif "3" in str(i) :
        return '3이 포함되어 있다!'
    return i  

result = game369(373)
print(result)