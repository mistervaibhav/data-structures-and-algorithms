import heapq


def nearlySorted(array, k):
    heap = []
    heapq.heapify(heap)

    sorted_array = []

    for item in array:
        heapq.heappush(heap, item)

        if len(heap) > k:
            sorted_array.append(heapq.heappop(heap))

    while len(heap) > 0:
        sorted_array.append(heapq.heappop(heap))

    return sorted_array
