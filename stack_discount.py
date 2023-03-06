# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]

def final_price(A): 
    stack = []
    for i, a in enumerate(A):
        while stack and A[stack[-1]] >= a:
            A[stack.pop()] -= a
        stack.append(i)
    return A

print(final_price([8,4,6,2,3]))
