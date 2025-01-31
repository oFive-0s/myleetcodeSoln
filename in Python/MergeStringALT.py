class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        len1, len2 = len(word1), len(word2)
        i = 0

        # Merge characters alternately
        while i < len1 and i < len2:
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1

        # Append the remaining part of the longer word
        if i < len1:
            merged.append(word1[i:])
        elif i < len2:
            merged.append(word2[i:])

        return "".join(merged)

# Example usage:
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))   # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))   # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))   # Output: "apbqcd"

'''Complexity Analysis:
   Time Complexity : O(N), where N = length of the longer word.
   Space Complexity: O(N), where N = the length of the longer word.'''