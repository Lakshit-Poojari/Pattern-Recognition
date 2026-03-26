# Find Peak Element

nums = [1,2,9,3,4,5,6,7,8,1]
left = 0
right = len(nums) -1

while left < right:
    mid = (left + right) // 2

    if nums[mid] < nums[mid+1]:
        left = mid+1
    else:
        right = mid

print(left)