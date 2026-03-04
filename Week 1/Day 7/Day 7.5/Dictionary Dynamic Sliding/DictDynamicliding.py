# Dictionary Dynamic Sliding

word = input("Enter a word ")
alpha_freq = {}
left = 0
k =2
max_len =0
for right in range(len(word)):
    alpha_freq[word[right]] = alpha_freq.get(word[right], 0) +1

    while len(alpha_freq) > k:
        alpha_freq[word[left]] -= 1
        if alpha_freq[word[left]] == 0:
            del alpha_freq[word[left]]

        left += 1

    max_len = max(max_len, right - left + 1)

print(alpha_freq)
print(max_len)