import sys

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

n = int(sys.stdin.readline())
num = []

for i in range(n):
    a = int(sys.stdin.readline())
    num.append(a)

num = merge_sort(num)
for i in range(len(num)):
    print(num[i])