user_input = input("Enter number between space ")
user_List = list(map(int, user_input.split()))
print(user_List)
k =3

for i in range(len(user_List)+1 -k):
    window = user_List[i: i+k]
    print(window)