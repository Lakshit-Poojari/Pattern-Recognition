# Two Sum in Sorted Array

number = input("Enter a Number with space in between ")
num_list = list(map(int, number.split()))
print(num_list)
target = 6
left = 0
right = len(num_list) -1

while num_list[left] != num_list[right]:

    current_sum = num_list[left] + num_list[right]
    if current_sum == target:
        print(f"Sum of {num_list[left]} and {num_list[right]} is equal to target")
        break

    elif current_sum > target:
        right -= 1

    else:
        left += 1