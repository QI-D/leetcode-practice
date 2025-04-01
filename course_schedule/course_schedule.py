'''
207. Course Schedule
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Step 1: Create a dictionary to track the prerequisites for each course
        prerequisites_dict = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prerequisites_dict[course].append(prereq)

        # Step 2: Set to track visited nodes
        # 0 -> unvisited, 1 -> visiting (part of current recursion stack), 2 -> fully processed
        visited = [0] * numCourses

        def dfs(course):
            # If the course is being visited (i.e., in the current recursion stack), we have a cycle
            if visited[course] == 1:
                return False

            # If the course has already been processed, no need to process it again
            if visited[course] == 2:
                return True

            # Mark the course as visiting
            visited[course] = 1

            # Explore all prerequisites for the current course
            for prereq in prerequisites_dict[course]:
                if not dfs(prereq):
                    return False

            # Mark the course as fully processed
            visited[course] = 2
            return True

        # Step 3: Check all courses
        for course in range(numCourses):
            if visited[course] == 0:  # If the course has not been visited yet
                if not dfs(course):
                    return False

        return True


numCourses = 2
prerequisites = [[1,0]]

result = Solution().canFinish(numCourses, prerequisites)
print(result)

numCourses = 2
prerequisites = [[1,0],[0,1]]

result = Solution().canFinish(numCourses, prerequisites)
print(result)
