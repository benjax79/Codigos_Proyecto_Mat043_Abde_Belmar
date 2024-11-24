import numpy as np

casos_favorables=0 # Atencion mayor a 500 autos
casos_totales=0 
cantidad_simulaciones=1000
simulacion_actual=0

while simulacion_actual<cantidad_simulaciones:
    atenciones_por_simulacion=0
    ventanilla1=np.random.normal(150,6)
    ventanilla2=np.random.normal(163,14)
    ventanilla3=np.random.exponential(180)
    atenciones_por_simulacion=ventanilla1+ventanilla2+ventanilla3
    casos_totales+=1
    if atenciones_por_simulacion>500:
        casos_favorables+=1
    simulacion_actual+=1

probabilidad=casos_favorables/casos_totales
print("Probabilidad de atender mas de 500 autos diarios",probabilidad)
    