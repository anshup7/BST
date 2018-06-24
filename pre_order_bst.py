from bst import *
def pre_order_traversal():
    root = insertBSTElements()
    print(str(root.data), end=" -> ")
    traverse_left_subtree(root.left)
    traverse_right_subtree(root.right)