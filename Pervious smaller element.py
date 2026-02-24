class Solution:
    def prevSmaller(self, arr):
        stack = []
        result = []
        
        for num in arr:
            
            # Pop elements greater than or equal to current
            while stack and stack[-1] >= num:
                stack.pop()
            
            # If stack is empty, no previous smaller element
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            # Push current element into stack
            stack.append(num)
        
        return result
