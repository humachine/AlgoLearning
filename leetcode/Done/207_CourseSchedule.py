#https://leetcode.com/problems/course-schedule/
''' Given n courses (labeled 0 to n-1), some courses have prerequisites represented as (a,b): i.e to take a, you must have taken b.
Given the total number of courses and prerequisites (if any), return if it is possible to cover all courses.

    Inp: 2 [[1, 0]]
    Out: True (Can be scheduled)

    Inp: 2, [[1, 0], [0, 1]]
    Out: False (Cyclic dependency)
'''
from collections import deque
class Solution(object):
    def canFinishBFS(self, numCourses, prerequisites): # more accurately, this is a topological sort
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

        coursesCovered = len(q)
        while q:
            preReq = q.popleft()
            for course in isPreReqFor[preReq]: # If course doesn't require any more prerequisites, add it to the queue.
                preReqNeededCount[course] -= 1
                if preReqNeededCount[course] == 0:
                    q.append(course)
                    coursesCovered+=1 
        # If we have covered all courses, then we return True. Else, there was a cycle somewhere
        return coursesCovered == numCourses

    def canFinishDFS(self, numCourses, prerequisites):
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
                if not isSchedulable(neighbour):.
                    return False
            visited[course] = VISITED #Once all neighbours have been visited, current course state goes to VISITED
            return True


        for course in xrange(numCourses):
            if not isSchedulable(course):
                return False
        return True

    def canFinish(self, numCourses, prerequisites):
        # return self.canFinishBFS(numCourses, prerequisites)
        return self.canFinishDFS(numCourses, prerequisites)
s = Solution()
print s.canFinish(2, [[1, 0]])
print s.canFinish(3, [[1, 0], [0, 1]])
print s.canFinish(10, [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]])
