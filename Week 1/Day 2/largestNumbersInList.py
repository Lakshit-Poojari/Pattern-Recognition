# Largest numbers in List

arr = []
arr_limit = int(input("Enter Number of Element "))

larger_number = []
num = int(input("Enter Number to be Compared "))
count= 1
for i in range(arr_limit):
    ele = int(input(f"Enter Element number {count} "))
    arr.append(ele)
    count+=1

print(arr)
for a in arr:
    if a > num:
        larger_number.append(a)

print(f"Element Greater than {num} is {larger_number}")