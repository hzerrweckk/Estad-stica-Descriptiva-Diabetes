# Usa: open, close, readlines, rstrip, split
def leer_csv_a_matriz(ruta):
 matriz = []
 f = open(ruta, "r", encoding="utf-8")
 lineas = f.readlines()
 for linea in lineas:
  cols= linea.rstrip("\n").split(",")
  matriz.append(cols)
 f.close()
 return matriz

def main():
  datos = leer_csv_a_matriz("titanic.csv")
  print(datos[0])
  print(datos[1])
  print("Numero de objetos = ",len(datos))
  print("La variable 2 del objeto 4 = ", datos[4][1])
main()
