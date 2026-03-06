# Pair Closest to Target

nums = [1,3,4,7,10]
target = 15
left = 0
right = len(nums) -1
best_pair = None
closest_diff = float("inf")

while left < right:
    current_sum = nums[left] +nums[right]
    diff = abs(target - current_sum)

    if diff < closest_diff:
        closest_diff = diff
        best_pair = (nums[left], nums[right])

    if current_sum < target:
        left += 1

    else:
        right -=1

print(best_pair)