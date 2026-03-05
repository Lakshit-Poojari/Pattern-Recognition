# Sum Based Dynamic Window

number = input("Enter a number ")
sum = 0 
k=15
left = 0

for right in range(len(number)):
    sum += number[right]

    while sum >= k:
        sum -= number[left]

        left +=1

