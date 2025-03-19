def solution(arr):
    n = len(arr)
    answer = [] 
    answer = [0, 0]
    
    # 재귀 함수
    def func(x, y, n):
        value = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if value != arr[i][j]:
                    # 1구역
                    func(x, y, n // 2)
                    # 2구역
                    func(x, y + n // 2, n // 2)
                    # 3구역
                    func(x + n // 2, y, n // 2)
                    # 4구역
                    func(x + n // 2, y + n // 2, n // 2)
                    return
            
        # 같은 요소끼리만 있을 경우
        answer[value] += 1
        
    func(0, 0, n)
    return answer
