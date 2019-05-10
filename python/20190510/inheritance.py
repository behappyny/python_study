#클래스의 상속 기능 : 다른 클래스의 기능이나 정보를 이어 받는다

class A:
    name = 'Class A'

class B(A): #Class A를 상속받는다는 의미
    pass

b = B()
print(b.name) #Class A라고 표시된다 