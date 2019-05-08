def foo(**kwargs):
    # **은 매개변수 앞, 미리 정의되지 않은 키워드 인수를 전달받는 방법

    print(kwargs)
foo(bar = 'bar', hoge ='hoge', num=999, name='길벗')