ENTER, EXIT = 0, 1

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # children, stored as an intrusive linked list instead of n little lists
        first_child = [-1] * n
        next_sibling = [-1] * n
        for node in range(n - 1, 0, -1):
            next_sibling[node] = first_child[parent[node]]
            first_child[parent[node]] = node

        letter_of = [ord(ch) - ord('a') for ch in s]
        subtree_size = [1] * n

        # ancestors_by_letter[L] = the nodes with letter L on the current
        # root -> here path, deepest last
        ancestors_by_letter = [[] for _ in range(26)]

        stack = [(0, ENTER)]
        while stack:
            node, phase = stack.pop()
            same_letter_path = ancestors_by_letter[letter_of[node]]

            if phase == EXIT:
                same_letter_path.pop()                      # node leaves the path
                new_parent = same_letter_path[-1] if same_letter_path else parent[node]
                if new_parent != -1:
                    subtree_size[new_parent] += subtree_size[node]
                continue

            same_letter_path.append(node)                   # node joins the path
            stack.append((node, EXIT))                      # revisit after all children
            child = first_child[node]
            while child != -1:
                stack.append((child, ENTER))
                child = next_sibling[child]

        return subtree_size