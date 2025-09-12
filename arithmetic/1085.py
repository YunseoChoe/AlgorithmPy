# 직사각형에서 탈출
x, y, w, h = map(int, input().split())

# (x, y)에서 4개의 길이를 비교
list = []
# 왼쪽
list.append(x - 0)
# 위
list.append(h - y)
# 오른쪽
list.append(w - x)
# 아래
list.append(y - 0)

# 최솟값
min = list[0]
for i in range(len(list)):
    if min > list[i]:
        min = list[i]

print(min)