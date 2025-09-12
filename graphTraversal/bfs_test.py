visited = set() # 중복 허용 안합니다. 순서가 없습니다.

def bfs_shortest_path(graph, start_node, goal_node):
    path_dic =  {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0} # 최단 거리를 저장하는 딕셔너리
    prev_dic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0} # 이전 정점 저장하는 딕셔너리
    path_dic[start_node] = 0

    queue = []               
    queue.append(start_node)
    visited.add(start_node)
    while len(queue) != 0:
        vertex = queue.pop(0) # 'A'

        for neighbor in graph[vertex]: # graph[vertex] = ['B', 'C']
            if neighbor == start_node:
                pass
            else:
                if path_dic[neighbor] == 0:
                    path_dic[neighbor] = path_dic[vertex] + 1
                    queue.append(neighbor)
                    prev_dic[neighbor] = vertex

    # 정점 출력
    path = []
    current_node = goal_node
    while current_node != start_node:
        path.append(prev_dic[current_node])
        current_node = prev_dic[current_node]
    path.reverse()
    path.append(goal_node)
    
    return path_dic[goal_node], path

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'E'],
    'G': ['E']
}

# path_dic = {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}

start_node = 'A'
goal_node = 'F'
distance = bfs_shortest_path(graph, start_node, goal_node)
print(distance) # print shortest distance: 2