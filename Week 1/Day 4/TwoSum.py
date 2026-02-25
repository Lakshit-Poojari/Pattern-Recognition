# Two Sum

num_ele = int(input("Enter number of element "))
num_list =[]

for i in range(num_ele):
    value = int(input("Enter value "))
    num_list.append(value)

print(num_list)

target = int(input("Target value "))

for i in range(len(num_list)):
    for j in range (i+1 , len(num_list)):
        if num_list[i] + num_list[j] == target:
            print(f"Sum of {num_list[i]} and {num_list[j]} is {target}")
            count += 1