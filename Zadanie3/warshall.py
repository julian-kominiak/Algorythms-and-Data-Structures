import numpy as np


class Warshall:
    def __init__(self, graph, start, stop):
        self.graph = graph.copy()
        self.d = graph.copy()
        self.defineD()
        self.p = graph.copy()
        self.defineP()
        self.start = start
        self.stop = stop

    def defineD(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph)):
                if x == y:
                    self.d[x][y] = 0
                    continue
                if self.graph[x][y] == 0:
                    self.d[x][y] = 99

    def defineP(self):
        for x in range(len(self.graph)):
            for y in range(len(self.graph)):
                if x == y:
                    self.p[x][y] = 0
                    continue
                if self.graph[x][y] != 0:
                    self.p[x][y] = (x + 1)

    def findPath(self):
        path = []
        path.append(self.stop)
        temp = self.stop
        while temp != self.start:
            temp = self.p[self.start - 1][temp - 1]
            path.append(temp)
        path.reverse()
        print("Path: " + str(path))

    def execute(self):
        for u in range(0, len(self.graph)):
            for v in range(0, len(self.graph)):
                if v != u:
                    for w in range(0, len(self.graph)):
                        if w != u and w != v:
                            l = self.d[v][u] + self.d[u][w]
                            if l < self.d[v][w]:
                                self.d[v][w] = l
                                self.p[v][w] = self.p[u][w]
                            else:
                                self.d[v][w] = self.d[v][w]
                                self.p[v][w] = self.p[v][w]
        self.findPath()



array = np.array([[0, 1, 5, 0, 0, 0, 0],
                  [0, 0, 2, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [7, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0],
                  [2, 0, 0, 4, 0, 0, 0],
                  [6, 0, 0, 0, 0, 3, 0]])
w = Warshall(array, 7, 3)
w.execute()
