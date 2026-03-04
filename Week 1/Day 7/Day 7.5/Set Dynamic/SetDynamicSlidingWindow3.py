# Set Dyanamic Sliding Window

user_input = input("Enter word ")
value_set = set()
left = 0
max_length = 0

for right in range(len(user_input)):
    while user_input[right] in value_set:
        value_set.remove(user_input[left])

        left +=1

    value_set.add(user_input[right])
    max_length = max(max_length , right-left +1)

print("Max length is ", max_length)