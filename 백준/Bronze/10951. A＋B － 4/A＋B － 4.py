# A + B - 4
while True:
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)
    except:
        break
    print(a+b)