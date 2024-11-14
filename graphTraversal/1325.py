# 효율적인 해킹
dict = {}
def dfs(start):
    if visited[start] == 1:
        return
    visited[start] = 1
    for next in adj_list[start]:
        dfs(next)



