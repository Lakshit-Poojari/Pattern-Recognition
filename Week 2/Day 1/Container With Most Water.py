# Container With Most Water

# water = width × min(height[left], height[right])
# width = right - left (indices)

# [1,8,6,2,5,4,8,3,7]
#  L               R


height = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(height) -1

max_water = 0


while left < right:
    width = right-left
    water = width * min(height[left], height[right])
    print(water)

    if water > max_water:
        max_water = water
    if height[left] < height[right]:
        left +=1
    else:
        right -=1


print(max_water)