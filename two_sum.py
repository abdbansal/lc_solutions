class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element_index_dict = {}
        for idx, num in enumerate(nums):
            if element_index_dict.get(target - num) is not None:
                return [element_index_dict[target - num],idx]
            else:
                element_index_dict[num] = idx
        
        return []
        