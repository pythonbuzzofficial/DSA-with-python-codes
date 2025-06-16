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
# def add_edge(v1,v2):
#     if v1 not in graph or v2 not in graph:
#         print("vertex not found")
#         return
#     graph[v1].append(v2)

#for undirected weighted graph   
# def add_edge(v1,v2,cost):
#     if v1 not in graph or v2 not in graph:
#         print("vertex not found")
#         return
#     graph[v1].append((v2,cost))
#     graph[v2].append((v1,cost))

#for directed weighted graph 
# def add_edge(v1,v2,cost):
#     if v1 not in graph or v2 not in graph:
#         print("vertex not found")
#         return
#     graph[v1].append((v2,cost))

def delete_vertex(vertex):
    graph.pop(vertex)
    for i in graph:
        if vertex in graph[i]:
            graph[i].remove(vertex)

def delete_vertex_weighted(vertex):
    graph.pop(vertex) 
    for i in graph:
        for j in graph[i]:
            if vertex in j:
                graph[i].remove(j)

def delete_edge(v1,v2):
    if v2 in graph[v1]:
        graph[v1].remove(v2)
    
    if v1 in graph[v2]:
        graph[v2].remove(v1)
    
def delete_weighted_edge(v1,v2):
    for edge in graph[v1]:
        if v2 in edge:
            graph[v1].remove(edge)
    for edge in graph[v2]:
        if v1 in edge:
            graph[v2].remove(edge)   

add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')

add_edge('A','B')
add_edge('A','C')
add_edge('C','D')
add_edge('B','D')
print(graph)

# delete_vertex('D')
# print(graph)
delete_edge('C','D')
print(graph)