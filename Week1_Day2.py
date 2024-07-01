# -*- coding: utf-8 -*-
"""

Challange of The Day - Triangle Height
---------------------
Week :1
Day  :2

----------------------
By Abdulrahim Alhadidi

"""

def triangle_height(white_balls, black_balls):
    height = 0
    while True:
        #how much balls needed to cover the row
        needed_balls = height + 1
        
        #white balls row(odd rows: 1, 3, 5, ...)
        if height % 2 == 0:
            if white_balls >= needed_balls:
                white_balls -= needed_balls
                height += 1
            else:
                #if not enough balls stop
                break
            
        #black balls row
        else:  
            if black_balls >= needed_balls:
                black_balls -= needed_balls
                height += 1
            else:
                break
    return height


white_balls = int(input("White balls: "))
black_balls = int(input("Black balls: "))

height = triangle_height(white_balls, black_balls)

print(f"The maximum height of the triangle is: {height}")
