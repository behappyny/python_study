class Human : 
    age = 0 #연령
    lastname = ' ' #성
    firstname = ' ' #이름
    height = 0.0 #신장
    weight = 0.0 #무게


a = Human()
a.age = 30
a.lastname = '김'
a.firstname = '영희'
a.height = 167.5
a.weight = 50.0

print(a.age)
print(a.lastname + ' ' + a.firstname)