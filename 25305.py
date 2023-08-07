n, k = input().split() # 응시자 수, 상을 받는 사람의 수
n = int(n)
k = int(k)

num = input().split()
for i in range(n):
    num[i] = int(num[i])

num.sort(reverse=1)

# 커트라인 출력하기
print(num[k - 1])