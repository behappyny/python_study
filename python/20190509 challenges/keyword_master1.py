def get_sum(**kargs):
    #인수 앞에 **는 키워드 인수 
    start = kargs['start']
    end = kargs['end']
    #'start'와 'end'는 인수에서 저장한 키워드 
    result = 0
    for v in range(start, end + 1):
        result += v
    return result 

val = get_sum(start = 1, end = 10)
print(val)

#반복하며 익히기 