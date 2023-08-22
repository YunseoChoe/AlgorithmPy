import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push_front":
        num.insert(0, a[1])
    elif a[0] == "push_back":
        num.append(a[1])
    elif a[0] == "pop_front":
        if len(num) == 0:
            print(-1)
        else:
            ret = num.pop(0)
            print(ret)
    elif a[0] == "pop_back":
        if len(num) == 0:
            print(-1)
        else:
            ret = num.pop(-1)
            print(ret)
    elif a[0] == "size":
        print(len(num))
    elif a[0] == "empty":
        if len(num) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(num) == 0:
            print(-1)
        else:
            print(num[0])
    elif a[0] == "back":
        if len(num) == 0:
            print(-1)
        else:
            print(num[-1])