def csBinarySearch(nums, target):
    def BinarySearch(nums, target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return BinarySearch(nums, target, start, mid - 1)
        else:
            return BinarySearch(nums, target, mid + 1, end)
    return BinarySearch(nums, target, 0, len(nums) - 1)
        