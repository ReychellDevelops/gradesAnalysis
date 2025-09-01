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

#se crea funcion calcularPromedioGeneral para calcular el promedio del curso
def calcularPromedioGeneral(df):
    promedioGeneral = df["definitiva"].mean(axis=0) 
    return promedioGeneral

#funcion contarAprobados que calcula el total de estudiantes con definitiva > 3.0
def contarAprobados(df, columna="definitiva"):
        return (df[columna] > 3.0).sum()

#funcion contarAprobados que calcula el total de estudiantes con definitiva < 3.0
def contarReprobados(df, columna="definitiva"):
        return (df[columna] < 3.0).sum()

def mejoresPromedios(df):
    columnaMejorEstudiante =["codigo","nombre","definitiva"]
    df_filtrado = df[columnaMejorEstudiante].sort_values(by = "definitiva",ascending = False).head(5)
    return df_filtrado

def peoresPromedios(df):
    columnaPeorEstudiante =["codigo","nombre","definitiva"]
    df_filtrado = df[columnaPeorEstudiante].sort_values(by = "definitiva",ascending = True).head(5)
    return df_filtrado

def notaMaxima(df):
    columnaMejorNota =["codigo","nombre","definitiva"]
    df_filtrado = df[columnaMejorNota].sort_values(by = "definitiva",ascending = False).head(1)
    return df_filtrado

def notaMinima(df):
    columnaPeorNota =["codigo","nombre","definitiva"]
    df_filtrado = df[columnaPeorNota].sort_values(by = "definitiva",ascending = True).head(1)
    return df_filtrado
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

        print("\n\n--------------------------PROMEDIO GENERAL DEL CURSO--------------------------")
        #calcularPromedioGeneral
        promedioGeneral = calcularPromedioGeneral(df)
        print(f"\nEl promedio general del curso es: {promedioGeneral}\n\n")

        print("----------------------------ESTUDIANTES APROBADOS---------------------------")
        #contarAprobados
        aprobados = contarAprobados(df)
        print(f"\nEl total de aprobados es: {aprobados}")

        print("----------------------------ESTUDIANTES REPROBADOS---------------------------")
        #contarReprobados
        reprobados = contarReprobados(df)
        print(f"\nEl total de reprobados es: {reprobados}")

        #mejoresPromedios
        print("----------------------------MEJORES 5 PROMEDIOS---------------------------")
        
        mejorPromedio = mejoresPromedios(df)
        print(f"\nLos 5 mejores promedios son:\n {mejorPromedio}")

         #peoresPromedios
        print("----------------------------PEORES 5 PROMEDIOS---------------------------")
        
        peorPromedio = peoresPromedios(df)
        print(f"\nLos 5 peores promedios son:\n {peorPromedio}")

        #notaMaxima
        print("----------------------------MEJOR ESTUDIANTE---------------------------")
        
        notaMasAlta = notaMaxima(df)
        print(f"\nMejor estudiante:\n {notaMasAlta}")

        #notaMinima
        print("----------------------------PEOR ESTUDIANTE---------------------------")
        
        notaMasBaja = notaMinima(df)
        print(f"\nMejor estudiante:\n { notaMasBaja}")


       



    except Exception as e: #si hay algun error al leer el archivo, la excepcion se guarda en la variable e y la muestra en el print
        print(f"❌ Error al leer el archivo CSV: {e}")

if __name__ == "__main__":
    main()

