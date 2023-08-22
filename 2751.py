# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#     less_arr = []
#     greater_arr = []
#     equal_arr = []
#     pivot = arr[-1]
#     for i in range(len(arr)):
#         if arr[i] < pivot:
#             less_arr.append(arr[i])
#         elif arr[i] > pivot:
#             greater_arr.append(arr[i])
#         else:
#             equal_arr.append(arr[i])

#     return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    m = len(arr) // 2 # 가운데 값
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])

    merge_arr = []
    l = h = 0
    while l < len(L) and h < len(R):
        if L[l] < R[h]:
            merge_arr.append(L[l])
            l += 1
        else:
            merge_arr.append(R[h])
            h += 1

    if l < len(L):
        merge_arr += L[l:]
    if h < len(R):
        merge_arr += R[h:]
    return merge_arr

n = int(input())
num = []

for i in range(n):
    a = int(input())
    num.append(a)

num = merge_sort(num)
for i in range(len(num)):
    print(num[i])

