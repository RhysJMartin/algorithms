import os
import random
import math
import logging


def load_data():
    file = os.path.join(os.path.dirname(__file__), '..', 'data', 'KargerMinCut.txt')
    print('loading file: {}'.format(file))
    data_file = open(file, 'r')
    data = []
    for line in data_file:
        data.append([int(x) for x in line.replace('\t\n', '').split('\t')])
    return data


class AdjacencyList():
    def __init__(self, data, seed=None):
        vertices, edges = self.init_adjacency_list(data)
        self.vertices = vertices
        self.edges = edges
        self.living_edges = list(range(len(edges)))
        if seed is not None:
            random.seed(seed)

    @staticmethod
    def init_adjacency_list(data):
        # Number of vertices
        total_vertices = len(data)
        # Initialise
        vertices = [set([]) for _ in range(total_vertices)]
        edges = []
        edge_index = 0
        # Iterate through vertices
        for vertex in data:
            vertex_index = vertex[0]
            opposing_vertices = vertex[1:]
            for opposing_vertex in opposing_vertices:
                if opposing_vertex > vertex_index:
                    # create edge
                    edges.append([vertex_index, opposing_vertex])
                    # append edges to vertices
                    vertices[vertex_index - 1].add(edge_index)
                    vertices[opposing_vertex - 1].add(edge_index)
                    edge_index += 1
        return vertices, edges

    def select_edge(self):
        random_selection = random.randint(0, len(self.living_edges) - 1)
        return self.living_edges[random_selection]

    def contraction(self):
        contract_edge = self.select_edge()
        contract_vertices = self.edges[contract_edge]
        v1 = min(contract_vertices)
        v2 = max(contract_vertices)
        e1 = self.vertices[v1 - 1]
        e2 = self.vertices[v2 - 1]
        logging.debug('Contracting vertices: {}, {} ({}, {})'.format(v1, v2, e1, e2))
        # Combine edges into one set and remove circular references
        e3 = (e1 | e2) - (e1 & e2)
        # The vertex with the minimum index will become the contracted vertex, the other vertex will loose all edges.
        self.vertices[v1 - 1] = e3
        self.vertices[v2 - 1] = set([])
        # Update the edges by iterating through all edges connected to either of the pre contracted vertices
        for edge in (e1 | e2):
            # Rename references to contracted vertex (v2)
            self.edges[edge] = [v1 if vertex == v2 else vertex for vertex in self.edges[edge]]
            # Remove circular references
            if self.edges[edge][0] == self.edges[edge][1]:
                logging.debug('Removing edge: {} (Circular reference)'.format(edge))
                logging.debug(self.living_edges)
                self.edges[edge] = []
                self.living_edges.remove(edge)
                ##### ERROR HERE #######3
                # self.living_edges.pop(contract_edge)
                # print(v1, v2, e1, e2, e3)
                # print(self.vertices)
                # print(self.edges)
                # print(self.living_edges)

                # print(len(self.living_edges))

    def estimate_min_cut(self):
        for i in range(0, len(self.vertices) - 2):
            logging.debug('Starting contraction: {}'.format(i + 1))
            self.contraction()
        # find min cut
        cuts = 0
        for edge in self.edges:
            if len(edge) == 2:
                cuts += 1
        return cuts


def run_min_cut(data):
    n = len(data)
    min_cut = n
    trials = int(n * math.log(n, math.e))
    logging.info('Trials: {}'.format(trials))
    for i in range(0, trials):
        al = AdjacencyList(data, seed=i)
        possible_min_cut = al.estimate_min_cut()
        if possible_min_cut < min_cut:
            min_cut = possible_min_cut
        logging.info(
            'Iteration: {}, Estimated min cut: {}, Current best min cut: {}'.format(i, possible_min_cut, min_cut))
    return min_cut


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    data = load_data()
    print(run_min_cut(data))
