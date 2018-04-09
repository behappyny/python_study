def compare_string(a,b):
    if len(a) > len(b):
        return a
    return b


result = compare_string('aaaaa','bbbbbbbbbbb')
print(result)