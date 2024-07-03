# -*- coding: utf-8 -*-
"""
Challange of The Day - Rotate Matrix
---------------------
Week :1
Day  :3

----------------------
By Abdulrahim Alhadidi
"""

def rotate(matrix):
    n = len(matrix)
    
    #create new matrix for output
    new_matrix = []
    for i in range(n):
        row = [0] * n  
        new_matrix.append(row)
    
    #rotate 
    for i in range(n):
        for j in range(n):
            new_matrix[j][n - i - 1] = matrix[i][j]
            
            #display itrations
            print(f"\n {new_matrix} \n")
    
    return new_matrix



input_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print("Input:", input_matrix)

rotated = rotate(input_matrix)
print("Output:", rotated)





