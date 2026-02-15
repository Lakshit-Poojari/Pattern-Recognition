# Count Even Digit

num = str(input("Enter number "))

count = 0
for i in num:
    if int(i) %2 == 0 :
        count +=1

print(f"Number of Even digit is ", count)