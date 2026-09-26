class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = i + 1

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                if key in d:
                    result.append(d[key])
                else:
                    result.append('?')

                i = j + 1

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)