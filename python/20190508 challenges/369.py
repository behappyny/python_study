def game369(v):
    if v % 3 == 0 :
        return '바보'
    elif "3" in str(v) : 
        return '바보'
    return v

#확인

result = game369(3)
print(result)

result = game369(12)
print(result)

result = game369(33)
print(result)