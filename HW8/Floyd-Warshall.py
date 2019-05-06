#### FLOYD'S ALGORITHM ####

## All pairs shortest path problem
## Find shortest distance between every pair of vertices

import numpy as np

### Infinity is huge number
INFINITY = 999999999999



## 5 vertices
vertices = 5


## Function to print D()
def FloydsAlgo(diagram):
    # 2D distance array is return value
    ## Initial min distance for each vertice
    ## Finds distance between i and j
    pi = np.zeros((vertices, vertices))
    for i in range(vertices):
        for j in range(vertices):
            if((i == j) or (diagram[i][j] == INFINITY)):
                pi[i][j] = None
            else:
                pi[i][j] = i
                                                                            ## vertice in distance array
    ## Loop through entirity of the diagram with 5 vertices
    for k in range(vertices):
        # iterate through and allow each vertice to be the source of the distance calculation
        for i in range(vertices):
            # iterate through and allow each vertice to be the destination of the i source vertices
            for j in range(vertices):
                # check for min distance, update if lower than min
                if((diagram[i][k] + diagram[k][j]) < diagram[i][j]):
                    diagram[i][j] = (diagram[i][k] + diagram[k][j])
                    pi[i][j] = pi[k][j]

        print("D(%d)" % k)
        printDiagram(diagram)
        print("Pi(%d)" % k)
        printDiagram(pi)
    # When exited final iteration, print the distance
    #printDiagram(distance)



## Helper function to print the solution distance
def printDiagram(distance):
    # create nested foor loops for 2D array
    for i in range(vertices):
        print("[", end = "")
        for j in range(vertices):
            # Check for infinite values
            if (distance[i][j] == INFINITY):
                print("%7s" % ("INF"), end = "")
            # If value is not infinite
            else:
                print("%7s" % ( distance[i][j]), end = "")
            if (j == vertices - 1):
                print("]")

def main():

    ##### INPUT #####
    D = [ [0, 2, INFINITY, 1, 8],
            [6, 0, 3, 2, INFINITY],
            [INFINITY, INFINITY, 0, 4, INFINITY],
            [INFINITY, INFINITY, 2, 0, 3],
            [3, INFINITY, INFINITY, INFINITY, 0]]

    TextBookTest = [
            [0, 3, 8, INFINITY, -4],
            [INFINITY, 0, INFINITY, 1, 7],
            [INFINITY, 4, 0, INFINITY, INFINITY],
            [2, INFINITY, -5, 0, INFINITY],
            [INFINITY, INFINITY, INFINITY, 6, 0]
    ]
##FloydsDAlgo(TextBookTest)
## D algo confirmed working

    #floydSCIPYAlgo(TextBookTest)

    FloydsDAlgo(TextBookTest)
    #FloydsPiAlgo(TextBookTest)
##Flo

if __name__ == "__main__":
    main()
