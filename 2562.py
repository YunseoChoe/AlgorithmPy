# 최댓값
index = 0
max = 1
for i in range(9):
    num = int(input())
    # 최댓값 찾기
    if num > max:
        max = num
        index = i + 1

print(max)
print(index)