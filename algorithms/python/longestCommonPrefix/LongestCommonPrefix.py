# Source : https://leetcode.com/problems/longest-common-prefix/
# Author : Kayn
# Date   : 2021-04-18

##########################################################################
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
#
# 	0 <= strs.length <= 200
# 	0 <= strs[i].length <= 200
# 	strs[i] consists of only lower-case English letters.
##########################################################################

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i, c in enumerate(min(strs)):
            for s in strs:
                if s[i] != c:
                    return min(strs)[:i]

        return min(strs)
