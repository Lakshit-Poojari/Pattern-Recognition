# Search in Rotated Sorted Array

nums = [4,5,6,7,0,1,2]
target = 0
left = 0
right =len(nums) -1
found = False

while left <= right:
    mid = (left +right) // 2

    if nums[mid] == target:
        print("Position of Target is ", mid)
        found = True

    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid -1
        else:
            left = mid +1
    else:
        if nums[right] <= target < nums[mid]:
            left = mid + 1
        else:
            right = mid -1

if not found:
    print("no element")