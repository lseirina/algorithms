class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


# recursive contains (the function will continue to call itself and repeat its behavior until some condition is met to return a result.)
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value  > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
# recursive insert

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
            
    def min_value(self,current_node):
        while current_node.left is not None:
           current_node = current_node.left
        return current_node.value
    
    def __delet_node(self, current_node, value):
        if current_node == None:
            return None
        if current_node.value > value:
            current_node.left = self.__delet_node(current_node.left, value)
        if current_node.value < value:
            current_node.right = self.__delet_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.right == None:
                current_node = current_node.left
            elif current_node.left == None:
                current_node = current_node.right
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delet_node(current_node.right, sub_tree_min)
            return current_node
    
    def delet_node(self, value):
        self.__delet_node(self.root, value)      
    
    
    
    

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)


my_tree.delet_node(2)

print(my_tree.min_value(my_tree.root.value))
print(my_tree.min_value(my_tree.root.left.value))
print(my_tree.min_value(my_tree.root.right.value))
