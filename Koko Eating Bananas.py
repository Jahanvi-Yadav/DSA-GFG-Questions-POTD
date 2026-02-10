'''Koko is given an array arr[], where each element represents a pile of bananas. She has exactly k hours to eat all the bananas.

Each hour, Koko can choose one pile and eat up to s bananas from it.

If the pile has atleast s bananas, she eats exactly s bananas.
If the pile has fewer than s bananas, she eats the entire pile in that hour.

Koko can only eat from one pile per hour.


Your task is to find the minimum value of s (bananas per hour) such that Koko can finish all the piles within k hours.'''
class Solution:
    def kokoEat(self, arr, k):
        left, right = 1, max(arr)
        while left<=right:
            hours = 0
            mid = (left+right)//2
            for bananas in arr:
                hours += math.ceil(bananas/mid)
            if hours <= k :
                right = mid - 1
            else:
                left = mid + 1
        return left
       
