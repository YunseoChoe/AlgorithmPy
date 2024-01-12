def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    less_arr = []
    greater_arr = []
    equal_arr = []

    for i in range(len(arr)):
        if arr[i] < pivot:
            less_arr.append(arr[i])
        elif arr[i] > pivot:
            greater_arr.append(arr[i])
        else:
            equal_arr.append(arr[i])
    return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)

n = int(input())

num = [] # 전체 좌표 배열
xy = [] # 각 좌표 배열

for _ in range(n):
    xy = input().split()
    for i in range(len(xy)):
        xy[i] = int(xy[i])
    num.append(xy)

print(num)

# 정렬
num = quick_sort(num)

# 출력
for i in range(len(num)):
    for j in range(len(xy)):
        print(num[i][j], end = " ")
    print()