from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        #monotonically decreasing queue. basically has values that are arranged in descending order
        q = deque()
        while r<len(nums):
            #if deque has elements and those elements are less than the current element we are checking then pop from right continuously THEN append the current element.
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            #if the element we are currently checking has an index that is greater than the leftmost index value of window then pop that value from window
            if l>q[0]:
                q.popleft()
            
            #only append value if window size is atleast "k" then increment left pointer
            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res