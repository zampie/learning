'''

# BFS0
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = deque([(beginWord,1)])
        wordSet = set(wordList)

        while queue:
            curr = queue.popleft()
            curr_word = curr[0]
            curr_depth = curr[1]

            for i in range(len(curr_word)):
                for s in range(97,123):
                    new_word = curr_word[:i] + chr(s) + curr_word[i+1:]
                    if new_word == endWord:
                        return curr_depth+1

                    if new_word in wordSet:
                        queue.append((new_word,curr_depth+1))
                        wordSet.remove(new_word)

        return 0

# BFS2 超时
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = deque([(beginWord,1)])

        while queue:
            curr = queue.popleft()
            curr_word = curr[0]
            curr_depth = curr[1]

            for i in range(len(curr_word)):
                key = curr_word[:i]+curr_word[i+1:]
                j=0
                while j < len(wordList):
                    word = wordList[j]
                    if key == (word[:i] + word[i + 1:]):

                        if word == endWord:
                            return curr_depth + 1

                        queue.append((word, curr_depth + 1))
                        wordList.remove(word)
                        j -= 1

                    j+=1


        return 0
'''



from collections import deque


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# wordList = ["hot","dot","dog"]
queue = deque([(beginWord, 1)])

while queue:
    curr = queue.popleft()
    curr_word = curr[0]
    curr_depth = curr[1]

    for i in range(len(curr_word)):
        key = curr_word[:i] + curr_word[i + 1:]
        j=0
        while j < len(wordList):
            word = wordList[j]

            print(word)
            if key == (word[:i] + word[i + 1:]):

                if word == endWord:
                    print(curr_depth + 1)

                queue.append((word, curr_depth + 1))
                wordList.remove(word)
                j -= 1

            j+=1

