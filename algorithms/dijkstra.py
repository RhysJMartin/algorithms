import heapq
import os


def load_graph(num_vertices):
    file = os.path.join(os.path.dirname(__file__), '..', 'data', 'DijkstraData.txt')
    print('loading file: {}'.format(file))
    adjacency_list = [[] for _ in range(num_vertices)]
    with open(file, 'r') as data_file:
        for line in data_file:
            line_entries = line.split()
            vertex = line_entries[0]
            for adjacent_vertex in line_entries[1:]:
                index, distance = adjacent_vertex.split(',')
                adjacency_list[int(vertex) - 1].append((int(index), int(distance)))
    return adjacency_list


def shortest_path(graph, start_vertex):
    heap = []
    heapq.heappush(heap, (0, start_vertex))
    explored = set([])
    spath = [1000000] * len(graph)
    while heap:
        distance, vertex = heapq.heappop(heap)
        if vertex not in explored:
            explored.add(vertex)
            spath[vertex - 1] = distance
            for adjacent_vertex, edge_lenght in graph[vertex - 1]:
                heapq.heappush(heap, (distance + edge_lenght, adjacent_vertex))
    return spath


if __name__ == '__main__':
    graph = load_graph(200)
    spath = shortest_path(graph, 1)
    test_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    test_paths = ','.join([str(spath[x - 1]) for x in test_vertices])
    print(test_paths)
