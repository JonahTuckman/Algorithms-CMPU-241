### Matrix-Chain-Order
import numpy as np
from numpy import array

INFINITY = 999999999999


def MatrixChainOrder(p):
    n = len(p) - 1

    # m is minimum number of multiplications needed
    m = [[0 for x in range(0,n)] for y in range(0,n)]
    # matrix after minimum multiplication split
    s = [[0 for x in range(0,n)] for y in range(0,n)]


    for i in range(1,n):
        m[i][i] = 0

    # Find the shortest matrix cost
    for l in range(2, n+1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            m[i][j] = INFINITY
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def Print_Optimal_Parens(s, i, j):
    if i == j:
        print("A_%d" % i)
    else:
        print("(")
        Print_Optimal_Parens(s, i, s[i][j])
        Print_Optimal_Parens(s, s[i][j] + 1, j)
        print(")")


def main():

    ## Input:
    p = [40, 20, 30, 10, 30]

    m, s =  MatrixChainOrder(p)

    print(m)
    print(s)
    Print_Optimal_Parens(s,1,4)


if __name__ == "__main__":
    main()
