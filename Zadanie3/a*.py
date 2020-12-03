import sys


class A:
    def __init__(self, graph, h, start):
        self.graph = graph
        self.h = h
        self.f = [0] * len(self.graph)
        self.g = [sys.maxsize] * len(self.graph)
        self.pred = [0] * len(self.graph)
        self.start = start
        self.visited = [False] * len(self.graph)

    def getLowestV(self):
        current_minimum = sys.maxsize
        minimum_index = 0
        for i in range(0, len(self.graph)):
            if self.g[i] < current_minimum and self.visited[i] is False:
                current_minimum = self.g[i]
                minimum_index = i
        return minimum_index

    def printResults(self):
        print("h = " + str(self.h))
        print("g = " + str(self.g))
        print("f = " + str(self.f))
        print("pred = " + str(self.pred))

    def printPath(self):
        current_pred = self.pred[7]
        path_array = [7, current_pred]
        while current_pred != self.start:
            current_pred = self.pred[current_pred]
            path_array.append(current_pred)
        path_array.reverse()
        print("Path: " + str(path_array))

    def execute(self):
        self.g[self.start] = 0
        self.f[self.start] = self.h[self.start] + self.g[self.start]
        for i in range(0, len(self.graph)):
            v = self.getLowestV()
            self.visited[v] = True
            for u in range(0, len(self.graph)):
                if self.graph[v][u] > 0 and self.visited[u] == False and self.g[u] > self.g[v] + self.graph[v][u]:
                    self.g[u] = self.g[v] + self.graph[v][u]
                    self.pred[u] = v
                    self.f[u] = self.g[u] + self.h[u]
        self.printResults()
        self.printPath()


h = [4, 8, 3, 4, 5, 2, 1, 0]
a = A([[0, 5, 0, 1, 0, 0, 0, 0],
       [0, 0, 2, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 3],
       [0, 0, 0, 0, 1, 2, 0, 0],
       [0, 0, 4, 0, 0, 0, 0, 0],
       [4, 0, 0, 0, 0, 0, 2, 0],
       [0, 0, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 2, 0, 0, 0]],
      h, 0)

a.execute()
