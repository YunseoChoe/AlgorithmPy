# 색종이
white_paper = []
for i in range(100):
    row_list = [0] * 100
    white_paper.append(row_list)

# 입력받기
t = int(input())    # 색종이의 수
for _ in range(t):  # 좌표
    num = input().split()
    for i in range(len(num)):
        num[i] = int(num[i])

    x = num[0] # 열
    y = num[1] # 행

    for i in range(x, x + 10): # 열
        for j in range(100 - y - 10, 100 - y): # 행
            white_paper[j][i] = 1

# 넓이 구하기
sum = 0
for i in range(len(white_paper)):
    for j in range(len(white_paper[0])):
        if white_paper[i][j] == 1:
            sum += 1

print(sum)