# Approach: Use Kahn's algorithm, iterative approach
# 
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True
        
        # key-value store of in-degrees
        # key: node value: 0
        prereqs = defaultdict(int)

        # build out the adjacency list
        graph = defaultdict(list)

        for course, req_course in prerequisites:
            # map of adjacency list
            # outgoing arrows
            graph[req_course].append(course)

            # populate the in-degrees
            # 0 points to 1
            # in-degree: how many arrows pointing to the node
            prereqs[course] +=1

            # make sure 0 gets initialized
            if req_course not in prereqs:
                prereqs[req_course] = 0

        q = []


        # khan's algorithm (DFS)
        # find starting nodes
        for node, degree in prereqs.items():
            if degree == 0:
                q.append(node)
        count = 0

        while q:
            curr_node = q.pop(0)
            count += 1

            for neighbor in graph[curr_node]:

                # minus 1 
                prereqs[neighbor] -= 1

                # if their value becomes 0, add to queue
                if prereqs[neighbor] == 0:
                    q.append(neighbor)
        
        # check the cycle
        return count == len(graph.keys())

        




