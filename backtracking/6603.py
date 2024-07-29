# 로또
# arr = []
# def func(start):
#     if len(arr) == 6:
#         for i in range(len(arr)):
#             print(s[arr[i]], end = " ")
#         print()
#         return
    
#     for i in range(start, len(s)):
#         if i not in arr:
#             arr.append(i)
#             func(i + 1)
#             arr.pop()

# while True:
#     num = list(map(int, input().split()))
#     if num[0] == 0:
#         break
#     s = num[1:]

#     func(0)
#     print()


# 로또 복습
def func(start):
        if len(arr) == 6:
            for i in range(len(arr)):
                print(arr[i], end = " ")
            print()
            return
        else:
            for i in range(start, len(s)):
                if s[i] not in arr:
                    arr.append(s[i])
                    func(i + 1)
                    arr.pop()
                    
while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break

    s = num[1:]

    arr = []

    func(0)
    print()
