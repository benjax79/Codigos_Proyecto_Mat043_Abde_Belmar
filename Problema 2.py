import numpy as np

capacidad_avion1=150
capacidad_avion2=300
capacidad_avion3=400
simulacion_actual=0
cantidad_simulaciones=10000
asientos_total_simulaciones=[]

while simulacion_actual<cantidad_simulaciones:
    asiento_por_simulacion=0
    for i in range(250):
        asiento_por_simulacion+= np.random.poisson(0.07*capacidad_avion1)
    for i in range(145):
        asiento_por_simulacion+= np.random.poisson(0.07*capacidad_avion2)
    for i in range(87):
        asiento_por_simulacion+= np.random.poisson(0.07*capacidad_avion3)
    simulacion_actual+=1
    asientos_total_simulaciones.append(asiento_por_simulacion)

print("Cantidad de asiento extra vendidos:",round(np.mean(asientos_total_simulaciones)))