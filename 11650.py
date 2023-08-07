# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#     pivot = arr[-1]
#     less_arr = []
#     greater_arr = []
#     equal_arr = []

#     for i in range(len(arr)):
#         if arr[i] < pivot:
#             less_arr.append(arr[i])
#         elif arr[i] > pivot:
#             greater_arr.append(arr[i])
#         else:
#             equal_arr.append(arr[i])
#     return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)

n = int(input())

num = [] # 전체 좌표 배열
xy = [] # 각 좌표 배열

for _ in range(n):
    xy = input().split()
    for i in range(len(xy)):
        xy[i] = int(xy[i])
    num.append(xy)

num.sort()

for i in range(len(num)):
    for j in range(len(xy)):
        print(num[i][j], end = " ")
    print()

# x_sort = [] 
# y_sort = []

# n = int(input())

# for i in range(n):
#     num = input().split()
#     for j in range(len(num)):
#         num[j] = int(num[j])
#     x_sort.append(num[0])
#     y_sort.append(num[1])

# # 정렬
# x_sort = quick_sort(x_sort)
# y_sort = quick_sort(y_sort)

# # 출력
# print('출력')
# for i in range(n):
#     print(x_sort[i], y_sort[i])