# 좌표 정렬하기 2
'''
n = int(input())
num = []
for i in range(n):
    xy = []
    x, y = input().split()
    x = int(x)
    y = int(y)
    xy.append(x)
    xy.append(y)
    num.append(xy)

# x를 기준으로 정렬
# num.sort(key = lambda x: (x[1], x[0]))
# print(num)

num.sort()

for y, x in num:
    print(x, y)
'''

n = int(input())
num = []
for i in range(n):
    num_array = []
    a, b = map(int, input().split())
    num_array.append(a)
    num_array.append(b)
    num.append(num_array)



