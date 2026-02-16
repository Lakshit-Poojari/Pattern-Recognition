# Increasing array

arr= []
num_ele = int(input("Enter Number of Element "))

count = 1
for i in range(num_ele):
    value = int(input(f"Enter {count} number "))
    count +=1

    arr.append(value)

print(arr)
is_increasing = True

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        continue
    else:
        print("Not Increasing")
        is_increasing = False
        break

if is_increasing:
    print("Increasing")