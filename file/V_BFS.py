N, M, V = map(int, input().split()) 
matrix = [[0] * (N + 1) for _ in range(N + 1)] # B,DFS를 위한 인접행렬을 설정
# 여기서 인접행렬이란? 각 노드가 연결된 간선을 행렬을 통해 나타내는 것을 의미한다
for _ in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1
# 주어진 간선을 양쪽으로 이어지게 0,1 1,0을 1로 만들어준다.

def dfs(current_node, row, visited):
    visited += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in visited:
            visited = dfs(search_node, row, visited)
    return visited


def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in visited:
                visited += [search_node]
                queue += [search_node]
    return visited


print(*dfs(V, matrix, []))
print(*bfs(V))
