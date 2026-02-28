# Sliding Window Max Vowels

word = input("Enter a word ").upper()
vowels = ["A", "E", "I", "O", "U"]
window = 4
count = 0

for i in range(window):
    if i in vowels:
        count += 1

max_num = count

print(word[0:window], "→", count)

for i in range(len(word) - window + 1):
    leaving_char = word[i-1]
    adding_char = word[i +window -1]

    if leaving_char in vowels:
        count -=1

    if adding_char in vowels:
        count += 1

    print(word[i:i+window], "→", count)

    if count > max_num:
        max_num = count

print(f"{max_num} is largest")