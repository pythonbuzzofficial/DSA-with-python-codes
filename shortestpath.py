from collections import deque
graph ={}
def add_vertex(vertex):
    if vertex in graph:
        print(f"{vertex} already exists.")
        return
    graph[vertex] =[]

#for undirected graph
def add_edge(v1,v2):
    if v1 not in graph or v2 not in graph:
        print("vertex not found")
        return
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs_shortest_path(start,target):
    if start not in graph or target not in graph:
        return None
    
    visited = set()
    queue = deque()
    queue.append((start,[start]))

    while queue:
        current,path = queue.popleft()
        if current == target:
            return path
        if current not in visited:
            visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor,path + [neighbor]))

    
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')
add_vertex('F')
add_vertex('G')


add_edge('A', 'B')
add_edge('B', 'E')
add_edge('C', 'A')
add_edge('E', 'D')
add_edge('C', 'D')
add_edge('C', 'G')
add_edge('G', 'F')
add_edge('F', 'D')


# print(graph)

shortest_path = bfs_shortest_path('A','F')
print("shortest path is :",shortest_path)