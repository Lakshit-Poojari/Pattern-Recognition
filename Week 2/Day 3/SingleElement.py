# Single Element

nums = [10]
target = 10
left = 0
right =len(nums)-1

while left <= right:
    mid =(left +right)//2

    if nums[mid] == target:
        print("Position of target is ", mid)
        break
    elif nums[mid] < target:
        left =target-1
    elif nums[mid] > target:
        right = target-1