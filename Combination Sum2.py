from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates easily
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # If the current number exceeds remaining target, break
                if candidates[i] > remaining:
                    break
                # Include candidates[i] and move to the next index
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()  # Backtrack

        backtrack(0, [], target)
        return result
