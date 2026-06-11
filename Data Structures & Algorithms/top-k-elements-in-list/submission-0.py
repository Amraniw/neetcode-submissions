class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        sorted_nums = sorted(count, key=count.get, reverse=True) #Reverse=True to give the largest frequency first

        return sorted_nums[:k]
        
        