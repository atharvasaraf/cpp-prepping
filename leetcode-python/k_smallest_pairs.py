def kSmallestPairs(nums1, nums2, k):
    p1, p2 = 0, 0
    n1, n2 = len(nums1), len(nums2)
    results = []
    while k > 0:
        if (p1 == n1) and (p2 == n2):
            return
        elif p1 == n1:
            p1 =  0
            p2 += 1
        
        elif p2 == n2:
            p2 = 0
            p1 += 1
        results.append([nums1[p1], nums2[p2]])
        if nums1[p1] > nums2[p2]:
            p1 += 1
        else:
            p2 += 1
        
        k -= 1
    return results


nums1 = [1,2]
nums2 = [3]
k = 3
results = kSmallestPairs(
    nums1=nums1,
    nums2=nums2,
    k=k
)
print(results)