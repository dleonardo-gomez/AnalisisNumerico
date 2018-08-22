def sumaTriangular(A):
    matrix = list(list(A))
    n = len(matrix)
    suma = 0
    nOperaciones = 0
    for x in range(0,n):
        for y in range(x,n):
            suma+=matrix[x][y]
            nOperaciones += 1
            
    print("la suma de la matriz superior triangular es:"+str(suma))
    print("la cantidad de operaciones es: "+str(nOperaciones)+"\n")
    return suma
    
def main():
    
    matrizA = [[1,2,3,5],[0,1,8,7],[0,0,8,5],[0,1,7,3]]
    matrizB = [[18,68,8,88],[0,90,23,49],[0,0,29,10],[0,0,0,85]]
    matrizC = [[16,12,13],[17,16,18],[5,14,18]]
    matrizD = [[16,12,13],[0,16,18],[0,0,18]]
    matrizE = [[1,16,3,16,15],[17,1,6,6,15],[14,10,1,15,8],[11,6,10,14,12],[11,6,10,14,12]]
    
    print("Prueba 1: 4x4")
    sumaTriangular(matrizA)
    print("Prueba 2: 4x4")
    sumaTriangular(matrizB)
    print("Prueba 3: 3x3")
    sumaTriangular(matrizC)
    print("Prueba 4: 3x3")
    sumaTriangular(matrizD)
    print("Prueba 5: 5x5")
    sumaTriangular(matrizE)
        
if __name__ == "__main__":
    main()
