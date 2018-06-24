from bst import *
def in_order_traversal():
    root = insertBSTElements()
    traverse_left_subtree(root.left)
    print(str(root.data), end=" -> ")
    traverse_right_subtree(root.right)