# Find Largest Number in a List

list = []
num = int(input("Enter Number of Element "))

count = 1
for i in range(num):
    ele = int(input(f"Enter Element number {count} :- "))
    list.append(ele)
    count += 1
print(list)
max_num = list[0]
second_largest = None

for a in list:
    if a > max_num:
        second_largest = max_num
        max_num = a
    elif second_largest is None or a > second_largest:
        if a != max_num:
            second_largest = a

print("largest is", max_num)
print("second largest is", second_largest)