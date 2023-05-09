class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = {}
            return True
        return False

    def add_edge(self, v1, v2, weight):
        # check if both vertex exist or not.
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # here we are connecting bidirectional
            self.adj_list[v1][v2] = weight
            self.adj_list[v2][v1] = weight
            return True
        return False

    def dijkstra(self, start_vertex, end_vertex):
        # initialize the distance dictionary with infinite distance for all vertices except the start vertex
        distance = {vertex: float('inf') for vertex in self.adj_list}
        distance[start_vertex] = 0

        # initialize the visited set
        visited = set()

        # loop until all vertices have been visited
        while len(visited) < len(self.adj_list):
            # find the vertex with the minimum distance that has not been visited
            min_vertex = None
            min_distance = float('inf')
            for vertex in self.adj_list:
                if vertex not in visited and distance[vertex] < min_distance:
                    min_vertex = vertex
                    min_distance = distance[vertex]

            # mark the min_vertex as visited
            visited.add(min_vertex)

            # update the distances of the neighboring vertices
            for neighbor in self.adj_list[min_vertex]:
                if neighbor not in visited:
                    new_distance = distance[min_vertex] + self.adj_list[min_vertex][neighbor]
                    if new_distance < distance[neighbor]:
                        distance[neighbor] = new_distance

        # return the distance to the end vertex
        return distance[end_vertex]


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B', 1)
my_graph.add_edge('B', 'C', 2)
my_graph.add_edge('C', 'D', 3)

my_graph.print_graph()
print('\n shortest distance: ', my_graph.dijkstra('A', 'D'))