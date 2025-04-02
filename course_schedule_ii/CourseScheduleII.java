/*
 * 210. Course Schedule II
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
 */

package course_schedule_ii;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CourseScheduleII {

    public int[] findOrder(int numCourses, int[][] prerequisites) {

        // step 1: build course dependency graph and prerequisite count
        Map<Integer, List<Integer>> courseDependencies = new HashMap<>();
        Map<Integer, Integer> prerequisiteCount = new HashMap<>();

        for (int i = 0; i < numCourses; i++) {
            courseDependencies.put(i, new ArrayList<>());
            prerequisiteCount.put(i, 0);
        }

        // step 2: build course dependencies and prerequisite count
        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int prereq = prerequisite[1];
            courseDependencies.get(prereq).add(course); // prereq: [course]
            prerequisiteCount.put(course, prerequisiteCount.get(course) + 1);
        }

        // step 3: find courses with no prerequisites
        List<Integer> availableCourses = new ArrayList<>();
        for (int course : prerequisiteCount.keySet()) {
            if (prerequisiteCount.get(course) == 0) {
                availableCourses.add(course);
            }
        }

        // step 4: process courses using a list as a queue
        List<Integer> courseOrder = new ArrayList<>();
        while (!availableCourses.isEmpty()) {
            int currentCourse = availableCourses.remove(0);
            courseOrder.add(currentCourse);

            for (int dependentCourse : courseDependencies.get(currentCourse)) {
                prerequisiteCount.put(dependentCourse, prerequisiteCount.get(dependentCourse) - 1);
                if (prerequisiteCount.get(dependentCourse) == 0) {
                    availableCourses.add(dependentCourse);
                }
            }
        }

        // step 5: check if all courses were processed
        if (courseOrder.size() != numCourses) {
            return new int[0];
        }

        // convert list to array
        int[] result = new int[courseOrder.size()];
        for (int i = 0; i < courseOrder.size(); i++) {
            result[i] = courseOrder.get(i);
        }

        return result;
    }

    public static void main(String[] args) {
        CourseScheduleII cs = new CourseScheduleII();

        // Expected: [0, 1]
        System.out.println(Arrays.toString(cs.findOrder(2, new int[][] { { 1, 0 } })));

        // Expected: [0, 1, 2, 3] or [0, 2, 1, 3]
        System.out.println(Arrays.toString(cs.findOrder(4, new int[][] { { 1, 0 }, { 2, 0 }, { 3, 1 }, { 3, 2 } })));

        // Expected: [0, 1, 2, 3] or [0, 2, 1, 3]
        System.out.println(Arrays.toString(cs.findOrder(2, new int[][] { { 1, 0 }, { 0, 1 } })));
    }
}
