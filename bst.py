class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


def insertBSTElements():
    root = None
    num = int(input("Enter the number of elements"))
    num_out = num
    while num_out >= 1:
        el = int(input("Enter the element for BST"))
        if root == None:
            root = Tree(el)
        else:
            temp = Tree(el)
            first = root
            num_in = num
            while num_in >= 1:
                if el < first.data and first.left != None:
                    first = first.left
                elif el > first.data and first.right != None:
                    first = first.right
                num_in -= 1
            if el < first.data:
                first.left = temp
            else:
                first.right = temp
        num_out -= 1
    return root

def traverse_right_subtree(node):
    if(node == None):
        return
    else:
        print(str(node.data), end=" -> ")
        traverse_left_subtree(node.left)
        traverse_right_subtree(node.right)

def traverse_left_subtree(node):
    if(node == None):
        return
    else:
        print(str(node.data), end=" -> ")
        traverse_left_subtree(node.left)
        traverse_right_subtree(node.right)







    


        





    
            
                


