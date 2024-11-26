import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm, expon, gamma, lognorm, probplot

# Estilo y personalización
custom = {
    "grid.linestyle": "dashed",  # Líneas punteadas
    "grid.color": "#B0B0B0",
    "axes.facecolor": "white",
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linewidth": 0.8,
}

sns.set(style="white", rc=custom)
sns.set_palette(sns.color_palette(["#38b73f"]))  # Verde pastel personalizado (sacado de photoshop, pastel, aunque no tanto)

# Cargar los datos desde un archivo CSV
df = pd.read_csv('ames-housing.csv')

# Seleccionar la variable de interés
sale_price = df['SalePrice']

# Histograma
plt.figure(figsize=(10, 6))
sns.histplot(sale_price, kde=False, bins=40)
plt.title('Histograma para la variable SalePrice')
plt.xlabel('Precio de venta')
plt.ylabel('Frecuencia')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()
plt.show()

sns.set_palette(sns.color_palette(["#53bed9"]))  # Celeste pastel

# Boxplot
plt.figure(figsize=(10, 2))
sns.boxplot(x=sale_price)
plt.title('Boxplot para la variable SalePrice')
plt.xlabel('Precio de venta')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()
plt.show()

sns.set_palette(sns.color_palette(["#b7384a"]))  # Rojo casi rosado

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x=sale_price)
plt.title('Violin plot para la variable SalePrice')
plt.xlabel('Precio de venta')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()  # Habilitar ticks menores
plt.show()

## PARTE 2

sns.set_palette(sns.color_palette(["#38b73f"]))  # Verde pastel

# Histograma con superposición de curva normal
plt.figure(figsize=(10, 6))
sns.histplot(sale_price, kde=False, bins=30)

# Superponer la curva de distribución normal
mu = sale_price.mean()
std = sale_price.std()
x = np.linspace(sale_price.min(), sale_price.max(), 100)
pdf = norm.pdf(x, mu, std)
plt.plot(x, pdf * len(sale_price) * (sale_price.max() - sale_price.min()) / 30, color='red', label='Curva normal teórica')

plt.title('Histograma de SalePrice con curva normal')
plt.xlabel('Precio de venta')
plt.ylabel('Densidad')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()  # Habilitar ticks menores
plt.legend()
plt.show()

# Análisis descriptivo
print("Media del precio de venta (mu):", mu)
print("Desviación estándar del precio de venta:", std)


## CURVA EXPONENCIAL

# Ajustar la distribución exponencial a los datos
param_expon = expon.fit(sale_price)  # Ajusta la distribución a los datos
lambda_expon = 1 / mu  # Calcula lambda manualmente

# Generar valores para la curva ajustada
pdf_expon = expon.pdf(x, *param_expon)

# Graficar el histograma y la curva exponencial ajustada
plt.figure(figsize=(10, 6))
sns.histplot(sale_price, kde=False, bins=30, stat='density', label='Histograma de datos')
plt.plot(x, pdf_expon, color='red', label='Curva exponencial ajustada')
plt.title('Ajuste de distribución exponencial a los datos')
plt.xlabel('Precio de venta')
plt.ylabel('Densidad')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()  # Habilitar ticks menores
plt.legend()
plt.show()


# Ajustar distribución Gamma
x = np.linspace(sale_price.min(), sale_price.max(), 100)
param_gamma = gamma.fit(sale_price)
pdf_gamma = gamma.pdf(x, *param_gamma)

# Graficar la distribución Gamma
plt.figure(figsize=(10, 6))
sns.histplot(sale_price, kde=False, bins=30, stat='density', label='Histograma de datos')
plt.plot(x, pdf_gamma, color='blue', label='Curva Gamma')
plt.title('Ajuste de distribución Gamma a los datos')
plt.xlabel('Precio de venta')
plt.ylabel('Densidad')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()  # Habilitar ticks menores
plt.legend()
plt.show()

# Ajustar la distribución lognormal
shape, loc, scale = lognorm.fit(sale_price, floc=0)  # floc=0 fuerza loc=0
pdf_lognorm = lognorm.pdf(x, shape, loc, scale)

# Graficar el histograma y la curva lognormal
plt.figure(figsize=(10, 6))
sns.histplot(sale_price, kde=False, bins=30, stat='density', label='Histograma')
plt.plot(x, pdf_lognorm, color='red', label='Curva Lognormal Ajustada')
plt.title('Histograma y Curva Lognormal Ajustada')
plt.xlabel('Precio de venta')
plt.ylabel('Densidad')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()  # Habilitar ticks menores
plt.legend()
plt.show()

# Generar el QQPlot
fig, ax = plt.subplots(figsize=(8, 8))
probplot(sale_price, dist="lognorm", sparams=(shape, loc, scale), plot=ax)
ax.get_lines()[1].set_color('red')  # Línea de referencia en rojo
ax.get_lines()[1].set_label('Cuantiles de los datos teóricos')  # Etiqueta para la línea
ax.get_lines()[0].set_label('Cuantiles de los datos experimentales')  # Etiqueta para los puntos
plt.title('QQPlot para la distribución lognormal ajustada')
plt.xlabel('Cuantiles teóricos')
plt.ylabel('Cuantiles de los datos')
plt.grid(alpha=0.3)
plt.legend()
plt.show()

## CURVA FINAL

sns.set_palette(sns.color_palette(["#38b73f"]))  # Verde pastel

# Histograma con curva de densidad
plt.figure(figsize=(10, 6))
sns.histplot(sale_price, kde=True, bins=40)
plt.title('Histograma y curva de densidad de SalePrice')
plt.xlabel('Precio de venta')
plt.ylabel('Densidad')
## # Personalizar la cuadrícula manualmente para duplicar la cantidad de líneas
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()  # Habilitar ticks menores
plt.show()

# Graficar el histograma, la curva lognormal y la real
plt.figure(figsize=(10, 6))
sns.histplot(sale_price, kde=False, bins=30, stat='density', label='Histograma')
sns.kdeplot(sale_price, label='Curva de la densidad teorica', color='red')
plt.plot(x, pdf_lognorm, color='blue', label='Curva Lognormal Ajustada')
plt.title('Histograma y Curva Lognormal Ajustada')
plt.xlabel('Precio de venta')
plt.ylabel('Densidad')
plt.grid(True, which='minor', axis='both', linestyle='--', color='#B0B0B0', alpha=0.5)
plt.minorticks_on()  # Habilitar ticks menores
plt.legend()
plt.show()

# Análisis descriptivo
print("Mediana del precio de venta:", sale_price.median())

# Parámetros de la distribución lognormal ajustada

# Probabilidad de que una casa cueste más de $200,000
prob_mas_200k = 1 - lognorm.cdf(200000, shape, loc=loc, scale=scale)

# Valor esperado del precio de las casas
valor_esperado = lognorm.mean(shape, loc=loc, scale=scale)

print("Probabilidad de que una casa cueste más de $200,000: ", prob_mas_200k)
print("Valor esperado del precio de las casas: ", valor_esperado)

# Valor esperado del precio de las casas
valor_esperado = lognorm.mean(shape, loc=loc, scale=scale)

print("Probabilidad de que una casa cueste más de $200,000: ", prob_mas_200k)
print("Valor esperado del precio de las casas: ", valor_esperado)
