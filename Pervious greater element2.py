class Solution:
    def preGreaterEle(self, arr):
        stack = []
        result = []
        
        for num in arr:
            
            # Remove elements smaller than or equal to current
            while stack and stack[-1] <= num:
                stack.pop()
            
            # If stack empty → no previous greater
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            stack.append(num)
        
        return result
