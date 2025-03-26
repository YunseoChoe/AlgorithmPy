# 최대 힙
import heapq, sys
input = sys.stdin.readline

if __name__ == '__main__':
    max_heap = [] # 배열로 구현
    n = int(input())
    for i in range(n):
        x = int(input())
        # 0이라면 현재 배열에서 최댓값 출력 후 제거
        if x == 0:
            # 배열이 비어있다면
            if len(max_heap) == 0:
                print(0)
            else:
                print(-heapq.heappop(max_heap))
        # 0이 아니라면 배열에 저장
        else:
            heapq.heappush(max_heap, -x)
