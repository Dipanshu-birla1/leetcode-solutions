
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n, edges, labels, k):

        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count]
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        # Starting node has one occurrence of its character
        if k < 1:
            return -1

        dist[0][1] = 0

        # cost, node, consecutive count
        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost != dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, v, new_count)
                    )

        return -1
