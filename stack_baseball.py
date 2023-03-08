# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

def calPoints(operations):
    result = []
    for c in operations:
        if c == "C":
            result.pop()
        elif c == "D":
            result.append(2 * result[-1])
        elif c == "+":
            result.append(result[-1] + result[-2])
        else:
            result.append(int(c))
        
        
    return sum(result)






print(calPoints(["5","2","C","D","+"]))
            
            
