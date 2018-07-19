import os


def load_graph_definition():
    file = os.path.join(os.path.dirname(__file__), '..', 'data', 'SCC.txt')
    print('loading file: {}'.format(file))
    graph_definition = []
    with open(file, 'r') as data_file:
        for line in data_file:
            line_values = [int(x) for x in line.split(' ')[:2]]
            graph_definition.append(line_values)
    return graph_definition


def create_graph(graph_definition, num_vertices, direction):
    """
    Takes a graph definition which consists of edges defined as a pair of vertices with the left value the tail and the
    right value the head vertex and creates a graph of vertices and adjacent vertices.
    :param graph_definition: List of edges [[a, b], [c, d]]
    :param num_vertices: Number of vertices
    :param direction: Can create the 'forward' or 'reverse' graph
    :return: list of adjacent vertices
    """
    graph = [[] for _ in range(num_vertices)]
    if direction == 'reverse':
        tail_index = 1
        head_index = 0
    elif direction == 'forward':
        tail_index = 0
        head_index = 1
    else:
        raise ValueError('Expected direction argument should be either "forward" or "reverse"')
    for edge in graph_definition:
        graph[edge[tail_index] - 1].append(edge[head_index] - 1)
    return graph


def dfs(graph, start, visited=None):
    """
    Searches using depth first search.
    :param graph: list of adjacent vertices
    :param start: id if vertex to start dfs search
    :param visited: set of pre-visited vertices
    :return: visted, finished, visited_together
    """
    if visited is None:
        visited = set([])
    stack, finished, visited_together = [start], [], []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            if vertex >= 0: # Natural number including zero describe a vertex yet to be visited
                visited.add(vertex)
                visited_together.append(vertex)
                stack.append(-vertex - 1)
                for adjacent_vertex in graph[vertex]:
                    if adjacent_vertex not in visited:
                        stack.append(adjacent_vertex)
            elif vertex < 0: # negative numbers are used to determine when we have finished exploring a vertex
                finished.append(-vertex - 1)
    return visited, finished, visited_together


def dfs_loop(graph, order):
    """
    Loop through the dfs search routine multiple times following the a given order
    :param graph: list of adjacent vertices
    :param order: start vertex will be evaluated in order based on list
    :return: Finish order, component size
    """
    visited = set([])
    component_size = []
    dfs_loop_finished_order = []
    for start in order:
        visited, finished_order, visited_together = dfs(graph, start, visited)
        component_size.append(len(visited_together))
        dfs_loop_finished_order.extend(finished_order)
    return dfs_loop_finished_order, component_size


def find_scc(graph_definition, num_vertices):
    """
    Performs reverse dfs search to find the finish order and a forward dfs to find strongly connected components
    :param graph_definition: list of edges
    :param num_vertices: number of vertices
    :return: list of length 5 with the larges strongly connected groups
    """
    print('Reverse pass')
    reverse_graph = create_graph(graph_definition, num_vertices, 'reverse')
    order = range(num_vertices)
    finish_order, _ = dfs_loop(reverse_graph, order)
    forward_graph = create_graph(graph_definition, num_vertices, 'forward')
    _, component_size = dfs_loop(forward_graph, reversed(finish_order))
    scc_sizes = sorted(component_size, reverse=True)
    return scc_sizes[:5]


if __name__ == '__main__':
    _graph_definition = load_graph_definition()
    print(find_scc(_graph_definition, 875714))
