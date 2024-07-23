# -*- coding: utf-8 -*-
"""

Problem of the day - Skyline Problem

"""

def get_skyline(buildings):

    points = []
    for x1, x2, h in buildings:
        points.append((x1, -h))  
        points.append((x2, h))

    points.sort(key=lambda x: (x[0], x[1]))
    
    import heapq
    heap = [0] 
    prev_height = 0
    skyline = []

    for x, h in points:
        if h < 0: 
            heapq.heappush(heap, h)
        else: 
            heap.remove(-h)
            heapq.heapify(heap)  
            
        current_height = -heap[0]
        if current_height != prev_height:
            skyline.append([x, current_height])
            prev_height = current_height

    return skyline


buildings = [[0, 2, 3], [2, 5, 3]]
output = get_skyline(buildings)
print(output) 
