import copy
from itertools import permutations

# 연산자 끼워넣기
n = int(input())
num = map(int, input().split())
num = list(num)
operator = map(int, input().split())
operator = list(operator)

op = [] # 연산자 배열
operators = ['+', '-', '*', '/']
for i in range(len(operator)):
    for j in range(operator[i]):
        op.append(operators[i])

p = [] # 연산자 순열 배열

# 순열 재귀 함수 (DFS)
# arr = []
# def func():
#     if len(arr) == (n - 1):
#         # p.append(arr)
#         p.append(copy.deepcopy(arr))
#         return
    
#     for i in range(n - 1):
#         if i not in arr:
#             arr.append(i)
#             func()
#             arr.pop()

# func()

# p를 연산자로 변경
# for i in range(len(p)):
#     for j in range(len(p[0])):
#         p[i][j] = op[p[i][j]]

list_p = list(set(permutations(op, n - 1))) # 중복 순열 제거
results = [] # 각 계산 결과를 저장하는 배열
sum_list = [] # 각 sum을 저장하는 배열

# 각 순열에 대한 조합 찾기
for i in range(len(list_p)):
    # calculate 배열 초기화
    calculate = [0] * (len(num) + len(op))
    odd = 0 # num 인덱스
    even = 0 # p 인덱스
    for j in range(len(calculate)):
        # j가 짝수면 숫자
        if j % 2 == 0:
            calculate[j] = num[odd]
            odd += 1
        # j가 홀수면 연산자
        else:
            calculate[j] = list_p[i][even]
            even += 1
    results.append(calculate) 

    # sum 구하기
    sum = calculate[0]
    for j in range(1, len(calculate) - 1):
        # 더하기
        if calculate[j] == '+':
            sum += calculate[j + 1]
        # 빼기
        elif calculate[j] == '-':
            sum -= calculate[j + 1]
        # 곱하기
        elif calculate[j] == '*':
            sum *= calculate[j + 1]
        # 나누기
        elif calculate[j] == '/':
            sum = int(sum / calculate[j + 1])

    sum_list.append(sum)

print(max(sum_list))
print(min(sum_list))
