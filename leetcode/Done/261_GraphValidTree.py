#https://leetcode.com/problems/graph-valid-tree/
'''
Given a set of nodes labeled 0 to n-1, check if the nodes make up a valid tree.

    Inp: edges = [[0, 1], [0, 2], [0, 3], [1, 4]], n=5
    Return: True

    Inp: edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], n=5
    Return: False (1,2,3 form a cycle and hence this cannot be a tree
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = set()
        self.visited = False

class Solution(object):
    def buildGraph(self, nodes, edges):
        for edge in edges:
            nodes[edge[0]].neighbours.add(edge[1])
            nodes[edge[1]].neighbours.add(edge[0])

    def validTreeBFS(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1: # numEdges = n-1 for a tree
            return False
        # We build the graph of nodes initially
        nodes = [Node(x) for x in xrange(n)]
        self.buildGraph(nodes, edges)

        visitedCount = 0
        q = [nodes[0]]
        # We start at a single node and run BFS from that node. If it reaches all the nodes AND there's no cycle, then this is a graph valid tree
        for node in q:
            if node.visited:    # If the node has already been visited, then there has been a cycle somewhere
                return False
            node.visited = True
            visitedCount += 1
            # For each of this node's neighbours, we add them to the queue. We also remove the backlink from the set of edges for the neighbours
            for neighbour in node.neighbours:
                nodes[neighbour].neighbours.remove(node.val)
                q.append(nodes[neighbour])
        return visitedCount == n


    def validTreeDFS(self, n, edges):
        if len(edges) != n-1: # numEdges = n-1 for a tree
            return False
        # Similar to the BFS solution, we build the graph of nodes
        nodes = [Node(x) for x in xrange(n)]
        self.buildGraph(nodes, edges)

        def hasCycle(parent, curr, nodes, visitedCount):
            '''Returns True if there's a cycle that's been discovered while exploring this node'''
            if curr.visited:
                return True
            curr.visited = True
            visitedCount[0] += 1
            for neighbour in curr.neighbours:
                # If your neighbour is your parent, then ignore it
                if neighbour == parent.val:
                    continue
                # Check if your neighbour leads you to a cycle
                if hasCycle(curr, nodes[neighbour], nodes, visitedCount):
                    return True
            return False

        visitedCount = [0]
        # We try to check if the component containing the first node has a cycle. If it does, we return False
        if hasCycle(nodes[0], nodes[0], nodes, visitedCount):
            return False
        # If there's no cycle in the first component, we return if the 1st component covered all nodes (to check for connectivity to all n nodes)
        return visitedCount[0] == n


    def validTreeUnionFind(self, n, edges):
        '''
        We use Union Find to find if there's a cycle in the graph. First, we begin with a separate island/component for each node. 
        Every time we process an edge, we perform 2 find operations (to find the islands they belong to). If they both belong to the same island already, then there's a cycle.
        If not, we then perform the union operation, where we join the 2 components into 1 single component.
        '''
        if len(edges) != n-1: # numEdges = n-1 for a tree
            return False

        components = [-1]*n # Each element represents a number that denotes its parent. If it is -1, then it has no parent
        # We attempt to form trees of nodes. Each time an edge is visited, we unionize the 2 components that they belong to. If they already belong to the same component, then we have a cycle.
        def find(x):
            '''Returns the index of the highest parent of x's component'''
            if components[x] == -1:
                return x
            return find(components[x])
        for edge in edges:
            compX, compY = find(edge[0]), find(edge[1])
            if compX == compY:
                return False
            components[compX] = compY  #Equating both components
            components[edge[0]] = compY #Optional: This line performs path compression, compressing the node edge[0] to compY which is the parent of compX
        return True

edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
s = Solution()
print s.validTreeUnionFind(5, edges)
print s.validTreeUnionFind(4, edges)
