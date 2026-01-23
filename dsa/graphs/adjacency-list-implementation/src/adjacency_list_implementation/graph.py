from typing import List, Dict 
from collections import defaultdict, deque

class Graph:

    def __init__(self, n: int, edges: List[List[int]], directed:bool = False):
        self._edgelength  = n
        self._directed = directed 
        self._graph = self._construct(edges)

    
    def _construct(self, edges) -> Dict[int, List[int]]:
        adj_list = {}

        if not edges and self._edgelength > 0:
            for i in range(self._edgelength):
                adj_list[i] = []
            return adj_list

        for u, v in edges:
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v] = []
            adj_list[u].append(v)
            if not self._directed:
                adj_list[v].append(u)

        return adj_list

    def neighbors(self,node):
        return self._graph.get(node, [])

    def dfs_recursive(self, start):
        visited = set[int]()
        res = []

        def _dfs(start, res, visited):
            visited.add(start)
            res.append(start)
            for neighbor in self._graph.get(start, []):
                if neighbor not in visited:
                    _dfs(neighbor, res, visited)
            return res

        return _dfs(start, res, visited)
        
    def dfs_iterative(self, start):
        visited = set[int]()
        res = []
        stack = [start]
        while stack:
            curr = stack.pop()
            res.append(curr)
            visited.add(curr)
            for neighbor in reversed(self._graph.get(curr, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
        return res
    
    def bfs(self, start):
        queue = deque[int]()
        queue.append(start)
        res = []
        visited = set[int]()
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            res.append(curr)
            for neighbor in self._graph.get(curr, []):
                if neighbor not in visited: 
                    queue.append(neighbor)
        return res
    
    def connected_components(self):
        #intentionally not reusing prewritten dfs so I can practice

        def _dfs(start,visited, components):
            visited.add(start)
            components.append(start)
            for neighbor in reversed(self._graph.get(start, [])):
                if neighbor not in visited:
                    _dfs(neighbor, visited, components)
            return components

        visited = set[int]()
        connected_components = []
        for node in self._graph.keys():
            if node not in visited:
                components = _dfs(node, visited,[])
                connected_components.append(components)

        return connected_components

    def has_cycle_undirected_dfs(self):

        visited = set[int]()

        def _dfs(start, parent, visited):

            visited.add(start)
            for neighbor in self._graph.get(start, []):
                if neighbor not in visited:
                    if _dfs(neighbor, start, visited):
                        return True
                elif neighbor != parent:
                    return  True
            return False 
        
        for node in self._graph.keys():
            if node not in visited:
                if _dfs(node, None, visited):
                    return True

        return False

    def has_cycle_undirected_bfs(self):
        
        def _bfs(startnode,visited):
            queue = deque()
            queue.append((startnode, None))
            visited.add(startnode)
            while queue: 
                parent_child_pair = queue.popleft()
                curr_node, parent_node = parent_child_pair[0], parent_child_pair[1]

                for neighbor in self._graph.get(curr_node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_node))
                    elif neighbor != parent_node:
                        return True
            return False
        
        visited = set()
        for node in self._graph.keys():
            if node not in visited: 
                if _bfs(node, visited):
                    return True
        return False

    def has_cycle_directed_dfs(self):

        in_path = {}

        def _dfs(startnode, in_path):
            in_path[startnode] = True 
            for neighbor in self._graph.get(startnode, []):
                if neighbor not in in_path:
                    if _dfs(neighbor, in_path):
                        return True
                elif in_path[neighbor]:
                    return True
                in_path[neighbor] = False
            return False
        
        for node in self._graph.keys():
            if node not in in_path:
                if _dfs(node, in_path):
                    return True
        return False

    def topo_sort_dfs(self):
        
        def _dfs(startnode, visited, res_stack):
            
            visited.add(startnode)
            for neighbor in self._graph.get(startnode, []):
                if neighbor not in visited:
                    _dfs(neighbor, visited, res_stack)
            res_stack.append(startnode)
        
        res_stack = []
        visited = set()
        for node in self._graph.keys():
            if node not in visited:
                _dfs(node, visited, res_stack)
        return res_stack

    def topo_sort_bfs(self):

        queue = deque()
        in_degree_map = defaultdict(int)
        for node, edges in self._graph.items():
            in_degree_map[node] = 0
            for edge in edges:
                in_degree_map[edge] += 1
        print(in_degree_map)

        for node in in_degree_map.keys():
            if in_degree_map[node] == 0:
                queue.append(node)
        
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neighbor in self._graph.get(curr, []):
                in_degree_map[neighbor] -= 1
                if in_degree_map[neighbor] == 0:
                    queue.append(neighbor)
        
        return res

    def shortest_path_unweighted(self, src, dst):

        queue = deque()
        queue.append(src)
        distance = defaultdict(int)
        distance[src] = 0
        visited = set()
        visited.add(src)

        while queue:
            curr = queue.popleft()
            if curr == dst:
                return distance[curr]

            for neighbor in self._graph.get(curr, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    distance[neighbor] = distance[curr] + 1
        return -1
