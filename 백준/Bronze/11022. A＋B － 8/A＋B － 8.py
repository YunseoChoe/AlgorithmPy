# A + B - 8
t = int(input())
for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)

    print(f'Case #{i + 1}: {a} + {b} = {a + b}')