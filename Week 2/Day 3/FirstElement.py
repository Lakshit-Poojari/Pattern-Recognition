# First Element

nums = [1, 2, 3, 4, 5]
target = 1
left =0 
right = len(nums) -1

while left <= right:
    mid = (left + right)//2

    if nums[mid] == target:
        print("Position is of target is", mid)
        break
    elif nums[mid] < target:
        left =target-1
    elif nums[mid] > target:
        right = target-1