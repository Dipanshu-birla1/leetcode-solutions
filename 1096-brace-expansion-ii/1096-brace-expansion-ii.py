class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def parse(i):
            res = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    group, i = parse(i + 1)
                    current = {a + b for a in current for b in group}

                elif expression[i] == ',':
                    res |= current
                    current = {""}
                    i += 1

                else:
                    current = {a + expression[i] for a in current}
                    i += 1

            res |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return res, i

        result, _ = parse(0)

        return sorted(result)