# 오븐 시계

# 현재 시간
h, m = input().split()
h = int(h)
m = int(m)
# 요리하는데 필요한 시간 (0 <= c <= 1000)
c = int(input())

# h가 23이 아니면
if h != 23:
    if m + c < 60:
        m = m + c
    else:
        h = h + (m + c) // 60
        if h > 23:
            h = h - 24
        m = (m + c) % 60
# h가 23이면
else:
    if m + c < 60:
        m = m + c
    else:
        h = -1 + ((m + c) // 60)
        m = (m + c) % 60

print(h, m)