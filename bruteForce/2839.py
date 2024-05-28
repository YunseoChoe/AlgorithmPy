# 설탕 배달 
n = int(input())

# 5로 나누어 떨어질 때
if n % 5 == 0:
    print(n // 5)

# 5로 나누어 떨어지지 않을 때
# n을 계속 3씩 뺌
else:
    cnt = 0
    while n > 0:
        n -= 3
        cnt += 1
        # 5로 나누어 떨어질 때
        if n % 5 == 0:
            cnt += (n // 5)
            print(cnt)
            break
        # n이 0이면 (3으로 나눠 떨어짐)
        if n == 0:
            print(cnt)
        # n이 1, 2이면 (5, 3 모두 나눠 떨어지지 않음)
        elif 0 < n < 3:
            print(-1)