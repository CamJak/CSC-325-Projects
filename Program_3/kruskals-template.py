import sys

class Graph:

    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    class __Vertex:
        def __init__(self, key):
            self.id = key       
            self.connectedTo = {} 

        def getId(self):
            return self.id

        def getConnections(self):
            return self.connectedTo.keys()

        def getWeight(self, nbr):
            return self.connectedTo[nbr] 

        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return f"connected to: {str([x.id for x in self.connectedTo])}"   

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Graph.__Vertex(key)
        self.verList[key] = newVertex 
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, source, destination, weight = 0):
        if source not in self.verList:
            newVertex = self.addVertex(source)
        if destination not in self.verList:
            newVertex = self.addVertex(destination)
        self.verList[source].addNeighbor(self.verList[destination], weight)
    
    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()

        if s not in visited:
            print(s, end = " ")
            visited.add(s)
            for next_node in [x.id for x in self.verList[s].connectedTo]:
                self.dfs(next_node, visited)        

    def bfs(self, s, visited = None):
        if visited is None:
            visited = set()

        q = Queue()
        q.put(s)
        visited.add(s)

        while not q.empty():
            current_node = q.get()
            print(current_node, end = " ")

            for next_node in [x.id for x in self.verList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)

    def kruskals(self):
        vertices_sets = set()
        edges_dict = dict()
        MST = set()
        
        # create set of vertex sets
        for vertex in self.verList.keys():
            temp = frozenset([vertex])
            vertices_sets.add(temp)
        # create dictionary of all edges and their weights
        # iterate through all the vertices
        for vertex in self.verList.keys():
            # iterate through the vertices connected to the current vertex
            for nbr in [x.id for x in self.verList[vertex].connectedTo]:
                # add edge to dictionary with its weight
                edges_dict[(vertex, nbr)] = self.verList[vertex].connectedTo[self.verList[nbr]]
        # sort the dictionary of edges by weight
        # used idea from: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        edges_dict = {k:v for k,v in sorted(edges_dict.items(), key = lambda x: x[1])}

        # iterate through the sorted edges
        for edge in edges_dict.keys():
            s_u = None
            s_v = None
            # iterate through the set of vertex sets
            for currSet in vertices_sets:
                # if the current vertex set contains the current edge's source or destination
                # save the current vertex set to s_u or s_v
                if edge[0] in currSet:
                    s_u = currSet
                if edge[1] in currSet:
                    s_v = currSet
            # if the sets containing the current edge's source and destination are not the same
            if s_u != s_v:
                # add the current edge to the MST
                MST.add((edge, edges_dict[edge]))
                # combine the two sets into one
                s_uv = s_u.union(s_v)
                # remove the old sets from the set of vertex sets
                vertices_sets.remove(s_u)
                vertices_sets.remove(s_v)
                # add the new set to the set of vertex sets
                vertices_sets.add(s_uv)

        return MST

def main():
    
    # create an empty graph
    graph = Graph()

    # get graph vertices & edges from input file and add them to the graph
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()
        graph.addEdge(int(values[0]), int(values[1]), int(values[2]))
        graph.addEdge(int(values[1]), int(values[0]), int(values[2]))   

    # print adjacency list representation of the graph
    print()
    print("Graph adjacency list:")
    for vertex in graph.verList:
        print(f"{vertex} {graph.verList[vertex]}")
    
    # create graph MST
    MST = graph.kruskals()
    # print graph MST
    print()    
    print("Graph MST:")
    print("Edge\t\tWeight")
    for edge in MST:
        print(f"{edge[0]}\t\t{edge[1]}")

main() 
    
    
