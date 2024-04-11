from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(length):
        for k in range(i + 1, length):
            if nums[i] + nums[k] == target:
                return [i, k]
    pass
