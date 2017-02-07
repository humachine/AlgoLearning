#https://leetcode.com/problems/generate-parentheses/
'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Inp: 3
Out: [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def buildParentheses(self, op_paren, closed_paren, curr_path, res):
        # If we have exhausted n PAIRS of parens, we store the path in the result.
        if len(curr_path) == 2*self.n:
            res.append(list(curr_path))
            return

        # If we can add an open parentheses at this juncture, we do so
        if op_paren < self.n:
            curr_path.append('(')
            self.buildParentheses(op_paren+1, closed_paren, curr_path, res)
            curr_path.pop()

        # If we can add a close parentheses at this juncture, we do so too
        if closed_paren < op_paren:
            curr_path.append(')')
            self.buildParentheses(op_paren, closed_paren+1, curr_path, res)
            curr_path.pop()

    def generateParenthesis(self, n):
        # We backtrack on the number of paren pairs we need to generate
        self.n, res = n, []
        self.buildParentheses(0, 0, [], res)
        return [''.join(li) for li in res]

s = Solution()
print s.generateParenthesis(3)
print s.generateParenthesis(0)
