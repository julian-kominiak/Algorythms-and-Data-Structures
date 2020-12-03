import sys


class Djikstra:
    def __init__(self, graph, start, finish):
        self.graph = graph
        self.start = start
        self.finish = finish
        self.pred = [0] * len(self.graph)
        self.dist = [sys.maxsize] * len(self.graph)
        self.dist[start] = 0
        self.visited = [False] * len(self.graph)

    def getElementWithLowestDist(self):
        current_lowest = sys.maxsize
        lowest_index = 0
        for i in range(len(self.graph)):
            if self.visited[i] is False and self.dist[i] < current_lowest:
                current_lowest = self.dist[i]
                lowest_index = i
        return lowest_index

    def printPath(self):
        current_pred = self.pred[self.finish]
        path_array = [self.finish, current_pred]
        while current_pred != self.start:
            current_pred = self.pred[current_pred]
            path_array.append(current_pred)
        path_array.reverse()
        print("Path: " + str(path_array) + " distance: " + str(self.dist[self.finish]))

    def getNumberOfVisited(self):
        counter = 0
        for i in self.visited:
            if i:
                counter += 1
        return counter

    def execute(self):
        going_from = self.start
        number_of_visited = 0
        while number_of_visited < len(self.graph):
            self.visited[going_from] = True
            for going_to in range(0, len(self.graph)):
                if self.visited[going_to] is False and self.graph[going_from][going_to]:
                    if self.dist[going_from] + self.graph[going_from][going_to] < self.dist[going_to]:
                        self.dist[going_to] = self.graph[going_from][going_to] + self.dist[going_from]
                        self.pred[going_to] = going_from
            going_from = self.getElementWithLowestDist()
            number_of_visited = self.getNumberOfVisited()
        self.printPath()


djikstra = Djikstra([[0, 3, 0, 3, 5],
                     [3, 0, 5, 1, 0],
                     [0, 5, 0, 2, 0],
                     [3, 1, 2, 0, 1],
                     [5, 0, 0, 1, 0]], 0, 4)

djikstra.execute()
