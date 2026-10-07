class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}        
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        
        arr = []
        for key, value in count.items():
            arr.append([value, key])
        arr.sort()

        res = []
        while k != 0:
            res.append(arr.pop()[1])
            k = k - 1

        return res