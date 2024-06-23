# N과 M(2)
n, m = map(int, input().split())

arr = []
def func(prev):
    if len(arr) == m:
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
        return
    for i in range(prev, n + 1):
        if i not in arr:
            arr.append(i)
            func(i + 1)
            arr.pop()

func(1)