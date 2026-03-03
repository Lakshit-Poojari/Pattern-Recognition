# Dyanamic Sliding Window

user_input = input("Enter values With space in between ")
input_list = list(map(int, user_input.split()))
left  = 0
print(input_list)

for right in range(len(input_list)):
    window += input_list[right]

    