def findLadders(beginWord: str, endWord: str, wordList):

    def is_adjacent(word1, word2):
        if len(word1) != len(word2):
            return False
        mismatches = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatches += 1
        return mismatches < 2

    class Node:
        def __init__(self, val):
            self.val = val
            self.neighbors = set()
        
        def add_neighbor(self, next_node):
            new_word = next_node.val
            curr_word = self.val
            if curr_word == new_word:
                return False
            if is_adjacent(new_word, curr_word) and (next_node not in self.neighbors):
                self.neighbors.add(next_node)
                return True
            else:
                return False
    
    word_to_node = {word:Node(word) for word in wordList}
    word_to_node[beginWord] = Node(beginWord)

    # build first adjacents of root Node:
    to_explore = [word_to_node[beginWord]]

    while len(to_explore):
        root_node = to_explore.pop()
        for word in wordList:
            next_node = word_to_node[word]
            if root_node.add_neighbor(next_node):
                to_explore.append(next_node)
    
    def dfs(node, search_word, curr_path, results, visited):
        if node.val == search_word:
            curr_path.append(node.val)
            results.append(curr_path)
            return
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                curr_path.append(neighbor.val)
                dfs(neighbor, search_word, curr_path, results, visited)
                curr_path.remove(neighbor.val)
                visited.remove(neighbor)
        
    results = []
    dfs(word_to_node[beginWord], endWord, [], results, set())
    min_length = 500
    for path in results:
        min_length = min(min_length, len(path))
    results = [result for result in results if len(result) == min_length]
    return results

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
findLadders(
    beginWord=beginWord,
    endWord=endWord,
    wordList=wordList
)