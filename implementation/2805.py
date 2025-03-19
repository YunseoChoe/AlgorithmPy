# 나무 자르기
# 입력
n, m = map(int, input().split()) # 나무의 수, 집으로 가져가려는 나무의 길이
height = list(map(int, input().split())) # 나무 길이 배열

start = 0 # 높이는 0부터 
end = max(height)
max_length = 0 # 초기화

# 이분 탐색
while start <= end: 
    count = 0
    middle = (start + end) // 2
    for i in range(len(height)):
        if height[i] - middle > 0:
            count += height[i] - middle

    # 만약 count가 m보다 크거나 같으면
    if count >= m:
        max_length = middle
        start = middle + 1
    else:
        end = middle - 1

print(max_length)
