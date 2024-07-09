# -*- coding: utf-8 -*-
"""
Challange of The Day 
---------------------
Week :2
Day  :2

----------------------
By Abdulrahim Alhadidi
"""

def is_path_crossing(distances):

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  
    visited = set()

    x, y = 0, 0

    visited.add((x, y))

    for i in range(len(distances)):
        current_distance = distances[i]
        current_direction = directions[i % 4]
        
        for step in range(current_distance):
            x += current_direction[0]
            y += current_direction[1]
        
            if (x, y) in visited:
                return True  
            
            visited.add((x, y))

    return False

distances = [1,1,1,2,1]
print(is_path_crossing(distances))