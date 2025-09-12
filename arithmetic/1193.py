# 분수찾기
n = int(input())

# 1. n이 몇 번째 줄에 있는지 알아내기
line = 1 # 대각선으로 몇 번째 줄에 있는지
line_max = 1 # line에서 최댓값

while n > line_max:
    line += 1
    line_max += line

# print(f'line_max: {line_max}')
# print(f'line: {line}')

# 2. 짝수인지, 홀수인지 나누고 해당 줄에서 첫번째 분수 값 알아내고 while문 돌면서 분수 조작하기
line_min = line_max - line + 1 # line에서 최솟값
gap = n - line_min # line에서 n과 line_min의 차이

# line이 짝수라면
if line % 2 == 0:
    boonja = line
    boonmo = 1 
    while gap != 0:
        # 분자 -= 1, 분모 += 1
        boonja -= 1
        boonmo += 1
        gap -= 1

# line이 홀수라면
else:
    boonmo = line
    boonja = 1
    while gap != 0:
        # 분자 += 1, 분모 -=1
        boonja += 1
        boonmo -= 1
        gap -= 1

print(str(boonmo) + "/" + str(boonja))