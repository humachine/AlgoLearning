#https://leetcode.com/problems/delete-node-in-a-bst/
''' Given the root of a BST and a key, delete the node corresponding to the key and return the new root of the tree.

Inp: key = 3
    5
   / \
  3   6
 / \   \
2   4   7

Out:
One valid answer is [5,4,6,2,null,null,7]

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].
    5
   / \
  2   6
   \   \
    4   7
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def smallestNode(self, root):
        ''' Returns the smallestNode (i.e leftmost) node present in root's subtree'''
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root, key):
        if not root:    return root
        # If key < root, then recurse for node deletion on root's left. Update root's left if required
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # If key > root, then recurse for node deletion on root's right. Update root's right if required
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # This is the node to be deleted
            if not root.left: #If there's no left, return the right child. (this also covers the case where root is a leaf)
                return root.right
            if not root.right: #Similarly, if there's no right child, return left child
                return root.left

            '''OPTIONAL: If root's left child does not contain a right child, then we just replace root with root.left. 
            root.left < root < root.right => root.left < root.right (Hence attaching root.left as root does not violate any BST properties)
            While this might be faster in certain use cases, it's best to avoid this method since it can cause the tree to become unbalanced. Deleting with inorder sucessor usually doesn't alter the balance/shape of the tree too much.
            '''
            if not root.left.right:
                root.val = root.left.val # Clone root.left's value into root 
                root.left = root.left.left # Connect root to root.left.left thereby deleting root.left
                return root

            # If both children are available, find the inorder successor (i.e smallest node of right child's subtree)
            delNode = self.smallestNode(root.right) 
            root.val = delNode.val # Swap the value of the inorder successor with root
            root.right = self.deleteNode(root.right, delNode.val) # Go on and delete the inorder successor node from its position in the right subtree
        return root

    def deleteGivenNode(self, root):
        if not root: #If there's nothing to delete (case where key is not found in tree)
            return root
        if not root.left: # If there's no left child, we can just return make the right child as the root
            return root.right
        if not root.right: #Similarly, if there's no right child, we can just attach the left child as the root
            return root.left

        delNode = self.smallestNode(root.right) #Find the inorder successor
        if delNode == root.right: #If inorder successor is the root's right, then just swap the root with root.right (i.e set root.right's left to root.left)
            root.right.left = root.left
            return root.right

        prev, curr = None, root.right
        while curr!=delNode:
            prev = curr
            curr = curr.left
        curr.left, prev.left = root.left, curr.right #Set the curr node as the new root. Hence set curr.left as root.left. Also set prev.left as curr.right
        curr.right = root.right #Finally set curr.right as root.right
        return curr

    def deleteNodeImproved(self, root, key):
        ''' We perform an improved solution of the above solution.
        Firstly, we have converted the recursive solution of above into a fully iterative solution.

        In the above solution, we find the inorder successor of the node to be deleted. We then swap the data of the inorder successor with the root node, and then delete the inorder successor.
        While this method is good for small payloads (such as only an int), it's a slow process for larger payloads.
        '''
        if not root:    return root
        originalRoot, prev = root, None

        while root and root.val!=key: #We find the node to delete
            if root.val < key:
                prev = root
                root = root.right
            elif root.val > key:
                prev = root
                root = root.left

        if not prev: #if previous was none, it means we have to delete the root of the entire tree
            return self.deleteGivenNode(root)
        elif prev.left == root: #Else, if we have to delete the left child of the parent (i.e prev), we update the left child after deletion
            prev.left = self.deleteGivenNode(root)
        else:
            prev.right = self.deleteGivenNode(root)
        return originalRoot
