graph = {}
visited = set() 

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
    stack = [start] 
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current,end=' ')
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

def is_connected():
    for i in list(graph):
        if i not in visited:
            print("Given graph is disconnected graph")
            break
    else:
        print("Given graph is connected graph")

def traverse_disconnected_graph():
     for i in list(graph):
        if i not in visited:
            print("next connected component")
            dfs(i)
            

add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('E')
add_vertex('F')
add_vertex('G')
add_vertex('K')
add_vertex('I')

add_edge('A', 'B')
add_edge('B', 'C')
add_edge('C', 'A')
add_edge('E', 'F')
add_edge('E', 'G')
add_edge('G', 'F')
add_edge('K', 'I')

print(graph)

dfs('A')
traverse_disconnected_graph()

# is_connected()





