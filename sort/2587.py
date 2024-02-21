# 대표값2
num = []
for i in range(5):
    n = int(input())
    num.append(n)

# 평균 
sum = 0
for i in range(len(num)):
    sum += num[i]
print(int(sum / 5))
# 중앙값
num.sort()
print(num[5 // 2])