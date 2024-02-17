# 대지
n = int(input())
x_min = 10000
x_max = -10000
y_min = 10000
y_max = -10000 
for i in range(n):
    x, y = map(int, input().split())
    # x,y min/max 구하기 (-10,000 이상 10,000 이하)  
    if x_min > x:
        x_min = x
    if x_max < x:
        x_max = x
    if y_min > y:
        y_min = y
    if y_max < y:
        y_max = y

# 밑면, 높이 구하기
under = x_max - x_min
high = y_max - y_min

# 넓이 구하기
s = under * high

print(s)