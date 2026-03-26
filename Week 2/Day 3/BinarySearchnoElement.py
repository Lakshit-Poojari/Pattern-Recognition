# No Element Binary Search

nums = [2, 4, 6, 8, 10]
target = 5
left = 0
right = len(nums) -1
found = False

while left <= right:
    mid = (left + right)//2

    if nums[mid] == target:
        print("Position of target is ", mid)
        found =True
        break
    elif nums[mid] < target:
        left = mid+1
    elif nums[mid] > target:
        right = mid-1
if not found:
    print("-1")