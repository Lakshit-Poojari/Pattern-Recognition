# Subarray with sum divisible by K

nums = [1,8,6,2,5,4,8,3,7]
k = 4

current_sum = 0
prefix = {0 : 1}
count = 0

for num in nums:
    current_sum += num

    if current_sum % k in prefix:
        count += prefix[current_sum % k]

    prefix[current_sum % k] = prefix.get(current_sum  % k,0) +1
print(count)