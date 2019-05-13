def import_data(self, file):
    import csv
    import datetime

    with open(file. 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) #헤더가 있으면 건너뛰기 

        for row in reader : 
            #row에 데이터가 한 줄씩 할당됩니다.

            p=Person()
            p.lastname = row[0]
            p.firstname = row[1]
            p.mail_address =row[2]

            #날짜 문자열로부터 날짜 타입 데이터 생성
            p. birthday = datetime.datetime.strptime(row[3], "%Y/%m/%d")
            p.tel = row[4]

            self.person_list.append(p)