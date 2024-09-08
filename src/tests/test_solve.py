import networkx as nx

from four_color import solve_four_color


def test_solve_four_color():
    g = nx.complete_graph(4)
    actual = solve_four_color(g)
    assert len(set(actual.values())) == 4
