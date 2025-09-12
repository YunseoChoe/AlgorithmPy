# N과 M(3) 복습
n, m = map(int, input().split())

all_arr = []
arr = []
def func():
    global all_arr
    if len(arr) == m:
        # 출력
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
        return
    
    for i in range(1, n + 1): # 원소는 1부터
        # 원소가 arr에 없다면 
        arr.append(i)
        func()
        arr.pop()

func()
