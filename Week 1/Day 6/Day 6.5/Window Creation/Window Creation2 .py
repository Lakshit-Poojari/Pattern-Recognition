# Window Creation
user_input = input("Enter value using space in between ")
user_list = list(map(int, user_input.split()))
k = 3
print(user_list)

for i in range(len(user_list) -k +1):
    window = user_list[i:i+k]
    print(window)