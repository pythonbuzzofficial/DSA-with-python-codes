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
    
#for directed graph
def add_edge(v1,v2):
    if v1 not in graph or v2 not in graph:
        print("vertex not found")
        return
    graph[v1].append(v2)

#for undirected weighted graph   
def add_edge(v1,v2,cost):
    if v1 not in graph or v2 not in graph:
        print("vertex not found")
        return
    graph[v1].append((v2,cost))
    graph[v2].append((v1,cost))

#for directed weighted graph 
def add_edge(v1,v2,cost):
    if v1 not in graph or v2 not in graph:
        print("vertex not found")
        return
    graph[v1].append((v2,cost))


add_vertex('A')
add_vertex('B')
add_vertex('C')
print(graph)

add_edge('A','B')
add_edge('A','C')
print(graph)