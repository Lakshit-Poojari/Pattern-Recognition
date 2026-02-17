# Character Frequency

word = str(input("Enter a Word "))
character = list(word)
unique_char = set(character)
print(character)
print(unique_char)

count = 1
for a in unique_char:
    for i in range(0, len(character)):
        if a == character[i]:

            count+=1

print(unique_char,count)
