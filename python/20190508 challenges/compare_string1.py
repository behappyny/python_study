def compare_string(a,b):
    if len(a) > len(b):
        return a
    return b

#확인

result = compare_string('aaaaaaa', 'bb')
print(result)