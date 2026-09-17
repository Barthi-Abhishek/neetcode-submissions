class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        #counted frquencies 
        for num in nums:
            d[num] = d.get(num,0)+1
        # created a bucket space which matches the maximum possible frequency a element can have in the nums
        bucket = [[] for _ in range(len(nums) + 1)]
        final =[]

        for num, freq in d.items():
            bucket[freq].append(num)
        for i in range(len(bucket)- 1,0,-1):
            for num in bucket[i]:
                final.append(num)
            if len(final)==k:
                return final
        print(final)
        return final





