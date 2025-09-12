# 커트라인
n, k = map(int, input().split())  # 응시자 수 n, 상을 받는 사람의 수 k
x = map(int, input().split())
x = list(x)

# 역순으로 정렬
x.sort()
x.reverse()

# k번째 점수 출력
cutline = k - 1
print(x[cutline])