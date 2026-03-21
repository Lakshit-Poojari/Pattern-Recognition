# Subarray Sum = K

nums = [1,8,6,2,5,8,3,7]
k =3

count = 0
current_sum = 0
prefix_count = {0:1}

for num in nums:
    current_sum += num

    if current_sum -k in prefix_count:
        count += prefix_count[current_sum -k]

    prefix_count[current_sum -k] = prefix_count.get(current_sum,0) +1

print(count)