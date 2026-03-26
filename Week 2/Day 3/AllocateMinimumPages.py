# Allocate Minimum Pages

books = [12, 34, 67, 90]
m = 2

low = max(books)
high = sum(books)
ans = high

while low <= high:
    mid = (low + high) // 2

    students = 1
    pages = 0

    for book in books:
        if pages + book <= mid:
            pages += book
        else:
            students += 1
            pages = book

    if students <= m:
        ans = mid
        high = mid - 1   # try smaller
    else:
        low = mid + 1    # increase capacity

print(ans)