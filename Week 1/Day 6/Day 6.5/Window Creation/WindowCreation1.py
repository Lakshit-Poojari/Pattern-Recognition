# Window Creation

user_input = input("Enter number with space ")
input_list = user_input.split()
k =3
print("list ", input_list)

for i in range(len(input_list) - k +1):
    window = input_list[i:i+k]
    print(window)