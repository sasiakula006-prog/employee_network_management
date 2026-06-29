from collections import deque
import heapq


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            order.append(node)

            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order


def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            order.append(node)

            for neighbor, _ in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    return distances


def prim_mst(graph):
    start = next(iter(graph))

    visited = {start}
    edges = []

    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []

    while edges:
        weight, frm, to = heapq.heappop(edges)

        if to in visited:
            continue

        visited.add(to)
        mst.append((frm, to, weight))

        for neighbor, w in graph[to]:
            if neighbor not in visited:
                heapq.heappush(
                    edges,
                    (w, to, neighbor)
                )

    return mst
