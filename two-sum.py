from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return (hash_table[complement], i)
        hash_table[num] = i
    return None


# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)
