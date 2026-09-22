class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        tree = [None] * (2 * size)

        def make_node(value):
            value %= k
            pref = [0] * k
            pref[value] = 1
            return pref, value

        def merge(left, right):
            lp, lprod = left
            rp, rprod = right

            pref = lp[:]

            for r in range(k):
                if rp[r]:
                    pref[(lprod * r) % k] += rp[r]

            return pref, (lprod * rprod) % k

        for i in range(size):
            if i < n:
                tree[size + i] = make_node(nums[i])
            else:
                tree[size + i] = ([0] * k, 1)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, value):
            pos += size
            tree[pos] = make_node(value)

            pos //= 2

            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        def query(l, r):
            left = None
            right = None

            l += size
            r += size

            while l <= r:
                if l % 2:
                    if left is None:
                        left = tree[l]
                    else:
                        left = merge(left, tree[l])
                    l += 1

                if r % 2 == 0:
                    if right is None:
                        right = tree[r]
                    else:
                        right = merge(tree[r], right)
                    r -= 1

                l //= 2
                r //= 2

            if left is None:
                return right
            if right is None:
                return left

            return merge(left, right)

        result = []

        for index, value, start, x in queries:
            update(index, value)

            pref, _ = query(start, n - 1)

            result.append(pref[x])

        return result