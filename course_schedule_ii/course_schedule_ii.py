'''
210. Course Schedule II
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # step 1: build course dependency graph and prerequisite count
        course_dependencies = {i: [] for i in range(numCourses)}
        prerequisite_count = {i: 0 for i in range (numCourses)}

        for course, prerequisite in prerequisites:
            course_dependencies[prerequisite].append(course) # prerequisite: [course]
            prerequisite_count[course] += 1 # track how many dependencies each course has

        # step 2: find courses with no prerequisites
        available_courses = [course for course in prerequisite_count if prerequisite_count[course] == 0]
        course_order = []

        # step 3: process courses using a list as a queue
        while available_courses:
            current_course = available_courses.pop(0)
            course_order.append(current_course)

            for dependent_course in course_dependencies[current_course]:
                prerequisite_count[dependent_course] -= 1 # reduce prerequisite count for dependent courses
                if prerequisite_count[dependent_course] == 0:
                    available_courses.append(dependent_course) # add to queue when no prerequisites left

        if len(course_order) == numCourses:
            return course_order

        return []


# Example test cases
solution = Solution()
print(solution.findOrder(2, [[1, 0]]))  # Expected: [0, 1]
print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Expected: [0, 1, 2, 3] or [0, 2, 1, 3]
print(solution.findOrder(2, [[1, 0], [0, 1]]))  # Expected: [] (cycle detected)
