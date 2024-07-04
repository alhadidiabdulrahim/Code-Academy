# -*- coding: utf-8 -*-
"""
Challange of The Day - Max Area In Bar Chart
---------------------
Week :1
Day  :4

----------------------
By Abdulrahim Alhadidi
"""

heights = [2, 1, 5, 6, 2, 3]
max_area = 0  
n = len(heights)


for i in range(n):
    min_height = heights[i]
    for j in range(i, n):
        min_height = min(min_height, heights[j])
        current_area = min_height * (j - i + 1)
        max_area = max(max_area, current_area)

print(max_area)
