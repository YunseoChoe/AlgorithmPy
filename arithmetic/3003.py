# 킹, 퀸, 룩, 비숍, 나이트, 폰
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
original = [1, 1, 2, 2, 2, 8]
subtract = []
# 입력받기
num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
    subtract.append(original[i] - num[i])

# 출력하기
for i in range(len(subtract)):
    print(subtract[i], end = " ")