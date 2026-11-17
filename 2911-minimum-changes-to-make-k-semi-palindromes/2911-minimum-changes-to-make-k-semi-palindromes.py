class Solution:
  def minimumChanges(self, s: str, k: int) -> int:
    n = len(s)
    
    # Calculates the dynamic programming state.
    # `start` is the suffix start, and `k1` is the number of parts
    # to split it into.
    @functools.cache
    def DP(start, k1):
      # If there is only 1 part, there is no splitting (pivot),
      # so the answer is the number of changes to make the whole
      # suffix a semi-palindrome.
      if k1 == 1:
        return toSemiPalindrome(start, n)
      
      # Try every way to split the suffix into a part followed by
      # another suffix.
      return min(
        toSemiPalindrome(start, pivot) + DP(pivot, k1 - 1)
        # There is an implicit rule that no part must be shorter than 2.
        # We use only such pivots that won't violate the rule.
        for pivot in range(start + 2, n - (k1 - 1) * 2 + 1)
      )
    
    # Counts the minimum number of changes to make an `s` substring
    # be a semi-palindrome.
    @functools.cache
    def toSemiPalindrome(start, end):
      minChanges = math.inf
      length = end - start
      
      # Try each valid `d`. Notice that `length` itself is not a valid `d`,
      # because otherwise any string would be a semi-palindrome
      for d in range(1, length):
        if length % d != 0:
          continue

        changeCount = 0
        subLength = length // d # Length of the palindrome for each offset

        for offset in range(d):
          # `i` is the distance from the edges of the palindrome
          for i in range(subLength // 2):
            if (
              s[start + offset + d * i] !=
              s[start + offset + d * (subLength - i - 1)]
            ):
              changeCount += 1

        minChanges = min(minChanges, changeCount)

      return minChanges

    return DP(0, k)