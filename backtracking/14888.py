# 연산자 끼워넣기
import copy
from itertools import permutations

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

# p = [] # 연산자 순열 배열

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

while len(list_p) != 0:
    operator = list_p.pop()
    # 합 구하기
    sum = num[0]
    for i in range(1, len(num)):
        # 더하기
        if operator[i - 1] == '+':
            sum += num[i]
        # 빼기
        elif operator[i - 1] == '-':
            sum -= num[i]
        # 곱하기
        elif operator[i - 1] == '*':
            sum *= num[i]
        # 나누기
        else:
            sum = int(sum / num[i])
    
    results.append(sum)

print(max(results))
print(min(results))
