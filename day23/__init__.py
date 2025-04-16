import itertools

import networkx as nx


def part_1_answer(lines):
    graph = parse(lines)

    interconnected_sets_of_3 = set()

    for clique in nx.find_cliques(graph):
        if len(clique) >= 3:
            for set_of_3 in itertools.combinations(clique, 3):
                if any(computer.startswith("t") for computer in set_of_3):
                    interconnected_sets_of_3.add(tuple(sorted(set_of_3)))

    return len(interconnected_sets_of_3)


def part_2_answer(lines):
    graph = parse(lines)

    max_clique = max(nx.find_cliques(graph), key=len)
    return ",".join(sorted(max_clique))


def parse(lines):
    connections = [tuple(line.split("-")) for line in lines]
    return make_graph(connections)


def make_graph(connections):
    graph = nx.Graph()
    for a, b in connections:
        graph.add_edge(a, b)
    return graph
