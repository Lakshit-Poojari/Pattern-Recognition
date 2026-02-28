# Dynamic Sliding Window

word = str(input("Enter a word "))
char_set = set()
left = 0
max_length = 0

for right in range(len(word)):
    while word[right] in char_set:
        char_set.remove(word[left])
        left +=1


    char_set.add(word[right]) 
    max_length = max(max_length, right - left + 1)

print("Longest length:", max_length)