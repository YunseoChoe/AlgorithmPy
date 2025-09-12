# 좌표 정렬하기
n = int(input())
num = []
x_list = []
y_list = []
for i in range(n):
    num = input().split()
    num[0] = int(num[0])
    num[1] = int(num[1])

    x_list.append(num[0])
    y_list.append(num[1])

xy = []
i = 0
while i != n:
    x_y = []
    x_y.append(x_list[i])
    x_y.append(y_list[i])
    xy.append(x_y)
    i += 1

# 정렬
xy.sort()

# 출력
for i in range(len(xy)):
    for j in range(2):
        print(xy[i][j], end = " ")
    print()