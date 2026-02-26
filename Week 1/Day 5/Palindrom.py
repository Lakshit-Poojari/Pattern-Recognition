# Palindrom.py

word = str(input("Enter A word "))

alpha = []
for i in word:
    alpha.append(i)

print(alpha)
is_palindrome = True
for j in range(len(alpha)):
    if alpha[j] != alpha[len(alpha)-1-j]:
        is_palindrome = False
        break
    
if is_palindrome :
    print(f"{word} is palindrom")

else:
    print(f"{word} is not Palindrom")

    