# Set Dyanamic Sliding Window

num_input = input("Enter value with space in between ")
num_set = set()
left = 0
max_length = 0

for right in range(len(num_input)):

    while num_input[right] in num_set:
        num_set.remove(num_input[left])
        left +=1

    num_set.add(num_input[right])
    max_length = max(max_length, right -left +1)

print("Maximum length is ", max_length)