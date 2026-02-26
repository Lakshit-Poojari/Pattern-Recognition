# Continues Tracking

word = str(input("Enter a word "))

count = 1
index = 1
for i in range(len(word) -1):
    
    if word[i] == word[i+1]:
        count +=1
        index +=1
    else:
        print(f"{word[i]} count {count}")
        count = 1
        
print(f"{word[-1]} count {count}")