# Update Frequency Controlled Sliding Window

word = str(input("Enter a word "))
char_count = {}
k = 2
left = 0
max_length = 0

for right in range(len(word)):
    char = word[right]
    char_count[char] = char_count.get(char, 0) +1

    while len(char_count) > k:
        left_char = word[left]
        char_count[left_char] -=1

        if char_count[left_char] == 0:
            del char_count[left_char]

        left +=1

    if len(char_count) == k:
        max_length = max(max_length, right - left +1)

print("Max length is ", max_length)