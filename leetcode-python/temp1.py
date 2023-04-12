def trap(height) -> int:
    right_max = [0]
    left_max = []
    curr_max = 0
    for i in range(len(height)):
        left_max.append(curr_max)
        curr_max = max(height[i], curr_max)
    
    curr_max = 0
    for i in range(len(height)-1, -1, -1):
        right_max.append(curr_max)
        curr_max = max(height[i], curr_max)
    
    total_water = 0
    for i in range(len(height)):
        height_water = min(right_max[i], left_max[i])
        total_water += max(0, height_water-height[i])
        print(f"{i} : {height_water}")
    return total_water

water = [0,1,0,2,1,0,1,3,2,1,2,1]
a = trap(water)
print(a)