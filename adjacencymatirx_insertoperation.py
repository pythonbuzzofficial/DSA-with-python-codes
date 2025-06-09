vertices =[]
matrix =[]

def add_vertex(vertex):
    if vertex in vertices:
        print(f"{vertex} already exixts.")
        return
    vertices.append(vertex)

    for row in matrix:
        row.append(0)
    
    matrix.append([0]*len(vertices))

#for undirected graph
def add_edge(V1,V2):
    if V1 not in vertices or V2 not in vertices:
        print("Vertex not found")
        return
    i = vertices.index(V1)
    j = vertices.index(V2)
    matrix[i][j] =1
    matrix[j][i] =1

#for directed graph
def add_edge(V1,V2):
    if V1 not in vertices or V2 not in vertices:
        print("Vertex not found")
        return
    i = vertices.index(V1)
    j = vertices.index(V2)
    matrix[i][j] =1

#for undirected weighted graph   
def add_edge(V1,V2,cost):
    if V1 not in vertices or V2 not in vertices:
        print("Vertex not found")
        return
    i = vertices.index(V1)
    j = vertices.index(V2)
    matrix[i][j] =cost
    matrix[j][i] =cost

#for directed weighted graph   
def add_edge(V1,V2,cost):
    if V1 not in vertices or V2 not in vertices:
        print("Vertex not found")
        return
    i = vertices.index(V1)
    j = vertices.index(V2)
    matrix[i][j] =cost


add_vertex('A')
add_vertex('B')
add_vertex('C')
print(vertices)

add_edge('A','B')
add_edge('B','C')
print(matrix)
for row in matrix:
    print(*row)