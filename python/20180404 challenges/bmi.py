weight = input('몸무게를 kg 단위로 입력해주세요:')
height = input('키를 m 단위로 입력해주세요:')
bmi = float(weight) / (float(height)**2)

if bmi < 18.5 :
    print('말랐다')
elif bmi < 25 :
    print('보통')
elif bmi < 35 : 
    print('약간 뚱뚱하다')
else : 
    print('아주 뚱뚱하다')