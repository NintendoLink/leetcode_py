# python 3.6.4
# encoding: utf-8
"""
1160. 拼写单词
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。

 

示例 1：

输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
示例 2：

输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
所有字符串中都仅包含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    """
    思路：利用字典哈希
    """
    def countCharacters(self, words, chars):

        char_dict = {}
        for ch in chars:
            char_dict[ch] = 1 if ch not in char_dict.keys() else char_dict.get(ch) + 1

        res = 0
        for word in words:
            if self.is_learnable(word,char_dict.copy()):
                res += len(word)
        return res

    def is_learnable(self, word, char_dict):

        for ch in word:
            if ch not in char_dict.keys() or char_dict.get(ch) <=0:
                return False
            else:
                char_dict[ch] -= 1

        return True
if __name__ == '__main__':
    # words = ["hello","world","leetcode"]
    # chars = "welldonehoneyr"

    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    solution = Solution()
    print(solution.countCharacters(words, chars))

