# sum of every window of size k

nums = [2, 1, 5, 1, 3, 2]
k = 3

for i in range(len(nums) - k +1):
    window = nums[i : k+i]
    print(window)