graph = {}

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

def bfs(start):
    visited = set()
    queue = [start]
    
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current,end=" ")
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)


add_vertex('A')
add_vertex('B')
add_vertex('F')
add_vertex('C')
add_vertex('E')
add_vertex('D')

add_edge('A','B')
add_edge('A','F')
add_edge('B','C')
add_edge('F','E')
add_edge('C','D')
add_edge('E','D')

print(graph)

bfs('A')

