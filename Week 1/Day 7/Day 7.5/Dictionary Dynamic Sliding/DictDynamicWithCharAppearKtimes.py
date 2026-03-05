# Longest substring where each character appears at most K times

word = input("Enter a word ")
k =3
left = 0
max_length = 0
freq = {}

for right in range(len(word)):
    freq[word[right]] = freq.get(word[right], 0) +1 

    while freq[word[right]] > k:
        freq[word[left]] -=1
        if freq[word[left]] == 0:
            del freq[word[left]]

        left +=1

    max_length = max(max_length, right - left + 1)

print(freq)
print(max_length)       