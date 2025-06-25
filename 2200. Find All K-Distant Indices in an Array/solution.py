from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indexes = [i for i, v in enumerate(nums) if v == key]
        result = []
        for j in indexes:
            for i in range(max(0, j-k), min(len(nums), j+k+1)):
                result.append(i)
        return sorted(set(result))

sol = Solution()     
nums1 = [3,4,9,1,3,9,5]
key1 = 9
k1 = 1
print(f"Test case 1:")  # 1,2,3,4,5,6
result1 = sol.findKDistantIndices(nums1, key1, k1)
print(f"Input: nums = {nums1}, key = {key1}, k = {k1}")
print(f"Expected: [1,2,3,4,5,6]")
print(f"Got: {result1}")
print()

# Test case 2
nums2 = [2,2,2,2,2]
key2 = 2
k2 = 2
result2 = sol.findKDistantIndices(nums2, key2, k2)
print(f"Test case 2:")  # 0,1,2,3,4 
print(f"Input: nums = {nums2}, key = {key2}, k = {k2}")
print(f"Expected: [0,1,2,3,4]")
print(f"Got: {result2}")