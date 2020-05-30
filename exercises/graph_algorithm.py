"""define Graph clss and DFS, BFS"""

class Vertex:
    """lightweight vertex structure for a graph"""
    __slots__ = '_element'

    def __init__(self, x):
        """do not call constructor directly, use Graph's insert_vertex(x) instead"""
        self._element = x

    def element(self):
        """return element associated with this vertex"""

    def __hash__(self):
        return hash(id(self))  # 预哈希函数使顶点可用作map或set的key


class Edge:
    """lightweight edge structure for a graph"""
    # __slots__ = '_origin, _destination, _element'

    def __init__(self, u, v, x):
        """Do not call constructor directly, use Graph's insert_edge(u,v,x) instead"""
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """return (u,v) tuple for vertices u & v"""
        return (self._origin, self._destination)

    def opposite(self, v):
        """return the vertex that is opposite v on this edge"""
        return self._origin if v is self._destination else self._destination

    def element(self):
        """return element associted with this edge"""
        return self._element

    def __hash__(self):
        return hash(id(self))  # allow edge to be a map/set key


class Graph:
    """representation of a simple graph with adjacency map"""

    def __init__(self, directed=False):
        """Create an empty graph(undirected, by default).
        Graph is directed if optional parameter 'directed' is set to be True"""
        self._outgoing = {}
        # if graph is directed, then initiate another map
        self._incoming = {} if directed == True else self._outgoing

    def is_directed(self):
        return self._outgoing is not self._incoming

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed else total // 2

    def edges(self):
        """return a set of all edges of the graph"""
        result = set()  # avoid double_reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        """return the edge from u to v or None if not adjacent"""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """return number of edges incident to vertex v in the graph.
        if graph is directed, optional parameter used to count incoming edges"""
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """return all edges incident to vertex v in the graph.
        if graph is directed, optional parameter used to request incoming edges"""
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge  # why use yield here?

    def insert_vertex(self, x=None):
        """insert and return a new vertex with element x"""
        v = Vertex(x)
        self._outgoing[v] = {}
        self._incoming[v] = {} if self.is_directed else self._outgoing
        return v

    def insert_edge(self, u, v, x=None):
        """insert and return a new edge from u to v with auxiliary element x"""
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

