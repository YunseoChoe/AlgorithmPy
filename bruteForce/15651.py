# N과 M(3)
n, m = map(int, input().split())

arr = []
def func():
    if len(arr) == m:
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
        return
    for i in range(1, n + 1):
        arr.append(i)
        func()
        arr.pop()

func()