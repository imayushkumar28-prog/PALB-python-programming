class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n  # default: no smaller element to the right
        
        # Find next smaller element for each index
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)
        
        # Count subarrays
        count = 0
        for i in range(n):
            count += next_smaller[i] - i
        
        return count
