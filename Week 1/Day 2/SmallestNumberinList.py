# Largest Number in List

arr =[]
num = int(input("Enter number of Element:- "))

count = 1
for i in range(num):
    value = int(input(f"Enter Element number {count} :- "))
    arr.append(value)
    count+=1

print(arr)

min_num = arr[0]

for a in arr:
    if min_num > a:
        min_num = a

print(f"Smallest Number is", min_num)