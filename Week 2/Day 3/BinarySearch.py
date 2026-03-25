# Binary Search

nums = [1, 3, 5, 7, 9, 11]
target = 7

left = 0
right = len(nums) -1

while left <= right:
    mid = (left + right)//2
    if nums[mid] == target:
        print("Position is", mid)
        break

    elif nums[mid] < target:
        left = mid +1
    elif nums[mid] > target:
        right = mid -1