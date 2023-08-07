n = input() # 문자열

num = []
for i in range(len(n)):
    num.append(n[i])

for i in range(len(num)):
    num[i] = int(num[i])

num.sort(reverse=1)

for i in range(len(num)):
    print(num[i], end = "")