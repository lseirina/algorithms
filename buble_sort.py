def buble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(buble_sort([6,4,2,3,1,5]))
                    