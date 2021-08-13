import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x,y):
  n = np.size(x)
  #Obtenemos los promedios de X y Y
  prom_x, prom_y = np.mean(x), np.mean(y)
  
  #Calcular la sumatoria de X Y y sumatoria de xx
  sumatoria_xy = np.sum((x-prom_x)*(y-prom_y))
  sumatoria_xx = np.sum((x*(x-prom_x)))

  #Coeficientes de regresion.
  b_1 = sumatoria_xy / sumatoria_xx
  b_0 = prom_y - b_1 * prom_x
  return(b_0, b_1)

# Funcion de graficado.
def plot_regression(x,y,b):
  plt.scatter(x,y, color = "g", marker="o", s=30)

  y_pred = b[0] + b[1] * x
  plt.plot(x, y_pred, color = "b")

  #etiquetado
  plt.xlabel('x-Independiente')
  plt.ylabel('y-Dependiente')

  plt.show()

#Codigo main
def main():
  #Dataset
  x = np.array([1,2,3,4,5])
  y = np.array([2,3,5,6,5])

  #Obtener b1 y b2
  b = estimate_b0_b1(x,y)
  print("Los valores b_0 = {}, b1 = {}".format(b[0], b[1]))

  #Graficamos la linea de regresión
  plot_regression(x,y,b)

if __name__=="__main__":
  main()