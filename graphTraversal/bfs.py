# Queue
class Queue:
    def __init__(self):
        self.data = []

    # 삽입
    def enqueue(self, value):
        self.data.append(value)

    # 삭제
    def dequeue(self):
        if self.isEmpty():
            print("데이터 없음")
        else:
            data_pop = self.data.pop(0)
            return data_pop

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
# 정점: 0, 1, 2, 3
adj_mat = [[0, 1, 1, 0],
           [1, 0, 0, 1],
           [1, 0, 0, 1],
           [0, 1, 1, 0]]
        
visited = [0, 0, 0, 0]  # 방문 배열
def bfs(start):
    queue = Queue()
    visited[start] = 1 
    queue.enqueue(start)
    
    while not queue.isEmpty(): # queue가 빌때 까지 (queue.isEmpty()가 True가 될 때 까지 반복)
        # queue에서 삭제하고 출력
        vertex = queue.dequeue()
        print(vertex)
        
        # 자식 노드 queue에 삽입
        for i in range(len(adj_mat[0])):
            if adj_mat[vertex][i] == 1 and visited[i] == 0:
                print(f'인접 정점: {i}', end = " ")
                print()
                queue.enqueue(i)
                visited[i] = 1

print("bfs: ", end = " ")
bfs(0)



       