#### FLOYD'S ALGORITHM ####

## All pairs shortest path problem
## Find shortest distance between every pair of vertices

### Infinity is huge number
INFINITY = 999999999999



## 5 vertices
vertices = 5

## Function to print D()
def FloydsDAlgo(diagram):
    # 2D distance array is return value
    ## Initial min distance for each vertice
    ## Finds distance between i and j

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
        print("D(%d)" % k)
        printDiagram(diagram)
    # When exited final iteration, print the distance
    #printDiagram(distance)
## Function to print pi()
def FloydsPiAlgo(diagram):
    ## Initialize Pi matrix
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if(k == 0):
                    if((i == j) or (diagram[i][j] == INFINITY)):
                        diagram[i][j] = None
                    else:
                        diagram[i][j] = i
                else:
                    if(diagram[i][k-1] != None and
                        diagram[k-1][j] != None and
                        diagram[i][j] != None and
                        diagram[i][k-1] + diagram[k-1][j] < diagram[i][j]):
                        diagram[i][j] = diagram[k-1][j]
        print("Pi(%d)" % k)
        printDiagram(diagram)




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
    FloydsDAlgo(D)
    FloydsPiAlgo(TextBookTest)
##Flo

if __name__ == "__main__":
    main()
