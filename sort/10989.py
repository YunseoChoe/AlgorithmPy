# # 수 정렬하기 3
import sys

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

n = int(sys.stdin.readline())
num = []
for i in range(n):
    a = int(sys.stdin.readline())
    num.append(a)

num = quick_sort(num)
for i in range(len(num)):
    print(num[i])