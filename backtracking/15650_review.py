# N과 M(2) 복습
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
        # arr가 비어있다면
        if len(arr) == 0:
            arr.append(i)
            func()
            arr.pop()
        else:
            # 정렬
            if arr[-1] < i:
                arr.append(i)
                func()
                arr.pop()

func()

# arr = []
# def func(start):
#     if len(arr) == m:
#         # 출력
#         for i in range(len(arr)):
#             print(arr[i], end = " ")
#         print()
#         return
    
#     for i in range(start, n + 1):
#         if i not in arr:
#             arr.append(i)
#             func(i + 1)
#             arr.pop()

# func(1)

