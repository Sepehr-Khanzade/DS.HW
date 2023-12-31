class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree(root, level=0):
    if root is not None:
        print_tree(root.left, level + 1)
        print('    ' * level + str(root.value))
        print_tree(root.right, level + 1)


def construct_pyramid(num_nodes):
    root = None
    node_list = []
    for i in range(num_nodes):
        node = TreeNode(i)
        node_list.append(node)
        if len(node_list) > 1:
            parent = (i + 1) // 2 - 1
            if i % 2 == 0: # left child
                node_list[parent].left = node
            else: # right child
                node_list[parent].right = node
        else:
            root = node
    return root


if __name__ == "__main__":
    root = construct_pyramid(15) #15 is an example
    print_tree(root)