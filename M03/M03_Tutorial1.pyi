class Solution:
    def sort012(self,arr,n):
            low = 0
            high = len(arr) - 1
            mid = 0
        
            while mid <= high:
                if arr[mid] == 0:
                    arr[low], arr[mid] = arr[mid], arr[low]
                    low += 1
                    mid += 1
                elif arr[mid] == 1:
                    mid += 1
                else:
                    arr[mid], arr[high] = arr[high], arr[mid]
                    high -= 1
        
            return arr