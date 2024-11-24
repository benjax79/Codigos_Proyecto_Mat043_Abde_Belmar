import numpy as np

simulacion_actual=0
simuciones_totales=10**6 #Un millon de simulaciones para mayor presicion
Valor_teorico=2/np.sqrt(np.pi) #Valor obtenido a traves de desarrollo analitico
distancias_totales=[]

while simulacion_actual<simuciones_totales:
    X=np.random.standard_normal()
    Y=np.random.standard_normal()
    distancias_totales.append(abs(X-Y))
    simulacion_actual+=1  
Valor_simulado=np.mean(distancias_totales)
Error_porcentual=(abs( (Valor_simulado-Valor_teorico) /Valor_teorico) ) *100                     

print("VALORES OBTENIDOS :")
print(f"Valor teorico  = {Valor_teorico}")
print(f"Valor simulado = {Valor_simulado}") #Esperanza entre todas las simulaciones obtenidas
print(f"\nError relativo porcentual ={Error_porcentual: .3f}%")