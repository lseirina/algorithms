# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

def nextGreaterElement(nums1, nums2):
   
    
	if not nums2:
		return None

	mapping = {}
	result = []
	stack = []
	#stack.append(nums2[0])

	for i in range(1, len(nums2)):                  # [2,4], nums2 = [1,2,3,4]
		while stack and nums2[i] > stack[-1]:       # if stack is not empty, then compare it's last element with nums2[i]
			mapping[stack[-1]] = nums2[i]           # if the new element is greater than stack's top element, then add this to dictionary 
			stack.pop()                             # since we found a pair for the top element, remove it.
		stack.append(nums2[i])                      # add the element nums2[i] to the stack because we need to find a number greater than this
	
	for element in stack:                           # if there are elements in the stack for which we didn't find a greater number, map them to -1
		mapping[element] = -1

	for i in range(len(nums1)):
		result.append(mapping[nums1[i]])
	return result

print(nextGreaterElement([2,4,7], [1,7,2,8,5,4,2,3,4,8,5]))
                
                
    