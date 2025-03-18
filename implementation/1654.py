# 랜선 자르기
k, n = map(int, input().split())
lans = []
for i in range(k):
    lans.append(int(input()))

start = 1
end = max(lans)

# 랜선의 개수 구하기
while start <= end:
    count = 0
    middle = (start + end) // 2
    for i in range(len(lans)):
        count += lans[i] // middle

    # 필요한 랜선의 개수보다 작게 잘랐으면
    if count >= n:
        # 최대 길이 갱신 (N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.)
        max_length = middle
        start = middle + 1 # 더 크게 자르기
    
    elif count < n:
        end = middle - 1 # 더 작게 자르기

print(max_length)
