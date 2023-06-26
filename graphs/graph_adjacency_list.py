from queue import Queue


class Graph:
    """non directed, non weighted"""

    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.dictionary = dict()

        for v in range(self.vertices):
            self.dictionary[v] = list()

    def __is_index_valid(self, index):
        # another way would be
        # return index < self.vertices

        return index in self.dictionary

    def __are_indexes_valid(self, *args):
        for index in args:
            if self.__is_index_valid(index):
                continue
            else:
                return False
        return True

    def __set_matrix_value(self, row, column, value):
        if not self.__are_indexes_valid(row, column):
            return

        if value not in (0, 1):
            return

        self.matrix[row][column] = value

    def display(self):
        for vertex in self.dictionary:
            edges = self.dictionary.get(vertex)
            for edge in edges:
                print(f"{vertex} -> {edge}")
            # print()

    def has_edge(self, source, destination):
        if not self.__are_indexes_valid(source, destination):
            return False

        return destination in self.dictionary[source]

    def add_edge(self, source, destination):
        if not self.__are_indexes_valid(source, destination):
            print(f"CANNOT ADD EDGE BETWEEN {source} AND {destination}")
            return

        self.dictionary[source].append(destination)

    def remove_edge(self, source, destination):
        if not self.has_edge(source, destination):
            print(f"CANNOT REMOVE EDGE BETWEEN {source} AND {destination}")
            return

        self.dictionary[source].pop(destination)

    def __depth_first_traversal_helper(self, start, visited):
        print("Visited => ", start)
        visited[start] = True

        for i in range(self.vertices):
            if self.has_edge(start, i) and not visited.get(i, False):
                self.__depth_first_traversal_helper(i, visited)

    def depth_first_traversal(self):
        visited = dict()

        for vertex in range(self.vertices):
            if not visited.get(vertex, False):
                self.__depth_first_traversal_helper(0, visited)

    def ___breadth_first_traversal_helper(self, start, visited):
        queue = Queue()
        queue.put(start)

        visited[start] = True

        while not queue.empty():
            node = queue.get()
            print("Visited => ", node)

            for i in range(self.vertices):
                if self.has_edge(node, i) and not visited.get(i, False):
                    queue.put(i)
                    visited[i] = True

    def breadth_first_traversal(self):
        visited = dict()

        for vertex in range(self.vertices):
            if not visited.get(vertex, False):
                self.___breadth_first_traversal_helper(vertex, visited)

    def has_path(self, source, destination, visited=dict()) -> bool:
        if self.has_edge(source, destination):
            return True

        visited[source] = True

        for i in range(self.vertices):
            if self.has_edge(source, i) and not visited.get(i, False):
                visited[i] = True
                if self.has_path(i, destination, visited):
                    return True

        return False

    def get_path_dfs(self, source, destination, visited=dict(), path=list()) -> bool:
        if self.has_edge(source, destination):
            return path.append(destination)

        visited[source] = True

        for i in range(self.vertices):
            if self.has_edge(source, i) and not visited.get(i, False):
                visited[i] = True
                return self.get_path_dfs(i, destination, visited, path)

        return []


#################################################################################################################

graph = Graph(5)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)


# graph.depth_first_traversal()
graph.breadth_first_traversal()

# graph.display()


# if __name__ == "__main__":
#     vertices, edges = map(int, input().split())

#     graph = Graph(vertices)

#     for i in range(edges):
#         source, destination = map(int, input().split())
#         graph.add_edge(source, destination)

#     source, destination = map(int, input().split())

#     # print('true' if graph.has_path(source,destination) else 'false')

#     path = graph.get_path_dfs(source, destination)

#     print(path)
