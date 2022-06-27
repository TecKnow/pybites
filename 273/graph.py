from typing import Mapping, Sequence, Tuple
import heapq
from collections import defaultdict
from math import inf

# Inspired by
# https://levelup.gitconnected.com/dijkstra-algorithm-in-python-8f0e75e3f16e

Graph = Mapping[str, Mapping[str, int]]
Path = Tuple[int, Sequence[str]]


def _find_shortest_distances_dijkstra(graph: Graph, start: str, end: str) -> Tuple[str, Mapping[str, int], Mapping[str, str]]:
    visited_nodes = set()
    node_distances = defaultdict(lambda: inf)
    node_distances[start] = 0
    parents: Mapping[str, str] = dict()
    work_heap = list()
    heapq.heappush(work_heap, (0, start))
    while (current_node := heapq.heappop(work_heap)[1]) != end:
        visited_nodes.add(current_node)
        current_distance = node_distances[current_node]
        unvisited_neighbors = {
            node: distance
            for (node, distance)
            in graph[current_node].items()
            if node not in visited_nodes}
        for neighbor, local_distance in unvisited_neighbors.items():
            new_distance = current_distance + local_distance
            if new_distance < node_distances[neighbor]:
                node_distances[neighbor] = new_distance
                parents[neighbor] = current_node
                heapq.heappush(work_heap, (new_distance, neighbor))
    return (start, node_distances, parents)


def _shortest_path_from_parents(start: str, end: str, parents: Mapping[str, str]) -> Sequence[str]:
    res = [end]
    current_node = end
    while current_node != start:
        current_node = parents[current_node]
        res.append(current_node)
    return list(reversed(res))


def shortest_path(graph: Graph, start: str, end: str) -> Path:
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """
    _, node_distances, parents = _find_shortest_distances_dijkstra(
        graph, start, end)
    route = _shortest_path_from_parents(start, end, parents)
    return node_distances[end], route
