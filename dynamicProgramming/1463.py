# 1로 만들기
n = int(input())

# dp배열 초기화
dp = []
dp.append(0)
dp.append(0)
dp.append(1)
dp.append(1)
for i in range(n - 3):
    dp.append(0) 

for i in range(4, n + 1):
    is_false_1 = False
    is_false_2 = False
    # 2로 나눠질 경우
    if i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        min_a = dp[i]
        is_false_1 = True

    # 3로 나눠질 경우
    if i % 3 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 3] + 1)
        min_b = dp[i]
        is_false_2 = True

    # 둘 다 아닐 경우
    if is_false_1 == False and is_false_2 == False:
        dp[i] = dp[i - 1] + 1
    
    # 둘 다 맞을 경우
    if is_false_1 and is_false_2:
        dp[i] = min(min_a, min_b)

print(dp[n])
