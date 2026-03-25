# Subarray Sum = K

nums = [3,1,4,1,5,9]
k =5

prefix_count ={0:1}
current_sum =0
count =0

for num in nums:
    current_sum += num

    if current_sum -k in prefix_count:
        count += prefix_count[current_sum-k]

    prefix_count[current_sum] = prefix_count.get(current_sum, 0) +1

print(count)