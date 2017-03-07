#https://leetcode.com/problems/binary-tree-inorder-traversal/
'''Perform in-order traversal of a tree iteratively.
'''
class Solution(object):
    def inorderTraversal(self, root):
        st, res = [], []
        # We just push all the left most nodes going from the root on to a stack
        while root:
            st.append(root)
            root = root.left

        # We pop elements from the stack and add them to the result. We then
        # add all of the left children of that node back on to the stack
        while st:
            node = st.pop()
            res.append(node.val)
            if node.right:
                node = node.right
                while node:
                    st.append(node)
                    node = node.left
        return res
