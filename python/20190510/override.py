#부모 클래스에 있는 기능을 덮어쓰는 것을 '오버라이드'라 함. 변수와 함수 모두 덮어쓸 수 있다

class A : 
    def hello(self): #Class A의 hello 함수
        print('Class A says Hello')

class B(A):
    def hello(self): #Class B의 hello 함수 
        print('Class B says Hello')

b = B()  # Class B 객체 생성 
b.hello() # 객체를 사용해서 hello 함수 호출 

# Class A 와 B는 이름이 같은 hello 함수가 있다. 이때, 이름이 중복되므로 어떤 클래스의 함수를 사용할 지 결정
# 여기서는 B의 객체를 사용했으므로 B에 정의된 hello 함수인 'Class B says Hello'가 출력) 
# 동작은 같지만, 방법이 다를 때 오버라이드를 사용하면 편리하다 