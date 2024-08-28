class TreeNode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def InorderTraversal(root):
    answer=[]
    inorderTraversal(root,answer)
    return answer
def InorderTraversalUtil(root):
    if root is None:
        return
    InorderTraversalUtil(root.left,answer)
    print inorderTraversal(root.answer)
    InorderTraversalUtil(root.right,answer)
root=node(4)
root.left=node(2)
root.right=node(5)
root.left.left=node(1)
root.left.right=node(3)
