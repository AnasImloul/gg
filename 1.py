from typing import List
import sys
import heapq

dp = dict()

operations = {
    "PROTON": (1, 0),
    "NEUTRON": (0, 1),
    "ALPHA": (-2, -2)
}


def solve(protons_start: int, neutrons_start: int, protons_target: int, neutrons_target: int,
          unstable_isotopes: List[List[int]]) -> List[str]:
    unstables = set()
    for x, y in unstable_isotopes:
        unstables.add((x, y))

    current = (protons_start, neutrons_start)
    target = (protons_target, neutrons_target)

    # use djiktra to return the shortest path from start to target using the operations
    q = [(0, current, [])]
    while q:
        cost, current, path = heapq.heappop(q)
        if current == target:
            return path

        if current in dp:
            continue

        dp[current] = cost

        for op, (p, n) in operations.items():
            new = (current[0] + p, current[1] + n)
            if new[0] < 0 or new[1] < 0 or new[0] >= 30 or new[1] >= 20:
                continue
            if new not in dp and new not in unstables:
                heapq.heappush(q, (cost + 1, new, path + [op]))

    return []

print(solve(8, 4, 9, 5, [[8, 3], [9, 4], [8, 5]]))
