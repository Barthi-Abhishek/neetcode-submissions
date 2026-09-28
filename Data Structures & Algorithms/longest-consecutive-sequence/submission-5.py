class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first removing duplicates using set
        longseq = 0
        seen = set(nums)
        for num in seen:
            if num-1 not in seen:
                length = 1
                while num + length in seen:
                    length = length + 1
                longseq = max(length, longseq)
        return longseq

                   