import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minheap=[1]
        seen=set([1])
        primes=[2,3,5]

        for _ in range(n - 1):  
            smallest = heapq.heappop(minheap) 
        
            for prime in primes:
                new_ugly = smallest * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(minheap, new_ugly)

        return heapq.heappop(minheap)
