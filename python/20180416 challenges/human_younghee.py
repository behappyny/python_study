class Human:
    age = 0 #연령
    lastname = ' ' #성
    firstname = ' ' #이름
    height = 0.0
    weight = 0.0

younghee = Human()
younghee.age = 35
younghee.lastname = '이'
younghee.firstname = '영희'
younghee.height = 157.2
younghee.weight = 44.5

if(younghee.age >= 35 and younghee.firstname == '영희'):
    print('선택된 사람->' + younghee.lastname + ' ' + younghee.firstname)