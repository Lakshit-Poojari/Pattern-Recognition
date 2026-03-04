# Longest substring with exactly K distinct characters

word = input("Enter word ")
k =3
max_length = 0 
left = 0
frequency = {}

for right in range(len(word)):
    frequency[word[right]] = frequency.get(word[right], 0) +1

    while len(frequency) == k:
        frequency[word[left]] -= 1
        if frequency[word[left]] == 0:
            del(frequency[word[left]])
        
        left +=1

    max_length = max(max_length, right - left + 1)

print(frequency)
print(max_length)