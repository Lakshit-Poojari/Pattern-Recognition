# Count Frequency of Numbers

num = int(input("Enter Number of element in list "))
numbers = []
frequency = {}

i = 1
for i in range(num):
    value = int(input("Enter the value "))
    numbers.append(value)
    i+=1

print(numbers)

for j in numbers:
    if j in frequency:
        frequency[j] += 1
    else:
        frequency[j] = 1

print(frequency) 