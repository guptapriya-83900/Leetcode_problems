import heapq
class Solution:
    def nlargest(self, k, stones):
        min_heap = []  # Min Heap to keep k largest elements
        for stone in stones:
            heapq.heappush(min_heap, stone)
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove the smallest
        
        return min_heap  # Return sorted in descending order

    def lastStoneWeight(self, stones: List[int]) -> int:
        # max_heap = [-stone for stone in stones]
        # heapq.heapify(max_heap)

        # while len(max_heap)>1:
        #     first = -heapq.heappop(max_heap)  
        #     second = -heapq.heappop(max_heap)

        #     if first != second:
        #         heapq.heappush(max_heap, -(first - second))

        stones = stones[:]  
        heapq.heapify(stones)  

        while len(stones) > 1:
            two_largest = self.nlargest(2, stones)  
            first, second = two_largest[1], two_largest[0]

            
            stones.remove(first)
            stones.remove(second)

            # Step 3: Compute the difference and insert back if nonzero
            if first != second:
                heapq.heappush(stones, first - second)

        # Step 4: Return the last remaining stone or 0 if none remain
        return stones[0] if stones else 0

            

            