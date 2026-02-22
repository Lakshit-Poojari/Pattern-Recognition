# Detect Duplicate

numbers = []
num = int(input("Enter Number of Element "))
frequency ={}

for i in range(num):
    values = int(input("Enter Values in list "))
    numbers.append(values)

print(numbers)

for j in numbers:
    if j in frequency:
        frequency[j] += 1 
        print("duplicate",  j)
        break
    else:
        frequency[j] = 1

