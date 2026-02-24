# Most Frequent Element

num = int(input("Enter number of element "))
numbers = []
frequency = {}
count = 0
for values in range(num):
    value = int(input("Enter value of element"))
    numbers.append(value)
    count+=1

print(numbers)

for Val in numbers:
    if Val in frequency :
        frequency[Val] +=1

    else :
        frequency[Val] = 1

print(frequency)

highest_value = 0
most_frequent = None
for key, value in frequency.items():
    if value > highest_value:
        highest_value = value
        most_frequent = key

print(f"{most_frequent} is most frequent value {highest_value}")