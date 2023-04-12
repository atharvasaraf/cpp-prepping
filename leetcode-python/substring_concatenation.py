import collections

def get_all_combinations(words):
    results = set()

    def func(words, curr_permute, results):
        if len(words) == 0:
            results.add(tuple(curr_permute))
        
        for idx in range(len(words)):
            tmp_words = words[:idx] + words[idx+1:]
            curr_permute.append(words[idx])
            func(tmp_words, curr_permute, results)
            curr_permute.pop()
    
    func(words, [], results)
    return results

def findSubstring(s, words):
    import collections
    len_word = len(words[0])
    total_len = len("".join(words))
    words = collections.Counter(words)
    results = []

    for start_index in range(0, len(s) - total_len+1):
        slicee = s[start_index:start_index+total_len]
        slicee = [
            slicee[i:i+len_word] 
            for i in range(0, total_len, len_word)
        ]
        slicee = collections.Counter(slicee)
        if slicee == words:
            results.append(start_index)
    return results
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
# words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
ret = findSubstring(s, words)
print(ret)
