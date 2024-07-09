# 숨바꼭질
n, m = input().split()
n = int(n)
m = int(m)

dist = [0] * 100001 # 최단 시간을 저장하는 배열, dist[3] = 5 -> 시작위치에서 3까지 가는 데 걸리는 시간은 5초
def bfs(start):
    dist[start] = 0
    queue = []
    queue.append(start)
    
    while not len(queue) == 0:
        x = queue.pop(0)
        for x_1 in [x - 1, x + 1, x * 2]:
            if x_1 == start:
                pass
            else:
                if 0 <= x_1 <= 100000 and dist[x_1] == 0:
                    dist[x_1] = dist[x] + 1
                    queue.append(x_1)

bfs(n)
print(dist[m])