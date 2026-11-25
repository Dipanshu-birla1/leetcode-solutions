class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        nxt, link, length = [{}], [-1], [0]
        last = 0

        for x in nums:
            cur = len(nxt)
            nxt.append({})
            link.append(0)
            length.append(length[last] + 1)

            p = last
            while p >= 0 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p >= 0:
                q = nxt[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(nxt)
                    nxt.append(nxt[q].copy())
                    link.append(link[q])
                    length.append(length[p] + 1)

                    while p >= 0 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]

                    link[q] = link[cur] = clone

            last = cur

        leaf = [True] * len(nxt)

        for v in range(1, len(nxt)):
            leaf[link[v]] = False

        return min(
            length[link[v]] + 1
            for v in range(1, len(nxt))
            if leaf[v]
        )