# 세로읽기
# column 초기화
column = []
for i in range(15):
    column.append([])

# column에 추가
for i in range(5):
    num = input()
    for j in range(len(num)):
        column[j].append(num[j])

# 출력
for i in range(15):
    for j in range(len(column[i])):
        # if column[i][j] != None:
        print(column[i][j], end = "")