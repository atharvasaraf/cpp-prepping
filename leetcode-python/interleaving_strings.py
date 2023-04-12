def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    
    if len(s1) == 0:
        return s2 == s3
    if len(s2) == 0:
        return s1 == s3
    
    p1 = 0
    p2 = 0
    p3 = 0

    while p3 < len(s3):
        if (p2 < len(s2)) and (s2[p2] == s3[p3]):
            p2 += 1
        elif (p1 < len(s1)) and (s1[p1] == s3[p3]):
            p1 += 1
        else:
            break
        p3 += 1

    if p1 < len(s1):
        return False
    if p2 < len(s2):
        return False
    
    if p3 < len(s3):
        return False

    return True

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
ans = isInterleave(
    s1 = s1,
    s2 = s2,
    s3 = s3,
)
print(ans)
