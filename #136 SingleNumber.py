class Solution:
    # Using XOR operator
    # Space Complexity O(1)
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result