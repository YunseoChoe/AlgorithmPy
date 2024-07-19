import copy
# from itertools import permutations

# 연산자 끼워넣기
n = int(input())
num = map(int, input().split())
num = list(num)
operator = map(int, input().split())
operator = list(operator)

op = [] # 연산자 배열
operators = ['+', '-', '*', '/']
for i in range(len(operator)):
    if operator[i] != 0:
        op.append(operators[i] * operator[i])

p = [] # 연산자 순열 배열

# 순열 재귀 함수 (DFS)
arr = []
def func():
    if len(arr) == (n - 1):
        # p.append(arr)
        p.append(copy.deepcopy(arr))
        return
    
    for i in range(n - 1):
        if i not in arr:
            arr.append(i)
            func()
            arr.pop()

func()

# p을 연산자로 변경
for i in range(len(p)):
    for j in range(len(p[0])):
        p[i][j] = op[p[i][j]]

# print(list(permutations(op, n - 1)))

results = [] # 각 계산 결과를 저장하는 배열


for i in range(len(p)):
    for j in range(len(p[0])):
        k = 0
        calculate = [0] * (len(num) + len(p))
        for l in range(len(calculate)):
            # 짝수자리면 num 넣기
            if l % 2 == 0: 
                calculate[l] = num[k]
                k += 1
            # 홀수자리면 p 넣기
            else:
                calculate[l] = p[i][j]
    results.append(calculate)

print(results)



# import copy

# # 입력 처리
# n = int(input())
# num = list(map(int, input().split()))
# operator = list(map(int, input().split()))

# # 연산자 배열 생성
# op = []  # 연산자 배열
# operators = ['+', '-', '*', '/']
# for i in range(len(operator)):
#     if operator[i] != 0:
#         op.extend([operators[i]] * operator[i])

# # 연산자 순열 배열 생성
# p = []  # 연산자 순열 배열

# def func(arr):
#     if len(arr) == (n - 1):
#         p.append(copy.deepcopy(arr))
#         return
    
#     for i in range(n - 1):
#         if i not in arr:
#             arr.append(i)
#             func(arr)
#             arr.pop()

# func([])

# # p을 연산자로 변경
# for i in range(len(p)):
#     for j in range(len(p[0])):
#         p[i][j] = op[p[i][j]]

# # 각 계산 결과를 저장하는 배열
# results = []

# for operators in p:
#     calculate = []
#     k = 0
#     for i in range(len(num) + len(operators)):
#         if i % 2 == 0:
#             calculate.append(num[k])
#             k += 1
#         else:
#             calculate.append(operators[(i - 1) // 2])
    
#     results.append(calculate)

# print("모든 계산 결과:", results)
