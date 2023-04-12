def func(s):
    c = s[0]
    count = 0
    results = ""
    for idx, char in enumerate(s):
        if char != c:
            results = results + f"{count}{c}"
            c = char
            count = 1
        else:
            count += 1
    results = results + f"{count}{char}"
    return results

s = "332251"
func(s)