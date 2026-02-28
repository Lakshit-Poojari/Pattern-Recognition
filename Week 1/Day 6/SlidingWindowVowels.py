# Sliding Window Vowels

word = input("Enter a word ").upper()

vowels = ["A", "E", "I", "O", "U"]
window = 4

# First window
count = 0
for i in range(window):
    if word[i] in vowels:
        count += 1

print(word[0:window], "→", count)

# Sliding window
for i in range(1, len(word) - window + 1):

    leaving_char = word[i-1]
    entering_char = word[i+window-1]

    if leaving_char in vowels:
        count -= 1

    if entering_char in vowels:
        count += 1

    print(word[i:i+window], "→", count)
