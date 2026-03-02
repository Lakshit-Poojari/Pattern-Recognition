# Window Creation

user_input = input("Enter number between space ")
user_List = list(map(int, user_input.split()))
print(user_List)
k =3

for i in range(len(user_List) -k +1):
    window = user_List[i:i+k]
    left = i
    right = i+k-1
    print(f"{window} start point is {left} end ponit is {right}")