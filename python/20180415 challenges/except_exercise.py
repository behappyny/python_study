def test(idx): 
    try: 
        abc = ['a','b','c']
        print(abc[idx])
    except IndexError as ie:
       print('인덱스가 범위를 벗어났습니다')


test(10)
