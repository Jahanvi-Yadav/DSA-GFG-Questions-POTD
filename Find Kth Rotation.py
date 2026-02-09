#Given an increasing sorted rotated array arr[] of distinct integers. The array is right-rotated k times. Find the value of k.
#Let's suppose we have an array arr[] = [2, 4, 6, 9], if we rotate it by 2 times it will look like this:
#After 1st Rotation : [9, 2, 4, 6]
#After 2nd Rotation : [6, 9, 2, 4]
class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            # If subarray is already sorted
            if arr[low] <= arr[high]:
                return low
            
            mid = (low + high) // 2
            next_idx = (mid + 1) % n
            prev_idx = (mid - 1 + n) % n
            
            # Check if mid is minimum
            if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
                return mid
            
            # Left part is sorted, go right
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0 
