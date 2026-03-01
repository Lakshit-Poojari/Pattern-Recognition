# Frequency Controlled Sliding Window

word = str(input("Enter a word "))
k = 2
char_count = {}
left = 0
max_lenght = 0

for right in range(len(word)):
    char = word[right]
    char_count[char] = char_count.get(char, 0) +1

    while len(char_count) > k:
        left_char = word[left]
        char_count[left_char] -=1

        if char_count[left_char] == 0:
            del char_count[left_char]

        left +=1

    max_lenght = max(max_lenght, right - left +1)

print("Max length is ", max_lenght)