#https://leetcode.com/problems/course-schedule-ii/
''' Given n courses (labeled 0 to n-1), some courses have prerequisites represented as (a,b): i.e to take a, you must have taken b.
Given the total number of courses and prerequisites (if any), return a valid ordering of courses so as to fulfil all dependencies.

    Inp: 2 [[1, 0]]
    Out: [0, 1]

    Inp: 4, [[1,0],[2,0],[3,1],[3,2]]
    Out: [0, 1, 2, 3] is one possible ordering
'''
from collections import deque
class Solution(object):
    def findOrderTopoSort(self, numCourses, prerequisites): # more accurately, this is a topological sort
        isPreReqFor = [set() for i in xrange(numCourses)] #isPreReqFor[x] is a set of courses for which x is the prerequisite for
        preReqNeededCount = [0]*numCourses # preReqNeededCount[x] = number of prerequisites course x has
        for course, reqd in prerequisites:
            # (course, reqd) means that to take the 'course' you have to have completed 'reqd'
            if course not in isPreReqFor[reqd]: # To avoid counting the same prerequisite more than once
                preReqNeededCount[course] += 1
            isPreReqFor[reqd].add(course)

        q = deque() #We add all courses that DON'T require any prerequisites into the queue
        for course in xrange(numCourses):
            if preReqNeededCount[course] == 0: #If no prerequisites needed for this course, then add it to the queue
                q.append(course)

        courseOrdering = []
        while q:
            preReq = q.popleft()
            courseOrdering.append(preReq)
            for course in isPreReqFor[preReq]: # If course doesn't require any more prerequisites, add it to the queue.
                preReqNeededCount[course] -= 1
                if preReqNeededCount[course] == 0:
                    q.append(course)
        # If we have covered all courses, then we return the ordereing. Else, there was a cycle somewhere
        if len(courseOrdering) == numCourses:
            return courseOrdering
        return []

    def findOrderDFS(self, numCourses, prerequisites):
        ''' We run a DFS starting at all nodes and exploring all nodes connected to them. 
        Each node has 3 states: UNVISITED, CURRENTLY_VISITING, VISITED


        If a node is in CURRENTLY_VISITING and we reach it again, then there's a backlink. Which means there's a cycle. We return False for the scheduability of that series of connected courses.
        If you reach a node that has already been VISITED, then you're only bridging 2 components together. Hence you return True.
        In all other cases you set the state to CURRENTLY_VISITING and proceed to go and visit all later neighbours of that node.

        It can be observed that all nodes of a component will be at the CURRENTLY_VISITING state before the recursion unrolls and they all get their state changed to VISITED.
        '''
        visited = [0]*numCourses
        CURRENTLY_VISITING, UNVISITED, VISITED = -1, 0, 1
        isPreReqFor = [set() for _ in xrange(numCourses)]
        for course, preReq in prerequisites:
            isPreReqFor[preReq].add(course) # Forming the graph as an adjacency list.

        def isSchedulable(course):
            if visited[course] == VISITED: # If the course has already been visited, return True (we are just bridging together 2 components with this edge.
                return True
            if visited[course] == CURRENTLY_VISITING: #If the course is currently being visited, then we have a backlink which means there's a cycle. We return False, since it can't be scheduled.
                return False

            visited[course] = CURRENTLY_VISITING
            for neighbour in isPreReqFor[course]: #For each neighbour of current course, explore DFS and check if the neighbour is schedulable. Even if one of the neighbours can't be scheduled, return False
                if not isSchedulable(neighbour):
                    return False
            visited[course] = VISITED #Once all neighbours have been visited, current course state goes to VISITED
            courseOrdering.append(course)
            ''' Once we are done visiting a node, we add it to courseOrdering. If 2 depends on 1 which depends on 0 and we start DFS at 1.
            1 leads to 2. We then append 2 to the list.
            When the recursion unrolls, we then append 1 to the list.

            Finally when we process 0 and append 0 to the list. The early elements of the list are the elements which have the most dependencies. The later elements of the list are the courses that have the least dependencies. 
            Hence we finally reverse the courseOrdering list to get the ordering of courses that we desire.
            '''
            return True


        courseOrdering = []
        for course in xrange(numCourses):
            if not isSchedulable(course):
                return []
        return courseOrdering[::-1]

    def findOrder(self, numCourses, prerequisites):
        ''' The TopoSort lists all the courses with no dependencies at the front and progressively courses with more and more dependencies.
        The DFS on the other hand lists courses in an order that's valid, but does not necessarily begin with the courses with no dependcies.

        Suppose courses were as below (4 depends on 3, 6 depends on 4 etc)
        3 - 4 - 6
         \
          5- 7 - 8 - 9 - 11
        Topo sort returns 3 first, then 4, 5 then 6, 7 and so on. (It returns level by level since it's a BFS)
        DFS may return any list, like say, [3, 5, 4, 6, 7, 8, 9, 11]
        '''
        # return self.findOrderTopoSort(numCourses, prerequisites)
        return self.findOrderDFS(numCourses, prerequisites)

s = Solution()
print s.findOrder(2, [[1, 0]])
print s.findOrder(3, [[1, 0], [2, 1]])
print s.findOrder(3, [[1, 0], [0, 1]])
print s.findOrder(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]])
