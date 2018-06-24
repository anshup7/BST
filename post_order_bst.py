from bst import *
def post_order_traversal():
    root = insertBSTElements()
    traverse_left_subtree(root.left)
    traverse_right_subtree(root.right)
    print(str(root.data), end=" -> ")