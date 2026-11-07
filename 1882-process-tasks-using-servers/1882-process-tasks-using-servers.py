
from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            
            while busy and busy[0][0] <= time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            
            heapq.heappush(
                busy,
                (time + task, weight, idx)
            )

        return ans
