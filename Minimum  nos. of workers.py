class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        # Convert arr into valid intervals
        for i in range(n):
            if arr[i] != -1:
                start = max(0, i - arr[i])
                end = min(n - 1, i + arr[i])
                intervals.append((start, end))
        
        # Sort intervals by starting time
        intervals.sort()
        
        count = 0
        i = 0
        curr_end = 0
        max_reach = 0
        
        # Cover the range [0, n-1]
        while curr_end < n:
            
            # Extend coverage as far as possible
            while i < len(intervals) and intervals[i][0] <= curr_end:
                max_reach = max(max_reach, intervals[i][1])
                i += 1
            
            # If we cannot extend coverage
            if max_reach < curr_end:
                return -1
            
            count += 1
            curr_end = max_reach + 1
        
        return count
