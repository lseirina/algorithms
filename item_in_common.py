# we have two lists and we need to find if they have item in common
# The first approach is O(n^2), and it is nested loop and not efficient:
list1 = [2,4,5]
list2 = [1,3,5]
"""
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False
"""
# the second approach is O(n) is more efficient to creat dictionary for each list:
def item_in_common(list1, list2):
    my_dict = {}

    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


print(item_in_common(list1,list2))
