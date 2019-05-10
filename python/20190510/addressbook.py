class Addressbook : 

    #주소록에 등록된 사람 목록
    person_list = []

    def add(self, person):
        self.person_list.append(person)  #append(덧붙이다) : 리스트의 마지막에 새 요소를 추가할 때 사용 
        #신규등록
        pass

    def show_all(self):
        for person in self.person_list:
            print(person.lastname + ' ' + person.firstname)

        #등록된 사람을 목록으로 표시
        pass

    def search(self, keyword):
        for person in self.person_list:
            if keyword in person.firstname or person.lastname:
                #성이나 이름에 키워드가 있다면
                print(person.lastname + ' ' + person.firstname) #출력 
        #검색 조건에 일치하는 사람을 표시
        pass 

#주소록에 등록할 개인 정보를 관리하는 클래스 
class Person : 
    import datetime

    firstname = ' '  #이름
    lastname = ' ' #성
    tel = ' ' #전화번호
    mail_address = '' #메일주소
    birthday = datetime.datetime(2000,1,1) #생년월일 

ab = Addressbook()

p = Person()
p.firstname = '철수'
p.lastname = '김'
p.tel = '010-1234-5678'

ab.add(p)

p2 = Person()
p2.firstname = 'John'
p2.lastname = 'Lennon'
p2.tel = '010-1234-0054'

print('------ 동작확인 ------')
ab.add(p2)

print('주소록에 등록된 사람 수 ->' + str(len(ab.person_list)) + '명')

print('------목록표시------')
ab.show_all()

print('------검색------')
ab.search('John')