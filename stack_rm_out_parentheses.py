# Input: s = "(()())(())"
# Output: "()()()"

def removeOuterParentheses(S):
        res = []
        opened = 0
        for c in S:
            if c == '(' and opened > 0: 
                res.append(c)
            if c == ')' and opened > 1: 
                res.append(c)
           
            if c == '(':
                opened += 1 
            else:
                opened -= 1
        return "".join(res)


print(removeOuterParentheses("(()())(())"))