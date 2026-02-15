# Sum of Digits

num = str(int(input("Enter Number")))

m=0
for i in num:
    m =int(i)+m

print(f"sum of number is ",m)


n=1 
for i in num:
    n=n*int(i)

print(f"sum of number is ",n)