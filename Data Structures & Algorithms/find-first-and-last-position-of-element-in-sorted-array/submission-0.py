class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left_index = self.findFirstOccurence(nums,target)
        right_index = self.findLastOccurence(nums,target)
        return [left_index, right_index]

    def findFirstOccurence(self,nums, target):
        res = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

    def findLastOccurence(self,nums, target):
        res = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                res = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res
        

        