'''Given a garden with n flowers planted in a row, that is represented by an array arr[], where arr[i] denotes the height of the ith flower.
You will water them for k days. In one day you can water w continuous flowers. Whenever you water a flower its height increases by 1 unit. 
You have to maximize the minimum height of all flowers after  k days of watering.
'''
class Solution:
  def maxMinHeight(self, arr, k, w):

        n = len(arr) 

        def ok(mi, k):
            nonlocal w, n
            diff = [0]*n 
            diff[0] = arr[0]
            for i in range(1, n):
                diff[i] = arr[i] - arr[i-1]
            
            v = 0
            for i in range(n):
                v += diff[i]
                if v < mi:
                    needed = mi - v 
                    k -= needed 
                    if k < 0:
                        return False
                    diff[i] += needed 
                    v += needed
                    if i+w < n:
                        diff[i+w] -= needed 
            return True
            
                
        lo, hi = min(arr), max(arr)+k+1
        while lo < hi:
            mi = hi - (hi - lo)//2 
            if ok(mi, k):
                lo = mi 
            else:
                hi = mi - 1
        
        return lo
