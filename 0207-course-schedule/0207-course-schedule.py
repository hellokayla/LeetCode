# Approach: Use Kahn's algorithm, iterative approach
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True
        
        # store incoming degrees
        # forces every course to exist
        in_degree = [0] * numCourses

        # build out the adjacency list
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            # map of adjacency list
            # outgoing arrows
            graph[prereq].append(course)

            # populate the in-degrees
            # 0 points to 1
            # in-degree: how many arrows pointing to the node
            # everything else gets 0
            in_degree[course] +=1


        q = []

        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)

        count = 0

        while q:
            curr_node = q.pop(0)
            count += 1

            for neighbor in graph[curr_node]:

                # minus 1 
                in_degree[neighbor] -= 1

                # if their value becomes 0, add to queue
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        # check the cycle
        return count == numCourses

        




