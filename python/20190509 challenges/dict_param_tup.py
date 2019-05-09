def foo(*args):
#인수를 받는 매개변수 앞에 *을 붙여 원하는 만큼 인수 출력
#인수를 뜻하는 arguments를 줄여, args로 표기하는 것이 관례 

    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(args[4])

foo('a', 'b', 'c', 'd', [1,2,3])