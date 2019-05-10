class Human : 
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0
    weight = 0.0

    def get_bmi(self):
        return (self.weight) / (self.height**2)

    #파이썬은 클래스에서 함수를 정의할 때 첫 번째 인수로 키워드 self 를 사용 // 클래스에서 정의한 함수의 첫 번째 인수는 self여야 함

chulsoo = Human()
chulsoo.lastname = '김'
chulsoo.firstname = '철수'
chulsoo.height = 1.8
chulsoo.weight = 80

bmi = chulsoo.get_bmi()
print(bmi)