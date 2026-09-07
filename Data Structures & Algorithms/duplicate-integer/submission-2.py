class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for i in range(len(nums)):
            if nums[i] in dict_:
                dict_[nums[i]] = dict_[nums[i]] + 1
            else:
                dict_[nums[i]] = 0
        for i in nums:
            if dict_[i] > 0:
                return True
        return False



        