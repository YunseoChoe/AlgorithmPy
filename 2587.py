sum = 0
num = []
for i in range(5):
    a = int(input())
    num.append(a)
    sum = sum + num[i]
    
num.sort()
print(int(sum / 5)) # 평균
print(num[2]) # 중앙값