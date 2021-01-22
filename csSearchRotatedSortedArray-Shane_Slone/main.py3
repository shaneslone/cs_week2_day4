def csSearchRotatedSortedArray(nums, target):
    if target > len(nums) or target < 1:
        return -1
    elif nums[0] == target:
        return 0
    elif nums[0] < target:
        return target - nums[0]
    else: 
        return target + (len(nums) - nums[0])

