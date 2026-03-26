# Insert in End

nums = [1, 3, 5, 6]
target = 7
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("position is of target is ", mid)
    elif nums[mid] < target:
        left = mid +1
    else:
        right = mid -1

print("Position is ", left)