import heapq
import itertools

_SERVER_MASK: int = 0x1FFFF
_SHIFT: int = 17


class Solution:
  """Solution for LeetCode 1606: Find Servers Handling Most Requests."""

  def busiestServers(  # pylint: disable=invalid-name
      self, k: int, arrival: list[int], load: list[int]
  ) -> list[int]:
    """Finds the IDs of the busiest servers that handled the most requests.

    Bypasses the first min(n, k) requests via the cold-start prefix invariant,
    packs (end_time, server_id) into a single integer for the busy min-heap,
    and projects freed servers onto the monotonic virtual ring interval
    [i, i + k - 1] via i + (s - i) % k.

    Args:
      k: The number of servers (1 <= k <= 10^5).
      arrival: Strictly increasing arrival times of requests.
      load: Processing duration of each request.

    Returns:
      A list of server IDs that handled the maximum number of requests.
    """
    n: int = len(arrival)
    if n <= k:
      return list(range(n))

    counts: list[int] = [1] * k
    busy: list[int] = [
        ((arrival[i] + load[i]) << _SHIFT) | i for i in range(k)
    ]
    heapq.heapify(busy)
    available: list[int] = []

    heappop = heapq.heappop
    heappush = heapq.heappush

    for i, (t, d) in enumerate(
        zip(
            itertools.islice(arrival, k, None),
            itertools.islice(load, k, None),
        ),
        k,
    ):
      limit: int = (t + 1) << _SHIFT
      while busy and busy[0] < limit:
        s: int = heappop(busy) & _SERVER_MASK
        heappush(available, i + (s - i) % k)

      if available:
        s = heappop(available) % k
        counts[s] += 1
        heappush(busy, ((t + d) << _SHIFT) | s)

    max_reqs: int = max(counts)
    return [s for s, c in enumerate(counts) if c == max_reqs]

  # Follows Google style guide snake_case convention as an alias.
  busiest_servers = busiestServers