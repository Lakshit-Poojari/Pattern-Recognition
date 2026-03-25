# Subarray Sum = K

nums = [3,1,4,1,5,9]
k =5

count = 0
prefix_sum = {0:1}
current_sum = 0

for num in nums:
    current_sum += num

    if current_sum -k in prefix_sum:
        count += prefix_sum[current_sum-k]

    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0 )+1

print(count)