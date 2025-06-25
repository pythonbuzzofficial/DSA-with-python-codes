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

def dfs(start):
    visited = set()
    stack = [start]
     
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current,end=' ')
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)


add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')
add_vertex('F')
add_vertex('G')

add_edge('A', 'B')
add_edge('B', 'C')
add_edge('B', 'G')
add_edge('C', 'D')
add_edge('C', 'E')
add_edge('E', 'F')

print(graph)

dfs('A')