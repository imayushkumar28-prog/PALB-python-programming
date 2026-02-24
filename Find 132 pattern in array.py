class Solution:
    def has132Pattern(self, arr):
        n = len(arr)
        stack = []
        second = float('-inf')
        
        # Traverse from right to left
        for i in range(n-1, -1, -1):
            if arr[i] < second:
                return True  # Found 132 pattern
            
            while stack and arr[i] > stack[-1]:
                second = stack.pop()  # arr[k] candidate
            
            stack.append(arr[i])  # Potential arr[j]
        
        return False
