
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3

def max_depth(s):
    res = 0
    temp = 0
    for c in s:
        if c == "(":
            temp += 1
            res = max(res, temp)
        if c == ")":
            temp -= 1
            
    return res

print(max_depth("(1+(2*3)+((8)/4))+1)"))