'''Given a positive number n and a number d.
Find the count of positive numbers smaller or equal to n such that the difference between the number and sum of its digits is greater than or equal to given specific value d.'''
class Solution:
     def getCount(self, n, d):
        if n <= d:
            return 0
        lo, hi = 1, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid - sum(map(int, str(mid))) >= d:
                hi = mid
            else:
                lo = mid + 1
        return n - lo + 1
        
