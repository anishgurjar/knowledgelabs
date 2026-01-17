class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
    
#Given a preorder sequence, construct a tree
def construct(preorder_sequence):
    i = -1
    def _construct():
        nonlocal i

        i+=1

        if(preorder_sequence[i] == -1):
            return None

        root = TreeNode(preorder_sequence[i])

        root.left = _construct()
        root.right = _construct()

        return root
    return _construct()

preorder_sequence = [1,2,-1,-1,3,4,-1,-1,5,-1,-1]
root = construct(preorder_sequence)
print(root.val, root.left.val, root.right.val)

def traverse(root):
    res = []
    def _traverse(root):
        nonlocal res
        if not root:
            res.append(-1)
            return
        
        res.append(root.val)

        _traverse(root.left)
        right = _traverse(root.right)
    
    _traverse(root)

    return res

print(traverse(root))
