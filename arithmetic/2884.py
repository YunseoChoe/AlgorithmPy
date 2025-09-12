# 알람 시계
h, m = input().split()
h = int(h)
m = int(m)

# h가 1 이상일 때
if h >= 1:
    if m >= 45:
        m = m - 45
    else:
        h = h - 1
        m = (60 - (45 - m))
# h가 0일 때
else:
    if m >= 45:
        m = m - 45
    else:
        h = 23
        m = (60 - (45 - m))

print(h, m)