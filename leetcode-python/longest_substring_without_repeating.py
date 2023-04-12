def func(s):
    foo = set()
    if len(s) <= 1:
        return len(s)
    left_ptr = 0
    right_ptr = 1
    curr_max = 0
    foo.add(s[left_ptr])
    while left_ptr < len(s):
        if s[right_ptr] not in foo:
            foo.add(s[right_ptr])
            curr_max = max(curr_max, len(s))
        while s[left_ptr] in foo:
            left_ptr = left_ptr + 1
            
        return curr_max

print(func("abcabcbb"))
print(func("pwwkew"))
print(func("bbbbb"))