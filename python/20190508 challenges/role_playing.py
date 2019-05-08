import random

#자신의 HP(에너지)
my_hit_point = 15

#몬스터의 HP(에너지)
monster_hit_point = 8

#공격순서
#자신이 먼저 공격한다고 가정
index = 0
#둘 중 하나의 HP가 0이 될 때까지 싸운다
#HP가 0이하가 되면 반복을 종료한다
while monster_hit_point > 0 and my_hit_point > 0:
    #랜덤으로 피해정도를 결정
    attack = random.randint(1,7)
    #자신과 몬스터가 서로 공격
    if index % 2 ==0:
        print('몬스터에게' +str(attack) + '의 피해를 입혔다')
        monster_hit_point -= attack 
        # -=연산자의 예 (a -= b 라면, a = a - b)
    else:
        print('주인공에게' + str(attack) + '의 피해를 입혔다')
        my_hit_point -= attack
    index += 1 

    #while을 빠져나오면 둘 중 하나가 죽은 것
    #자신의 HP가 남아 있으면 몬스터 격파!
    if my_hit_point > 0:
        print('몬스터를 격파했다')
    else: 
        print('주인공을 죽였다')
