# Count Number of Two Sum

num_ele = int(input("Enter number of element "))
nums = []

for ele in range(num_ele):
    value = int(input("Enter the value "))
    nums.append(value)

print(nums)

target = int(input("Enter The target value"))

count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"{nums[i]} + {nums[j]} = {target}")
            count += 1

print(f"Total pair is {count}")