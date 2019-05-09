file = open('test.txt', 'w')
#첫 번째 인수 : 파일 이름, 두 번째 인수 : 쓰기 모드(해당 파일이 있을 때는 원래 내용 삭제, 없으면 파일 생성 후 쓰기 진행) 
file.write('test')
file.close()
#파일에 기록한 데이터를 디스크에 저장 
