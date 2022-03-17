# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:11:34 2021

@author: abeln
"""

# soma Matrizes
# multiplica coluna de A pelas linhas de B


def mult_matrizes(A, B):
    num_lin_A, num_col_A  = len(A), len(A[0])
    num_lin_B, num_col_B  = len(B), len(B[0])
    assert num_col_A == num_lin_B
    C = []
    for lin in range(num_lin_A):
        # cria uma nova linha
        C.append([])
        for col in range(num_col_B):
            # cria nova coluna
            C[lin].append(0)
            for k in range(num_col_A):
                C[lin][col] += A[lin][k] * B[k][col]
    return C

if __name__ == "__main__":
    A = [1, 2, 3], [4, 5, 6], [7, 8, 9]
    B = [10, 20, 30], [40, 50, 60], [70, 80, 90]
    print(mult_matrizes(A, B))
    A = [1, 2, 3], [4, 5, 6]
    B = [1, 2], [3, 4], [5, 6]
    print(mult_matrizes(A, B))

    
    
  # C[0][0] = (a0,0 * b0,0) + (a0,1 * b1,0) + (a0,2 * b2,0)
  # C[0][1] = (a0,0 * b0,1) + (a0,1 * b1,1) + (a0,2 * b2,1)
  # C[0][2] = (a0,2 * b0,2) + (a0,2 * b1,2) + (a0,2 * b2,2)
  #
  # Ex.:
  #   A     *      B        =          C
  # 1 2 3        1 2 3        12 + 15 + 18 = 45  = C[0][0]
  # 4 5 6        4 5 6        24 + 30 + 36 = 90  = C[0][1]
  # 7 8 9        7 8 9        36 + 45 + 52 = 133 = c[0][2]
  