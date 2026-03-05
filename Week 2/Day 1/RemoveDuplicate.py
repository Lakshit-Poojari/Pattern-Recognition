# Remove Duplicate 

user_input = input("Enter Number With Space in between ")
input_list = list(map(int, user_input.split()))
print(input_list)
left = 0

for right in range(1, len(input_list)):
    if input_list[left] != input_list[right]:
        left+=1
        input_list[left] = input_list[right]

print(input_list[:left+1])