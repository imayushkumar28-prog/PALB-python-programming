class Solution:
    def combinationSum(self, n, k):  # swap parameter order
        result = []
        
        def backtrack(start, path, target):
            if len(path) == k:
                if target == 0:
                    result.append(path[:])
                return
            
            for num in range(start, 10):
                if num > target:
                    break
                path.append(num)
                backtrack(num + 1, path, target - num)
                path.pop()
        
        backtrack(1, [], n)
        return result
