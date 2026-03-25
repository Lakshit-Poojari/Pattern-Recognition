# Longest Sub Array With sum = k

nums = [1,8,6,2,5,4,8,3,7]
k = 8

count = 0
prefix = {0:-1}
current_sum = 0
max_length = 0


for i in range(len(nums)):
    current_sum += nums[i]

    if current_sum - k in prefix:
        length = i - prefix[current_sum - k]
        max_length = max(max_length, length)

    # store only first occurrence
    if current_sum not in prefix:
        prefix[current_sum] = i

print(max_length)