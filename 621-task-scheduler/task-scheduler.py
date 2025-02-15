import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap=[-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        time=0
        cooldown = deque()


        while maxHeap or cooldown:
            time+=1

            if maxHeap:
                count=heapq.heappop(maxHeap) + 1
                if count<0:
                    cooldown.append((time+n,count))

            if cooldown and cooldown[0][0]==time:
                heapq.heappush(maxHeap, cooldown.popleft()[1]) 
            
        return time



       