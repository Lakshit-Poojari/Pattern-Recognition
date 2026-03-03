# Sum of Window Greater Than Value

user_input = input("Enter Values with space in between ")
input_list = list(map(int, user_input.split()))
k =3
print(input_list)
window_sum = 0 
max_value = int(input("Enter max_value "))

for i in range(k):
    window_sum += input_list[i]

count = 0

print(window_sum)
if window_sum >= max_value:
        count += 1

for i in range(1, len(input_list) -k +1):
    leaving = input_list[i-1]
    entering = input_list[i +k -1]
    window_sum = window_sum -leaving + entering
    print(window_sum)

    if window_sum > max_value:
        count += 1
        print(f"{window_sum} has sum greater than {max_value}")