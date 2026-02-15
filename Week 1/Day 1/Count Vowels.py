# Count Vowels

word = str(input("Enter a word "))

vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

count = 0
for i in word:
    if i in vowels:
        count += 1
        print(i)
    # else:

print("Number of vowels are", count)