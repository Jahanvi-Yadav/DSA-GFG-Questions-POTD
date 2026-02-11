#Equalize the Towers
'''You are given an array heights[] representing the heights of towers and another array cost[] where each element represents the cost of modifying the height of respective tower.

The goal is to make all towers of same height by either adding or removing blocks from each tower.
Modifying the height of tower 'i' by 1 unit (add or remove) costs cost[i].
Return the minimum cost to equalize the heights of all the towers.'''
class Solution:
    def minCost(self, heights, costs):
        def ok(mid):
            totalCost = 0
            for _, (height, cost) in enumerate(zip(heights, costs)):
                totalCost += abs(height-mid)*cost
            return totalCost
        
        l, h = min(heights), max(heights)        
        while l <= h:
            mid = l+(h-l)//2
            
            prev = ok(mid-1)
            curr = ok(mid)
            nxt = ok(mid+1)
            
            if prev >= curr and curr <= nxt:
                return curr
                
            if prev >= curr and curr >= nxt:
                l = mid+1
            else:
                h = mid-1
        return -1
