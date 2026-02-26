# Reverse String

word = str(input("Enter a word "))
alpha = []

for i in word:
    alpha.append(i)

print(alpha)
length = len(alpha)
print(length)
newalpha = []
for j in range(length):

    newalpha.append(alpha[length -1 -j])

print(newalpha)