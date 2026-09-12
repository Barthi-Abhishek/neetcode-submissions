class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        L = []
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d:
                L.append(d[comp])
                L.append(i)
                return L
            d[nums[i]] = i
        
        


        