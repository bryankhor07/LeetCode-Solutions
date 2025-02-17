# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize two stacks to perform iterative tree traversal for both trees
        stackp = []
        stackq = []

        # Push the root nodes of both trees onto their respective stacks
        stackp.append(p)
        stackq.append(q)

        # Continue the traversal as long as there are nodes to process in either stack
        while len(stackp) > 0 or len(stackq) > 0:
            # Pop nodes from both stacks
            nodep = stackp.pop()
            nodeq = stackq.pop()

            # If both nodes are not None, continue checking
            if nodep is not None and nodeq is not None:
                # Push the right and left children of both nodes onto their respective stacks
                stackp.append(nodep.right)
                stackp.append(nodep.left)
                stackq.append(nodeq.right)
                stackq.append(nodeq.left)
                # If the values of the current nodes are different, the trees are not the same
                if nodep.val != nodeq.val:
                    return False
            # If one of the nodes is None and the other is not, the trees are not the same
            elif nodep is None and nodeq is not None:
                return False
            elif nodep is not None and nodeq is None:
                return False

        # If all nodes have been processed and no differences were found, the trees are the same
        return True
    
# Time Complexity: O(N)
# Space Complexity: O(N)