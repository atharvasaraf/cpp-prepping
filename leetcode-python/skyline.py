def getSkyline(buildings):
    h = sorted(buildings, key= lambda x: x[0], reverse=True)
    max_x = max([x[1] for x in buildings])
    results = [0]* max_x

    for start, end, height in h:
        for i in range(start, end+1, 1):
            results[i] = max(results[i], height)
    
    curr_height = 0
    ans = []
    for i in range(results):
        if results[i] != curr_height:
            ans.append([i, results[i]])
            curr_height = results[i]
    return ans

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
getSkyline(
    buildings=buildings
)
