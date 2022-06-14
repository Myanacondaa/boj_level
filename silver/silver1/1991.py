class Node:
    def __init__(self, val=' ', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: Node):
    print(root.val, end='')
    if root.left != ".":
        preorder(tree[root.left])
    if root.right != '.':
        preorder(tree[root.right])


def inorder(root: Node):
    if root.left != ".":
        inorder(tree[root.left])
    print(root.val, end='')
    if root.right != '.':
        inorder(tree[root.right])

def postorder(root:Node):
    if root.left != ".":
        postorder(tree[root.left])
    if root.right != '.':
        postorder(tree[root.right])
    print(root.val, end='')


if __name__ == "__main__":
    num = int(input())
    tree = {}
    for _ in range(num):
        root, left, right = map(str, input().split())
        tree[root] = Node(root, left, right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])





