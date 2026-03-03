# max window sum

user_input = input("Enter values with space in between ")
input_list = list(map(int, user_input.split()))
k =3
print(input_list)
window_sum = 0 
max_sum = window_sum
for i in range(k):
    window_sum += input_list[i]

print(window_sum)

for i in range(1, len(input_list) -k +1):
    leaving = input_list[i-1]
    entering = input_list[i +k -1]

    window_sum = window_sum -leaving + entering
    print(window_sum)

    if max_sum < window_sum:
        max_sum = window_sum

print("Max sum is ", max_sum)