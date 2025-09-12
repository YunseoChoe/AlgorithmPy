# 평균
n = int(input()) # 시험 본 과목의 개수
scores = input().split()
max = 0
for i in range(n):
    scores[i] = int(scores[i])
    # 최댓값 찾기
    if max < scores[i]:
        max = scores[i]

# 점수 변경
for i in range(n):
    scores[i] = scores[i] / max * 100

# 평균 출력
sum = 0
for i in range(n):
    sum = sum + scores[i]

print(sum / n)