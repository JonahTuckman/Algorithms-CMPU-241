### Matrix-Chain-Order
#import numpy as np
#from numpy import array

INFINITY = 999999999999


def MatrixChainOrder(p):
    n = len(p) - 1

    # m is minimum number of multiplications needed
    m = [[0 for x in range(0,n)] for y in range(0,n)]
    # matrix after minimum multiplication split
    s = [[0 for x in range(0,n)] for y in range(0,n)]


    ## Make the diagonal 0
    for i in range(1,n):
        m[i][i] = 0

    # Find the shortest matrix cost
    for l in range(1, n):
        for i in range(0, n - l):
            j = i + l
            # Set value to large infinity value set above
            m[i][j] = INFINITY
            for k in range(i, j):
                # Calculate the cost of each iteration
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                # find min cost
                if (q < m[i][j]):
                    # if min cost:
                    # set m value to the cost
                    m[i][j] = q
                    # set s value to the iteration number
                    s[i][j] = k

    return m, s

def Print_Optimal_Parens(s, i, j):
    if i == j:
        # Print the A value
        print("A_%d" % i, end = "")
    else:
        # print parenthasis and recursively call
        print("(", end = "")
        Print_Optimal_Parens(s, i, s[i][j])
        Print_Optimal_Parens(s, s[i][j] + 1, j)
        # once call has concluded and returned we add closing parenthasis
        print(")", end = "")


def main():

    ## Input:
    p = [40, 20, 30, 10, 30]

    # create m and s matrix with input
    m, s =  MatrixChainOrder(p)

    # Printing M and S matrix
    print("M Matrix")
    for i in m:
        print(i)
    print("")
    print("S Matrix")
    for i in s:
        print(i)
    print("")
    # Parenthasis using m and s
    Print_Optimal_Parens(s,0,3)
    print("")



if __name__ == "__main__":
    main()
