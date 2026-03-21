# Subarray with sum divisible by K

nums = [1,8,6,2,5,4,8,3,7]
k = 4

current_sum = 0

for num in nums:
    current_sum += num

    if current_sum % k == 0:
        