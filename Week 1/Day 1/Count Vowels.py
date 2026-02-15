# Count Vowels

word = str(input("Enter a word "))

vowels = ["A", "E", "I", "O", "U"]
count = 0
for i in word.upper():
    if i in vowels:
        count +=1

print(f"Number of vowels is", count)

consonant = len(word) - count 

print(f"number of consonant", consonant)


