import heapq


def Klargest(array, k):
    # heapq.heapify(array)

    # k_largest = heapq.nlargest(k, array)
    # k_largest.sort()

    heap = []
    heapq.heapify(heap)
    # (heap, item)
    for item in array:
        heapq.heappush(heap, item)

        if len(heap) > k:
            heapq.heappop(heap)

    heap.sort()
    return heap
