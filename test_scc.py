from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

        # A function used by DFS

    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        print('fill {}'.format(v))

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

        # Function that returns reverse (or transpose) of this graph

    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

        # The main function that finds and prints all strongly

    # connected components
    def printSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)

        visited = {i: False for i in self.graph}
        # Fill vertices in stack according to their finishing
        # times
        for i in self.graph:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

                # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = {i: False for i in self.graph}
        print(stack)
        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print()


        # Create a graph given in the above diagram


g = Graph(7)
g.addEdge(5, 4)
g.addEdge(8, 0)
g.addEdge(4, 3)
g.addEdge(3, 5)
g.addEdge(0, 1)
g.addEdge(1, 8)
g.addEdge(8, 6)
print(g.graph)






print("Following are strongly connected components " +
      "in given graph")
g.printSCCs()
# This code is contributed by Neelam Yadav