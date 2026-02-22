def non_decreasing(nums):
    if not nums:
        return False
    counter = 0
    for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1]:
            counter += 1
            if counter > 1:
                return False
            if index > 0 and nums[index - 1] > nums[index + 1]:
                nums[index + 1] = nums[index]

    return counter == 1


nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))

nums = [3, 4, 1, 2]
print(non_decreasing(nums))
