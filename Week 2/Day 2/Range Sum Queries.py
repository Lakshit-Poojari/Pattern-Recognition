# Range Sum Queries

nums = [2,4,6,8,10]
prefix = [0] * len(nums)
prefix[0] = nums[0]
print(prefix)

for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

left = 2
right = 4

if left == 0:
    result = prefix[right]

else:
    result = prefix[right] - prefix[left -1]

print(result)