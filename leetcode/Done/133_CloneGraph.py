#https://leetcode.com/problems/clone-graph/
''' Given an undirected graph, clone it.'''
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
from Queue import Queue
class Solution:
    def cloneGraphBFS(self, node):
    # @param node, a undirected graph node
    # @return a undirected graph node
        if not node:    return node
        nodes, q = {}, Queue()
        q.put(node)
        # We begin with a queue containing just the seed node
        while not q.empty():
            # As long as we have nodes, we keep polling the queue and cloning them
            n = q.get()
            if n.label not in nodes: #If no clone already exists, then create a copy and add it to the dictionary too
                nodes[n.label] = UndirectedGraphNode(n.label)
            # For each of the original node's neighbors, if there aren't clones for the neighbors, create them. Append a reference to the cloned neighbors in the cloned copy's neighbors attribute.
            # Finally put each of the neighbors in the queue for them to cloned themselves (which leads to the cloning of their neighbors and so on...)
            for neighbor in n.neighbors:
                if neighbor.label not in nodes: #If neighbor's clone does not already exist, create one and register it with the dictionary of clones
                    nodes[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    q.put(neighbor)
                nodes[n.label].neighbors.append(nodes[neighbor.label])
        return nodes[node.label] #Return the clone corresponding to the seed node.

    def __init__(self):
        self.nodes = {}

    def cloneGraph(self, node):
        if not node:    return None

        #If node has already been cloned, just return the cloned copy of the node
        if node.label in self.nodes: 
            return self.nodes[node.label]
        # Since the node has not yet been cloned, let's clone it now.
        clone = UndirectedGraphNode(node.label)
        self.nodes[node.label] = clone #Adding clone to the dictionary of cloned copies

        for neighbor in node.neighbors:
            # For each of the neighbors of the node to be cloned, we recurse and find the cloned copy of the neighbor and then add the cloned neighbor to current node's neighbors
            clone.neighbors.append(self.cloneGraph(neighbor))
        return clone
