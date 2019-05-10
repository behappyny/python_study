class Human : 
    age = 0 #연령
    lastname = ' ' #성
    firstname = ' ' #이름
    height = 0.0 #신장
    weight = 0.0 #무게

younghee = Human()
younghee.age = 30
younghee.lastname = '김'
younghee.firstname = '영희'
younghee.height = '165.0'
younghee.weight = 47.2

if (younghee.age >= 30 and younghee.firstname == '영희'):
    print('선택된 사람 ->' + younghee.lastname + ' ' + younghee.firstname)