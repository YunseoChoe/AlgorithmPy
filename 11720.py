# 숫자의 합
# 입력받기
n = int(input())
string = input() # 문자열로 입력
string_list = []

# 문자열 -> list
for i in range(len(string)):
    string_list.append(string[i])

# 정수화
for i in range(n):
    string_list[i] = int(string_list[i])

# 합 구하기
sum = 0
for i in range(n):
    sum = sum + string_list[i]

# 출력하기
print(sum)