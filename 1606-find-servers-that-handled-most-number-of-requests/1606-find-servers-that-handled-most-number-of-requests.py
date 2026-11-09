
from typing import List
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        size = 4 * k
        tree = [0] * size

        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, end, idx, val)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def find(node, start, end, ql):
            if end < ql or tree[node] == 0:
                return -1

            if start == end:
                return start

            mid = (start + end) // 2

            result = find(node * 2, start, mid, ql)

            if result != -1:
                return result

            return find(node * 2 + 1, mid + 1, end, ql)

        for i in range(k):
            update(1, 0, k - 1, i, 1)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                update(1, 0, k - 1, server, 1)

            if tree[1] == 0:
                continue

            start = i % k
            server = find(1, 0, k - 1, start)

            if server == -1:
                server = find(1, 0, k - 1, 0)

            update(1, 0, k - 1, server, 0)

            count[server] += 1
            heapq.heappush(busy, (time + load[i], server))

        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum]
