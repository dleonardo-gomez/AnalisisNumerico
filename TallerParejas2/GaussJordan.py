# Funcion que determina si en la matriz A y en la columna k ya existe un uno y retorna la fila 
# en la que se encuentra de lo contrario retorna -1.
#El vectorBool es para saber qué filas ya fueron pivotes
def unoExist(A,k,vectorBool):
	M = list(list(A))
	lenH = len(M)
	for i in range(0,lenH):
		if M[i][k] == 1 and vectorBool[i]==False:
			return i
	return -1
#Funcion que resuelve una ecuacion basado en el metodo de GaussJordan
def gaussJordan(A):
    vectorBool = []
    M = list(list(A))
    lenV = len(M)
    lenH = len(M[0])
    for i in range(0,lenV):
    	vectorBool.append(False)
    if lenH - lenV < 0:
        return M
    #recorremos todas las filas para crear los pivotes
    for i in range(0,lenH-1):
    	#buscamos si hay un pivote 1 en la columna i
    	uno=unoExist(A,i,vectorBool)
    	#si no lo encontramos, entonces creamos el pivote dividiendo la fila por el valor del primer 
    	#numero de la primera fila que no haya sido pivote
    	if uno==-1:
    		val=False
    		for y in range(0,lenV):
    			if(vectorBool[y]==False and val==False):
    				aux=M[y][i]
    				uno=y
    				val=True
    				for x in range(0,lenH):
    					M[y][x]=M[y][x]/aux
    	#marcamos la fila para recordar que ya es pivote
    	vectorBool[uno]=True
    	#Hacemos el metodo de GaussJordan
    	for y in range(0,lenV):
    		pri=M[y][i]*(-1)
    		for x in range(0,lenH):
    			if y!=uno:
    				M[y][x]=(M[uno][x]*pri)+M[y][x]

    	
    		
    #imprimimos la solucion
    print(M)

a=[[1,2,3,5],[2,1,8,7],[4,6,8,9]]
gaussJordan(a)
