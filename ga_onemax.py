import random
import copy

class respuesta:
    def __init__(self, s):
        self.s = s
        self.eval = self.evaluacion(s)
        self.normalizacion = 0
    
    def evaluacion(self,s):
        evaluacion = 0
        for i in range(len(s)):
            evaluacion = evaluacion + s[i]
        return evaluacion

    def get_evaluacion(self):
        return self.eval
    
    def setNormalizacion(self, valor):
        self.normalizacion = valor

    def evaluar(self):
        self.eval = evaluacion(self.s)
    
    def __str__(self) -> str:
        print(self.s)
    

def GA(max_iteraciones, poblacion, dimension):
    
    poblaciones = []
    t = 0
    soluciones = []

    for i in range(poblacion):
        s = []
        for j in range(dimension):
            aux = random.random()
            if aux < 0.5:
                s.append(1)
            else:
                s.append(0)
        soluciones.append(respuesta(s))
    
    #print("padres: ")
    #for i in range(len(soluciones)):
    #    print(soluciones[i].s)
    
    while(t < max_iteraciones):
        t = t+1
        #print("el valor de T es: ", t)
        parejas = seleccion_de_padres(soluciones)
        hijos = cruza(parejas, soluciones)
        hijosMutados = mutacion(hijos)
        evaluacion(hijosMutados)
        soluciones = mejoresGeneraciones(soluciones, hijosMutados)

    #print("padres e hijos mejorados:")
    #for i in range(len(soluciones)):
    #    print(soluciones[i].s)    

                
def seleccion_de_padres(soluciones):
    sum = 0

    for i in range(len(soluciones)):
        sum = sum + soluciones[i].get_evaluacion()

    aux = 0
    for i in range(len(soluciones)):
        normalizacion = soluciones[i].get_evaluacion() / sum
        aux = aux + normalizacion
        soluciones[i].setNormalizacion(aux)

    parejas = []
    for i in range(int (len(soluciones)/2)):
        sumNormTotal = 0
        indices = []
        ruleta = random.random()
        for j in range(len(soluciones)):
            sumNormTotal = sumNormTotal + soluciones[j].normalizacion
            if(sumNormTotal > ruleta):
                indices.append(j)
                break
        sumNormTotal = 0
        ruleta = random.random()
        for j in range(len(soluciones)):
            sumNormTotal = sumNormTotal + soluciones[j].normalizacion
            if(sumNormTotal > ruleta):
                indices.append(j)
                break
        parejas.append(indices)
    return parejas

def cruza(indices_padres, soluciones):
    hijos = []
    for i in range(len(soluciones)):
        hijos.append(respuesta(copy.copy(soluciones[i].s)))

    corte = int (random.uniform(1, len(soluciones[0].s)))
    #print("este es el corte: ", corte)
    for i in range(len(indices_padres)):
        for j in range(corte, len(hijos[0].s)):
            aux = hijos[indices_padres[i][0]].s[j]
            hijos[indices_padres[i][0]].s[j] = hijos[indices_padres[i][1]].s[j]
            hijos[indices_padres[i][1]].s[j] = aux        

    return hijos

def mutacion(hijos):
    hijosMutados = []
    for i in range(len(hijos)):
        hijosMutados.append(respuesta(copy.copy(hijos[i].s)))

    for i in range(len(hijosMutados)):
        mutacion = int(random.uniform(0, len(hijosMutados[0].s)))
        if(hijosMutados[i].s[mutacion] == 0):
            hijosMutados[i].s[mutacion] = 1
        else:
            hijosMutados[i].s[mutacion] = 0
    #print("tamaño de hijos mutados: ", len(hijosMutados))
    return hijosMutados

def evaluacion(soluciones):
    for i in range(len(soluciones)):
        soluciones[i].evaluar

def mejoresGeneraciones(soluciones, hijos):
    topPadreseHijos = []
    padres = []
    hijos1 = []

    for i in range(len(soluciones)):
        padres.append(respuesta(copy.copy(soluciones[i].s)))
    for i in range(len(hijos)):
        hijos1.append(respuesta(copy.copy(hijos[i].s)))

    padres.sort(key=lambda x:x.eval, reverse=True)
    hijos1.sort(key=lambda x:x.eval, reverse=True)
    print("el mejor padre: ", padres[0].s)
    print("el mejor hijo: ", hijos1[0].s)
    #sorted(padres, key = lambda x:x.eval, reverse=True)
    #sorted(hijos1, key= lambda x:x.eval, reverse= True)
    #print("tamaño de listas:", len(padres), "tamaño de lista hijos: ", len(hijos1))
    for i in range(int (len(padres)/2)):
        topPadreseHijos.append(padres[i])
    for i in range(int (len(hijos1)/2)):
        topPadreseHijos.append(hijos1[i])

    #print("resultado mejores generaciones: ")
    #for i in range(len(topPadreseHijos)):
    #    print(topPadreseHijos[i].s)
    return topPadreseHijos


GA(1000, 50, 100)
