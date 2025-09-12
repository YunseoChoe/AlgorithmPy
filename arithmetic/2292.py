# 벌집

# 2~7     6 (2)
# 8~19    12 (3)
# 20~37   18 (4)
# 38~61   24 (5)
#         30 (6)
#         36 (7)
#         ...

# num = 2
# for i in range(n // 2):
#     print(f'i: {i}')
#     a = num
#     num += 6 * i
#     print(f'a: {a}')
#     print(f'num: {num}')
#     # list에 추가
#     list = []
#     for j in range(a, num):
#         list.append(j)
#     if a <= n <= num:
#         cnt += 1
#     print(f'cnt: {cnt}')
#     print(list)
#     print()

n = int(input()) # (1 <= n <= 1,000,000,000)
i = 0
cnt = 0
beebox = 1 # 해당하는 칸의 최댓값
if n == 1:
    print(1)
else:
    while n > beebox: # 해당하는 칸의 최댓값보다 크면 cnt += 1
        beebox += 6 * i # 최댓값 갱신
        cnt += 1
        i += 1
    print(cnt)