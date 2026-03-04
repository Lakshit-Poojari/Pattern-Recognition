# Set Dyanamic Sliding Window

word = input("Enter value with space in between ")
left = 0
max_length = 0
char_set = set()

for right in range(len(word)):

    while word[right] in char_set:
        char_set.remove(word[left])
        left +=1

    char_set.add(word[right])
    max_length = max(max_length, right -left +1)
print(max_length)