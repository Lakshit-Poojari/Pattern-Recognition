# Closest Pair

num_ele = int(input("Ënter Number of Element "))

nums= []

for ele in range(num_ele):
    value = int(input("Enter value "))
    nums.append(value)

print(nums)
target = int(input("Target value is "))

closest_diff = float('inf')
best_pair = None

for i in range(len(nums)):
    for j in range(i+1, len(nums)):

        pair_sum = nums[i] + nums[j]
        diff = abs(target - pair_sum)

        if diff < closest_diff:
            closest_diff = diff
            best_pair = (nums[i], nums[j])

print("Closest pair:", best_pair)
print("Difference:", closest_diff)