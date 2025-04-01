/*
 * 207. Course Schedule
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
 */

package course_schedule;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CourseSchedule {

    public boolean canFinish(int numCourses, int[][] prerequisites) {

        // Step 1: create a hashmap to track the prerequisites for each course
        Map<Integer, List<Integer>> prerequisitesMap = new HashMap<>();

        for (int i = 0; i < numCourses; i++) {
            prerequisitesMap.put(i, new ArrayList<>());
        }

        for (int[] prereq : prerequisites) {
            prerequisitesMap.get(prereq[0]).add(prereq[1]);
        }

        // Step 2: create a visited array
        int[] visited = new int[numCourses];

        // Step 3: defind DFS function for cycle detection
        for (int course = 0; course < numCourses; course++) {
            if (visited[course] == 0) { // if course has not been visited
                if (!dfs(course, prerequisitesMap, visited)) {
                    return false; // cycle detected
                }
            }
        }

        return true; // no cycle detected, can finish all courses
    }

    private boolean dfs(int course, Map<Integer, List<Integer>> prerequisitesMap, int[] visited) {
        // if the course is in the current recursion stack, a cycle is detected
        if (visited[course] == 1) {
            return false;
        }

        // if the course has already been processed, no need to process again
        if (visited[course] == 2) {
            return true;
        }

        // mark the course as visiting
        visited[course] = 1;

        // explore all prerequisites for the current course
        for (int prereq : prerequisitesMap.get(course)) {
            if (!dfs(prereq, prerequisitesMap, visited)) {
                return false;
            }
        }

        // mark the course as fully processed
        visited[course] = 2;

        return true;
    }

    public static void main(String[] args) {
        CourseSchedule cs = new CourseSchedule();

        // Test Case 1
        int numCourses1 = 2;
        int[][] prerequisites1 = { { 1, 0 } };
        System.out.println(cs.canFinish(numCourses1, prerequisites1)); // Expected: true

        // Test Case 2
        int numCourses2 = 2;
        int[][] prerequisites2 = { { 1, 0 }, { 0, 1 } };
        System.out.println(cs.canFinish(numCourses2, prerequisites2)); // Expected: false

        // Test Case 3
        int numCourses3 = 3;
        int[][] prerequisites3 = { { 1, 0 }, { 2, 1 } };
        System.out.println(cs.canFinish(numCourses3, prerequisites3)); // Expected: true
    }
}
