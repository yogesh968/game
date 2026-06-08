class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l= 0 
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] ==target:
                return True
            if nums[l]==nums[mid] and nums[mid] ==nums[r]:
                l = l+1
                r = r-1
                continue
            if nums[l]<=nums[mid]:
                if nums[l]<=target and nums[mid]>=target:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[r]>=nums[mid]:
                if nums[r]>=target and nums[mid]<=target:
                    l = mid+1
                else:
                    r = mid-1
        return False
