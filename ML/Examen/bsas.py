import math

def distanciaCluster(data,cluster):
    """
    data -> puntos (x,y) a los que se les requiere calcular la distancia a los cluster
    cluster -> recibe la lista de los puntos que pertenecen a un cluster especifico

    """
    xsum, ysum =0 , 0

    for x,y in cluster:
        xsum += x
        ysum += y
    
    xsum/= len(cluster)
    ysum/= len(cluster)

    distancia = math.sqrt((xsum-data[0])**2 + (ysum-data[1])**2)

    return distancia # devuelve la distancia entre los puntos y el cluster especifico

def clusterCercano(x,clusters):
    """
    x -> puntos (x,y) a los que se les quiere agregar a un cluster
    cluser -> matriz con todo los clusters 
    """
    preferedCluster = 0
    distancia = distanciaCluster(x, clusters[preferedCluster])

    for cluster in clusters[1]:
        nuevaDistancia= distanciaCluster(x,cluster)
        if nuevaDistancia < distancia:
            distancia = nuevaDistancia
            preferedCluster = clusters.index(cluster)

    return preferedCluster  # devuelve el cluster del que los puntos dados se encuentran mas cerca

def BSAS(listXY, maxDistance, maxClusters):
    clusterNumber=1
    clusters=[]
    clusters.append([])
    cluster = clusters[0]
    cluster.append(listXY[0])

    for x in listXY[1:]:
        cluster = clusterCercano(x,cluster)
        if(distanciaCluster( x,clusters[cluster])>maxDistance and clusterNumber < maxClusters):
            clusterNumber +=1
            clusters.append([x])
        else:
            clusters[cluster].append(x)


