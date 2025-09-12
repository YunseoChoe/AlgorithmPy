# 너의 평점은
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

sum = 0
score_sum = 0

for i in range(20):
    num = input().split()
    subject = num[0]        # 과목명
    score = float(num[1])   # 학점
    # grade                 # 등급
    if num[2] == 'A+':
        grade = 4.5
    elif num[2] == 'A0':
        grade = 4.0
    elif num[2] == 'B+':
        grade = 3.5
    elif num[2] == 'B0':
        grade = 3.0
    elif num[2] == 'C+':
        grade = 2.5
    elif num[2] == 'C0':
        grade = 2.0
    elif num[2] == 'D+':
        grade = 1.5
    elif num[2] == 'D0':
        grade = 1.0
    elif num[2] == 'F':
        grade = 0.0
    elif num[2] == 'P':
        grade = 0.0
        score = 0

    sum = sum + (score * grade)
    score_sum = score_sum + score

print(round(sum / score_sum, 6))