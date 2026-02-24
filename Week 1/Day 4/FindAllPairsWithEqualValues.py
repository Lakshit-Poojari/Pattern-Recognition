num_list = int(input("Enter number of Ele in List "))

ele_list = []

for ele in range(num_list):
    ele = int(input("Enter value "))
    ele_list.append(ele)

print(ele_list)

for i in range(len(ele_list)):
    for j in range(i+1, len(ele_list)):
        if ele_list[i] == ele_list[j]:
            print(f"{ele_list[i]} has a pair with {ele_list[j]}")
