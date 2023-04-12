def ladderLength(beginWord, endWord, wordList):
    return


def func(wordList):
    from collections import defaultdict
    adj = defaultdict(set)
    import re

    for idx, word in enumerate(wordList):
        for i in range(len(word)):
            regex_word = word[:i]+'.'+word[i+1:]
            print(regex_word)
            matches = [x for x in wordList if re.match(regex_word, x) and word != x]
            for match in matches:
                adj[match].add(word)
                adj[word].add(match)
    return adj

wordList = ["hot","dot","dog","lot","log","cog"]
ret = func(wordList)
print(ret)