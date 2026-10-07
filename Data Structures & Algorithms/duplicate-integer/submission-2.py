class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) <  len(nums)     
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
        
    #     return False O(n2) time complexity
        # my_map = {}
        # for i in range(len(nums)):
        #     if nums[i] in my_map.values():
        #         return True
        #     my_map[i] = nums[i]
        
        # return False O(n)





        