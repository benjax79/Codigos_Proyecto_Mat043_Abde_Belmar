import numpy as np

numero_simulaciones=0
trabajo_diario=360 # 6 horas en minutos
trabajado=0 # Por dia en minutos
operados=0 # Total operados por mes
operados_simulacion=[]
while numero_simulaciones<10000 :
    operados=0 # Se reinicia los operados por simulacion
    for i in range(30): # operados en 30 dias
        while True: # operados por dia
            preoperatorio= np.random.normal(16,4)
            operatorio= np.random.exponential(56)
            postoperatorio= np.random.uniform(15,25)
            trabajado+=preoperatorio+operatorio+postoperatorio
            if trabajado>trabajo_diario: # Si no se alcanzaba a operar no se contabiliza
                break
            operados+=1
        trabajado=0    # Nueva jornada de 6 horas
    operados_simulacion.append(operados)
    numero_simulaciones=numero_simulaciones+1
    
print("Numero aproximado de pacientes atendido por mes:",round(np.mean(operados_simulacion)))