# Last Element

nums = [1, 2, 3, 4, 5]
target = 5

left = 0
right = len(nums) -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Position of Target is ", mid)
        break

    elif nums[mid] > target:
        right = mid-1
    elif nums[mid] < target:
        left = mid+1