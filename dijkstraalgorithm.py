import heapq
graph = {}

def add_vertex(vertex):
    if vertex in graph:
        print(f"{vertex} already exists.")
        return
    graph[vertex] =[]

def add_edge(v1,v2,cost):
    if v1 not in graph or v2 not in graph:
        print("vertex not found")
        return
    graph[v1].append((v2,cost))
    graph[v2].append((v1,cost))

def dijkstra(start):
    distances = {node:float('inf')  for node in graph}
    distances[start] = 0
    # print(distances)
    pq = [(0,start)]
    
    while pq:
        current_distance,current_node = heapq.heappop(pq)
        
        for neighbor,weight in graph[current_node]:
            distance = current_distance+weight
            if distance<distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq,(distance,neighbor))

    return distances

add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')
add_vertex('F')

add_edge('A', 'B', 2)
add_edge('A', 'C', 5)
add_edge('A', 'D', 4)
add_edge('B', 'F', 2)
add_edge('C', 'D', 6)
add_edge('C', 'E', 2)
add_edge('C', 'F', 1)
add_edge('D', 'E', 2)
add_edge('E', 'F', 3)

# print(graph)
shortest_path = dijkstra('B')
# print(shortest_path)

for node,weight in shortest_path.items():
    print(f"Shortest path from B to {node} is {weight}")

