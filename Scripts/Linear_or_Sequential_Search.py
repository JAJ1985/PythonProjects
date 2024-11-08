def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

if __name__ == '__main__':
    nums = [2, 12, 15, 11, 7, 19, 45]
    target = 7
    print(search(nums, target))