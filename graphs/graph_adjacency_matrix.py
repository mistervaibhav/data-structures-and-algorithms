from queue import Queue


class Graph:
    """non directed, non weighted"""

    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.matrix = [[0 for i in range(vertices)] for j in range(vertices)]

    def __is_index_valid(self, index):
        return index < self.vertices

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
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.matrix[i][j], end=" ")
            print()

    def has_edge(self, source, destination):

        if not self.__are_indexes_valid(source, destination):
            return False

        return (
            self.matrix[source][destination] == 1
            and self.matrix[destination][source] == 1
        )

    def add_edge(self, source, destination):

        if not self.__are_indexes_valid(source, destination):
            print(f"CANNOT ADD EDGE BETWEEN {source} AND {destination}")
            return

        self.__set_matrix_value(source, destination, 1)
        self.__set_matrix_value(destination, source, 1)

    def remove_edge(self, source, destination):

        if not self.has_edge(source, destination):
            print(f"CANNOT REMOVE EDGE BETWEEN {source} AND {destination}")
            return

        self.__set_matrix_value(source, destination, 0)
        self.__set_matrix_value(destination, source, 0)

    def __depth_first_traversal_helper(self, start, visited):

        print("Visited => ", start)
        visited[start] = True

        for i in range(self.vertices):
            if self.has_edge(start, i) and not visited.get(i, False):
                self.__depth_first_traversal_helper(i, visited)

    def depth_first_traversal(self):
        visited = dict()
        self.__depth_first_traversal_helper(0, visited)

    def breadth_first_traversal(self):
        queue = Queue()
        queue.put(0)

        visited = dict()
        visited[0] = True

        while not queue.empty():
            node = queue.get()
            print("Visited => ", node)

            for i in range(self.vertices):
                if self.has_edge(node, i) and not visited.get(i, False):
                    queue.put(i)
                    visited[i] = True

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
#         graph.addEdge(source, destination)

#     source, destination = map(int, input().split())
#     print('true' if graph.has_path(source,destination) else 'false')
