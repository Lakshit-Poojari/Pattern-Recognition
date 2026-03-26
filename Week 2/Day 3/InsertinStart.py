# Insert Element in Start

nums = [1, 3, 5, 6]
target = 0
left = 0
right = len(nums) -1

while left <= right:
    mid = (left +right) //2

    if nums[mid] == target:
        print("Position of target is ", mid)

    elif nums[mid] < target:
        left = mid +1

    else:
        right = mid -1
print("the position is ", left)