import traceback

class Graph(dict):
    def __init__(self,vs=[],es=[]):
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self,v):
        self[v] = {}

    def add_edge(self,e):
        v,w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self,v,w):
        try:
            e = self[w][v]
        except Exception:
            e = None
        return e

    def remove_edge(self,edge):
        w = edge[0]
        v = edge[1]
        try:
            del(self[w][v])
            del(self[v][w])
        except Exception:
            print traceback.print_exc()

class Vertex(object):
    def __init__(self,label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls,(e1,e2))

    def __repr__(self):
        return 'Edge(%s,%s)' % (repr(self[0]),repr(self[1]))


if __name__ == '__main__':
    w = Vertex('w')
    v = Vertex('v')
    u = Vertex('u')
    z = Vertex('z')
    e = Edge(w,v)
    e1 = Edge(z,u)
    g = Graph([w,v],[e,])
    e = g.get_edge(w,u)

    g.remove_edge(e1)