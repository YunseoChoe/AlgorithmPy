# 분해합
# n = int(input())

# sum = 0
# constructor = 0
# min = []
# for i in range(0, 10):
#     for j in range(0, 10):
#         for k in range(0, 10):
#             constructor = int(str(i) + str(j) + str(k))
#             if constructor + i + j + k == n:
#                 # print(f'consturctor: {constructor}')
#                 # print(f'i: {i}')
#                 # print(f'i: {j}')
#                 # print(f'i: {k}')
#                 # print(f'constructor + i + j + k: {constructor + i + j + k}')
#                 min.append(constructor)

# # 생성자가 없는 경우 
# if not min:
#     print(0)

# else:
#     print(min[0])

n = int(input())

for num in range(n):
    # num -> 문자열
    num = str(num)
    
    # num의 각 자릿수 합 구하기
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    
    number = int(num) + sum
    # 가장 작은 생성자를 만나면 출력하고 종료
    if number == n:
        print(num)
        break

# 생성자가 없을 때
else:
    print(0)