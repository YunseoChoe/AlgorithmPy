# N과 M(1)
n, m = map(int, input().split())

arr = []
def func(): # 재귀 함수
    if len(arr) == m:
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
        return
    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            func()
            arr.pop()

func()