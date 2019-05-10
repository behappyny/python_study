try : 
    with open('test.txt') as file : 
    # with : 처리가 끝나면 자동으로 파일을 닫게 하는 함수
    # finally : file.closer() 필요 없음 
        print(file.read())
except FileNotFoundError as fne : 
    print(fne)