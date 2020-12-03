import sys


class Prim:
    def __init__(self, G):
        self.G = G
        self.V = len(self.G)
        self.size = len(self.G)
        self.visited = [False] * self.size
        self.num_of_visited = 0
        self.visited[0] = True
        self.pred = [0] * self.size
        self.k = [0] * self.size
        self.k_sum = 0

    def execute(self):
        while self.num_of_visited < self.V - 1:
            current_k = sys.maxsize
            current_element, new_element = 0, 0
            for i in range(self.V):
                if self.visited[i]:
                    for j in range(self.V):
                        if not self.visited[j] and self.G[i][j]:
                            if current_k > self.G[i][j]:
                                current_k = self.G[i][j]
                                current_element, new_element = i, j
            self.pred[new_element] = current_element
            self.k[new_element] = current_k
            print("{} => {} : {}".format(current_element, new_element, self.k[new_element]))
            self.visited[new_element] = True
            self.num_of_visited += 1
            self.k_sum += self.k[new_element]

        print()
        print('V'.rjust(4), '║', 'Pred'.rjust(4), '║', 'K'.rjust(4))
        print('═════╬══════╬═════')
        for i in range(self.V):
            print(str(i).rjust(4), '║', str(self.pred[i]).rjust(4), '║', str(self.k[i])
                  .rjust(4))
        print("sum(k) = " + str(self.k_sum))


prim = Prim([[0, 3, 0, 3, 5],
             [3, 0, 5, 1, 0],
             [0, 5, 0, 2, 0],
             [3, 1, 2, 0, 1],
             [5, 0, 0, 1, 0]])

prim.execute()
