# Check Palindrom 2 Pointer

word = input("Enter a word ")
left = 0
right = len(word) -1

is_palindrom = True

while left < right:
    if word[left] != word[right]:
        is_palindrom =False
        break
    left += 1
    right -= 1
        
if is_palindrom:
    print("given word is palindrome")
else: 
    print("Given word is not palindrome")