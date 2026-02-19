# First Non-Repeating Character

word= str(input("Enter a word "))

frequency = {}

for alpha in word:
    if alpha in frequency:
        frequency[alpha] += 1

    else:
        frequency[alpha] = 1

print(frequency)

for alpha in word:
    if frequency[alpha] == 1:
        print("First non-repeating character:", alpha)
        break
