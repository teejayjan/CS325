# Author: Timothy Jan
# Date: 05/18/2021
# Description: Implements minimum spanning tree algorithms Kruskal and Prim's.


import heapq

class Graph:
    """Implements weighted graph to test MST algorithms. Copied from my CS261 Directed Graph assignment."""

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """Adds a new vertex to the graph, returning the number of vertices in the graph after addition."""

        self.v_count += 1
        new_vertex = []

        # fill new vertex with zero placeholders
        for _ in range(self.v_count):
            new_vertex.append(0)
        # append to matrix
        self.adj_matrix.append(new_vertex)

        # update placeholder zeroes of existing vertices
        for vertex in self.adj_matrix:
            if len(vertex) < self.v_count:
                while len(vertex) < self.v_count:
                    vertex.append(0)
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """Adds a new edge to the graph, connecting two vertices with provided indices. If either (or both) vertices
        do not exist, or if the weight is not a positive integer, or if src and dst are the same, does nothing.
        If an edge already exists, the method will update the weight. Adjusted from CS261 to make it undirected."""

        if src == dst:  # no same
            return
        if src >= self.v_count or dst >= self.v_count or src < 0 or dst < 0:  # vertices aren't in the graph
            return
        if weight < 0:
            return
        self.adj_matrix[src][dst] = weight
        self.adj_matrix[dst][src] = weight

    def get_vertices(self) -> []:
        """Returns a list of vertices of the graph."""

        vertices = []
        for _ in range(self.v_count):
            vertices.append(_)
        return vertices

    def get_edges(self) -> []:
        """Returns a list of edges in the graph. Each edge is a tuple of two vertex indices and weight:
        (source, destination, weight)."""

        edges = []
        for row_index in range(self.v_count):  # iterate through rows
            for column_index in range(self.v_count):  # iterate through columns
                if self.adj_matrix[row_index][column_index] != 0:  # add new tuple if the edge exists
                    edge = (row_index, column_index, self.adj_matrix[row_index][column_index])
                    edges.append(edge)
        return edges


def Kruskal(G):
    """Uses Kruskal's algorithm to find the minimum spanning tree of graph G."""
    # get connected vertices and corresponding edges, sorted by ascending weight
    edge_temp = sorted(edges, key=lambda x: x[-1])
    E = {}
    # convert sorted vertices and edges to dictionary
    for edge in edge_temp:
        E[(edge[0], edge[1])] = edge[2]
    # get vertices
    V = G.get_vertices()
    # initialize forest
    forest = {}
    # populate forest with each vertex by itself
    for v in V:
        forest[v] = [v]
    # initialize MST
    MST = {}
    # iterate through edges
    for edge in E:
        v1 = edge[0]
        v2 = edge[1]
        # check to see whether they belong to the same trees to avoid cycle
        if v1 not in forest[v2] and v2 not in forest[v1]:
            # if not, add it to the MST
            MST[(v1, v2)] = E[(v1, v2)]
            # merge the trees
            forest[v1] = forest[v1] + forest[v2]
            forest[v2] = forest[v1] + forest[v2]

    return MST


def Prims(G):
    """Uses Prim's algorithm to find the minimum spanning tree of graph G."""
    # get connected vertices and corresponding edges, sorted by ascending weight
    edge_temp = sorted(edges, key=lambda x: x[-1])
    E = {}
    # convert sorted vertices and edges to dictionary
    for edge in edge_temp:
        E[(edge[0], edge[1])] = edge[2]
    # get vertices
    V = G.get_vertices()

    result = {}
    visited = [V[-1]]

    while len(visited) < G.v_count:
        for a in visited:
            minimum = (float("inf"), 0)
            for b in range(G.v_count):
                if G.adj_matrix[a][b] != 0 and G.adj_matrix[a][b] < minimum[0] and b not in visited:
                    minimum = (G.adj_matrix[a][b], b)
            if a in visited and minimum[1] not in visited:
                result[(a, minimum[1])] = minimum[0]
                visited.append(minimum[1])
    return result




if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = Graph()
    for _ in range(5):
        g.add_vertex()

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)

    print(Kruskal(g))
    print(Prims(g))
    