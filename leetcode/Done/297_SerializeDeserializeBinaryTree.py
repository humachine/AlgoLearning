#https://leetcode/com/problems/serialize-and-deserialize-binary-tree/
''' Given a binary tree, serialize it into a string and deserialize it back into a tree. '''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from Queue import Queue
class Codec:
    DELIM = ';'
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        We pick up the root and put it into a string. We use ; as the delimiter.
        We run a BFS of the tree. For each node, we add it's children into the queue.
        """
        if not root:    return []

        q, res = Queue(), [str(root.val)]
        q.put(root)
        while not q.empty(): #While there are nodes yet to be serialized, we poll the queue
            node = q.get()
            res.append(str(node.left.val) if node.left else '')
            res.append(str(node.right.val) if node.right else '')
            if node.left: #If we had seen a node.left, we add it to the queue
                q.put(node.left)
            if node.right:
                q.put(node.right)
            # Below is an alternate map-filter methodology to perform the same action
            # x = filter(lambda x: x is not None, [node.left, node.right])
            # if x:   map(q.put, x)
        return self.DELIM.join(res)

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        Here, we begin with the root node. We scroll through the serialized nodes that we see. 
        For each two nodes we see, we assign it as the parent's children if they are non-null.
        We then add both the child nodes into the queue, (to be later processed as parents themselves)
        """
        if not data:    return None
        res = data.split(self.DELIM)
        n, q, i = len(res), Queue(), 1
        root = TreeNode(int(res[0]))
        q.put(root)
        while i<n:
            parent = q.get()
            if res[i] != '': #res[i] will be the left child of parent.
                parent.left = TreeNode(int(res[i]))
                q.put(parent.left)
            i+=1
            if res[i] != '': #res[i] will now the right child of the parent.
                parent.right = TreeNode(int(res[i]))
                q.put(parent.right)
            i+=1
        return root


class CodecRecursive:
    DELIM = ';'
    def _serialize(self, root, result):
        if not root:
            result.append('')
            return
        result.append(str(root.val)) #Append only the current node being processed, to the list evertime.
        self._serialize(root.left, result)
        self._serialize(root.right, result)

    def serialize(self, root):
        """Encodes a tree to a single string.

        Here we perform a recursive PRE-ORDER traversal (root, traversal(root.left), traversal(root.right))
        We add each node to a list of nodeStrings (node.val if node else ''). We then attempt to serialize the children of the node recursively.
        """
        if not root:    return
        res = []
        self._serialize(root, res)
        return self.DELIM.join(res) #Join the list of strings into a single string
        
    def _deserialize(self, res, start):
        ''' This function takes in the original list of strings. And a starting integer.

        At each time, we increment the starting integer by 1 and use res[start[0]] as the value for the current node. 
        start[0]+=1 ; root = TreeNode(int(res[start[0]])) is exactly analogous to the 'next(it)' in _deserializeIter() below.
        '''
        start[0]+=1
        if not res[start[0]]:
            return None
        root = TreeNode(int(res[start[0]]))
        root.left = self._deserialize(res, start)
        root.right = self._deserialize(res, start)
        return root

    def _deserializeIter(self, it):
        ''' This function accepts an iterable. Having an iterable frees us from the effort of having to store the next element/current element index/state of the list.
        '''
        val = next(it) #val is the serialized string of the next node (will be str(node.val) or '')
        if not val: #if the val is '', return None
            return None
        root = TreeNode(int(val))
        root.left = self._deserializeIter(it) 
        root.right = self._deserializeIter(it)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        Here, we begin with the root node. We scroll through the serialized nodes that we see. 
        For each two nodes we see, we assign it as the parent's children if they are non-null.
        We then add both the child nodes into the queue, (to be later processed as parents themselves)
        """
        if not data:    return None
        res = data.split(self.DELIM) #Split the string based on the delimiter into a list of strings (1 for each node)
        return self._deserialize(res, [-1])
        # An alternate way to perform the same action is to create an iterator out of the iterable (list res). 
        it = iter(res)
        return self._deserializeIter(it)
        
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(3)
root.right.left.right = TreeNode(1)
root.right.right = TreeNode(4)

# Your Codec object will be instantiated and called as such:
codec = CodecRecursive()
print codec.serialize(root)
root = codec.deserialize(codec.serialize(root))
print codec.serialize(root)
