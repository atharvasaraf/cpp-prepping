def largestRectangleArea(heights) -> int:
    curr_width = 0
    ans = 0

    ptr = 0
    running_minimum = float('inf')
    while ptr < len(heights):
        running_minimum = min(running_minimum, heights[ptr])

        area_that_ends_here = (curr_width + 1)* (running_minimum)

        if area_that_ends_here > ans:
            ans = area_that_ends_here
            curr_width += 1
        
        if ans <= heights[ptr]:
            running_minimum = heights[ptr]
            ans = heights[ptr]
            curr_width = 1
        
        ptr += 1
    return ans
heights = [9, 0]
largestRectangleArea(heights)
