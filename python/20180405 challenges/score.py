midterm_score = [
[100,58,100],
[90,68,90],
[20,50,70],
[100,100,100],
[65,21,98]
]

# print("a의 평균은 ", (midterm_score[0][0]+midterm_score[0][1]+midterm_score[0][2])/3)
# print("b의 평균은 ", (midterm_score[1][0]+midterm_score[1][1]+midterm_score[1][2])/3)

# a_sum = sum(a_midterm_score, 0.0)
# a_average = a_sum/3
# print(a_average)

# b_sum = sum(b_midterm_score, 0.0)
# b_average = b_sum/3
# print(b_average)

for i in midterm_score:
    print(sum(i, 0.0)/3)