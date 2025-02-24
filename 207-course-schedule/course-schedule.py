class Solution:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_egde(self,course,prerequisite):
        self.graph[course].append(prerequisite)

    def cyclehelper(self,node,visited,recStack):
        visited.add(node)
        recStack.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.cyclehelper(neighbor,visited,recStack):
                    return True
            elif neighbor in recStack:
                return True
        recStack.remove(node)
        return False

    def hascycle(self,numCourses):
        visited=set()
        recStack=set()
        for node in range(numCourses):
            if node not in visited:
                if self.cyclehelper(node,visited,recStack):
                    return True
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        for crs,pre in prerequisites:
            self.add_egde(crs,pre)
    
        return not self.hascycle(numCourses)
                



        