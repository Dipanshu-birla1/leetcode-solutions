
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: Euler tour and parent/depth
        stack = [(0, 0, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))
                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting table
        up = [[0] * n for _ in range(LOG)]
        up[0] = parent[:]

        for k in range(1, LOG):
            for u in range(n):
                up[k][u] = up[k - 1][up[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = up[k][u]
                diff >>= 1
                k += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree for range XOR updates, point queries
        bit = [0] * (n + 2)

        def add(i, val):
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def range_xor(left, right, val):
            add(left + 1, val)
            add(right + 2, val)

        def point_query(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        values = [1 << (ord(c) - ord('a')) for c in s]

        # Each node's character affects root-prefix masks
        # of every node in its subtree.
        for u in range(n):
            range_xor(tin[u], tout[u], values[u])

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_val = 1 << (ord(parts[2]) - ord('a'))

                delta = values[u] ^ new_val
                range_xor(tin[u], tout[u], delta)
                values[u] = new_val

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask = (
                    point_query(tin[u])
                    ^ point_query(tin[v])
                    ^ values[w]
                )

                answer.append((mask & (mask - 1)) == 0)

        return answer
