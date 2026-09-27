class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()

                for c in temp:
                    stack.append(c)

            else:
                stack.append(ch)

        return ''.join(stack)