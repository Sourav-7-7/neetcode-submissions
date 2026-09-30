class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        visiting=set()
        visited=set()
        graph=[[] for _ in range(numCourses)]
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True