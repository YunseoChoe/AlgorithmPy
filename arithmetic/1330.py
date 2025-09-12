# 두 수 비교하기
a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")