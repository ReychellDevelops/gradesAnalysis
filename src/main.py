# main.py - programa principal

#importacion de librerias

import os #libreria que permite trabajar con archivos del sistema operativo
import pandas as pd #libreria para el analisis de datos, en este caso para el analisis de un csv

#definicion de funcion para realizar conteo del total de estudiantes
def contarEstudiantes(df):
    #retorna el numero total de estudiantes del dataframe (tabla)
    return len(df)

#se define la funcion como calcularPromedio para realizar el calculo
def calcularPromedio(df):
    columnaNotas = ["parcial","quices","investigacion","taller","trabajo"] #se asigna el nombre de las columnas para cada valor
    df["definitiva"] = df[columnaNotas].mean(axis=1)  #se agrega la columna definitiva para agregarle el promedio de cada fila
    return df
   

#definicion de funcion principal main
def main():
    """
    Punto de entrada principal del programa.
    Se encarga de cargar el archivo CSV y mostrar las notas.
    """

    print("----------- PROYECTO DE GESTIÓN DE NOTAS -----------")

    #ruta del archivo csv de manera portable
    data_path = os.path.join("data", "notes.csv") #path es una sublibreria de os que nos ayuda a indicar bien la ruta segun el sistema operativo y join coloca bien los separadores(/ mac \\ windows)

    #verificamos si el archivo existe
    if not os.path.exists(data_path): #el .exists nos permite verificar si un archivo existe
        print(f"⚠️ No se encontró el archivo: {data_path}")
        return
    
    #cargue de datos del archivo notes.csv usando libreria pandas para que nos muestre los datos en forma de tabla
    try: #intentaejecutar el bloque de codigo, si todo sale bien muestra la tabla con los datos
        df = pd.read_csv(data_path, sep=";")
        print("\n📊 Datos cargados correctamente:\n")
        print(df) #mostrar tabla

        #llamamos la funcion contarEstudiantes asignandole su retorno a la variable total
        #Contar estudiantes
        total = contarEstudiantes(df) #le enviamos el argmento df a la funcion para que lo pueda evaluar
        print(f"\n👩‍🎓👨‍🎓 Número de estudiantes en el curso: {total}\n\n")

        print("--------------------------PROMEDIO DE LOS ESTUDIANTES-------------------------\n")
        #calcularPromedio
        promedios = calcularPromedio(df)
        print(promedios)
    except Exception as e: #si hay algun error al leer el archivo, la excepcion se guarda en la variable e y la muestra en el print
        print(f"❌ Error al leer el archivo CSV: {e}")

if __name__ == "__main__":
    main()

