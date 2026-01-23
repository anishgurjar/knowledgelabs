from adjacency_list_implementation.graph import Graph
import pytest

@pytest.mark.parametrize(
    "n, edges, directed, expected",
    [
        (3, [[0,1],[1,2]], False, {0:[1], 1:[0,2], 2:[1]}),
        (3, [[0,1],[1,2]], True,  {0:[1], 1:[2], 2:[]}),
        (1, [], False, {0:[]}), #edgeless graphs
    ]
)
def test_build_adj_list(n, edges, directed, expected):
    g = Graph(n, edges, directed)
    assert g._graph == expected

@pytest.mark.parametrize(
    "edges, node, expected",
    [
        ([[0,1],[1,2]], 1, [0,2]),
        ([[0,1]], 0, [1]),
        ([], 0, []),
    ]
)
def test_neighbors(edges, node, expected):
    g = Graph(3, edges)
    assert sorted(g.neighbors(node)) == sorted(expected)

@pytest.mark.parametrize(
    "edges, start, expected",
    [
        ([[0,1],[1,2]], 0, [0,1,2]),
        ([[0,1],[0,2]], 0, [0,1,2]),
    ]
)
def test_dfs_recursive(edges, start, expected):
    g = Graph(3, edges)
    assert g.dfs_recursive(start) == expected

@pytest.mark.parametrize(
    "edges, start, expected",
    [
        ([[0,1],[1,2]], 0, [0,1,2]),
        ([[0,1],[0,2]], 0, [0,1,2]),
    ]
)
def test_dfs_iterative(edges, start, expected):
    g = Graph(3, edges)
    assert g.dfs_iterative(start) == expected

@pytest.mark.parametrize(
    "edges, start, expected",
    [
        ([[0,1],[1,2]], 0, [0,1,2]),
        ([[0,1],[0,2]], 0, [0,1,2]),
    ]
)
def test_bfs(edges, start, expected):
    g = Graph(3, edges)
    assert g.bfs(start) == expected

@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [[0,1],[1,2],[3,4]], [[0,1,2],[3,4]]),
        (3, [], [[0],[1],[2]]),
    ]
)
def test_connected_components(n, edges, expected):
    g = Graph(n, edges)
    comps = g.connected_components()
    assert sorted(map(sorted, comps)) == sorted(map(sorted, expected))

@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[0,1],[1,2],[2,0]], True),
        ([[0,1],[1,2]], False),
    ]
)
def test_cycle_undirected_dfs(edges, expected):
    g = Graph(3, edges)
    assert g.has_cycle_undirected_dfs() is expected

@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[0,1],[1,2],[2,0]], True),
        ([[0,1],[1,2]], False),
    ]
)
def test_cycle_undirected_bfs(edges, expected):
    g = Graph(3, edges)
    assert g.has_cycle_undirected_bfs() is expected

@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[0,1],[1,2],[2,0]], True),
        ([[0,1],[1,2]], False),
    ]
)
def test_cycle_directed_dfs(edges, expected):
    g = Graph(3, edges, directed=True)
    assert g.has_cycle_directed_dfs() is expected

@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[0,1],[1,2]], [2,1,0]),
    ]
)
def test_topo_sort_dfs(edges, expected):
    g = Graph(3, edges, directed=True)
    assert g.topo_sort_dfs() == expected

@pytest.mark.parametrize(
    "edges, expected",
    [
        ([[0,1],[1,2]], [0,1,2]),
    ]
)
def test_topo_sort_bfs(edges, expected):
    g = Graph(3, edges, directed=True)
    assert g.topo_sort_bfs() == expected

@pytest.mark.parametrize(
    "edges, src, dst, expected",
    [
        ([[0,1],[1,2]], 0, 2, 2),
        ([[0,1]], 0, 2, -1),
    ]
)
def test_shortest_path_unweighted(edges, src, dst, expected):
    g = Graph(3, edges)
    assert g.shortest_path_unweighted(src, dst) == expected
