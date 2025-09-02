# main.py - programa principal

#importacion de librerias

import os #libreria que permite trabajar con archivos del sistema operativo
import pandas as pd #libreria para el analisis de datos, en este caso para el analisis de un csv
import matplotlib.pyplot as plt

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
    return (df[columna] > 3.0).sum() #si el valor de la columna dentro del archivo es >3.0 se va sumando y retorna dicha suma

def tablaAprobados(df, columna = "definitiva"):
    columnaMejorEstudiante =["codigo","nombre",columna] #indicamos nombres de columnas a evaluar
    df_aprobados = df[df[columna] > 3.0][columnaMejorEstudiante]
    return df_aprobados

#funcion contarAprobados que calcula el total de estudiantes con definitiva < 3.0
def contarReprobados(df, columna="definitiva"):
    return (df[columna] < 3.0).sum() #si el valor de la columna dentro del archivo es <3.0 se va sumando y retorna dicha suma

def tablaReprobados(df, columna = "definitiva"):
    columnaPeorEstudiante =["codigo","nombre",columna]
    df_reprobados = df[df[columna] < 3.0][columnaPeorEstudiante]
    return df_reprobados

#funcion para ordenar descendentemente la tbla en los valores ["codigo","nombre","definitiva"] y mostrar los 5 mejores
def mejoresPromedios(df):
    columnaMejorEstudiante =["codigo","nombre","definitiva"] #indicamos nombres de columnas a evaluar
    df_filtrado = df[columnaMejorEstudiante].sort_values(by = "definitiva",ascending = False).head(10) #ordenamos descendentemente y sleccionamos 5 primeras
    return df_filtrado

#funcion para ordenar ascendentemente la tbla en los valores ["codigo","nombre","definitiva"] y mostrar los 5 peores
def peoresPromedios(df):
    columnaPeorEstudiante =["codigo","nombre","definitiva"] 
    df_filtrado = df[columnaPeorEstudiante].sort_values(by = "definitiva",ascending = True).head(5) #ordenamos ascendentemente y sleccionamos 5 primeras
    return df_filtrado

#funcion para mostrar nota maxima
def notaMaxima(df):
    columnaMejorNota =["codigo","nombre","definitiva"]
    df_filtrado = df[columnaMejorNota].sort_values(by = "definitiva",ascending = False).head(1) #se ordena la lista desecendentemente y se muestra el primero
    return df_filtrado

#funcion par mostrar nota minima
def notaMinima(df):
    columnaPeorNota =["codigo","nombre","definitiva"]
    df_filtrado = df[columnaPeorNota].sort_values(by = "definitiva",ascending = True).head(1) #se ordena la lista asecendentemente y se muestra el primero
    return df_filtrado

def graficasPorcentaje(aprobados, reprobados):
    cifrasCartera = [aprobados, reprobados]
    colores = ['#238E23', 'red']
    nombresCartera = ['Aprobaron', 'Perdieron'] 
    desfase = (0.1, 0.1)

    # Configuración del gráfico
    plt.figure(figsize=(6, 6))
    plt.title('Porcentaje de estudiantes que aprobaron y perdieron', fontsize=14)
    plt.axis('equal')  # Hace que el pastel sea redondo

    # Datos para el pie chart
    # nombrescartera = ["Aprobados", "Reprobados"]
    # cifrascartera = [aprobados, reprobados]
    # colores = ["#4CAF50", "#F44336"]
    # desfase = [0.05, 0]  # separa un poco la primera porción

    # Crear gráfico de pastel
    _, _, textos = plt.pie(
        cifrasCartera,
        labels=nombresCartera,
        autopct="%0.1f%%",
        colors=colores,
        explode=desfase
    )

    # Cambiar color de los porcentajes a blanco
    for tex in textos:
        tex.set_color('white')

    # Mostrar gráfico
    return plt.show()

def graficasNotasDefinitivas(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df["nombre"], df["definitiva"], color="#4682B4")
    plt.axhline(3.0, color="red", linestyle="--", label="Línea de aprobación")

    plt.title("Notas Definitivas por Estudiante", fontsize=14)
    plt.xlabel("Estudiantes")
    plt.ylabel("Nota definitiva")
    plt.xticks(rotation=45)
    plt.legend()
    return plt.show()

def graficasMejores10(df):
    Mejores10 = df.sort_values(by="definitiva", ascending=False).head(10)

    plt.figure(figsize=(8, 6))
    plt.barh(Mejores10["nombre"], Mejores10["definitiva"], color="#2E8B57")

    plt.title("Mejores 10 promedios", fontsize=14)
    plt.xlabel("Nota definitiva")
    plt.gca().invert_yaxis()
    return plt.show()

def graficasPeores5(df):
    Peores5 = df.sort_values(by="definitiva", ascending=True).head(5)

    plt.figure(figsize=(8, 6))
    plt.barh(Peores5["nombre"], Peores5["definitiva"], color="#FF8C00")

    plt.title("Peores 5 promedios", fontsize=14)
    plt.xlabel("Nota definitiva")
    plt.gca().invert_yaxis()
    return plt.show()

def graficasResumen(df):
    nota_max = df["definitiva"].max()
    nota_min = df["definitiva"].min()
    nota_prom = df["definitiva"].mean()

    valores = [nota_min, nota_prom, nota_max]
    etiquetas = ["Nota mínima", "Promedio general", "Nota máxima"]
    colores = ["#CD5C5C", "#1E90FF", "#32CD32"]

    plt.figure(figsize=(7, 6))
    plt.bar(etiquetas, valores, color=colores)

    plt.title("Resumen de notas", fontsize=14)
    plt.ylabel("Valor de la nota")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.05, f"{v:.2f}", ha='center', fontsize=10, color="black")
    return plt.show()



#definicion de funcion principal main
def main():
    """
    Punto de entrada principal del programa.
    Se encarga de cargar el archivo CSV y mostrar las notas.
    """

    print("----------- PROYECTO DE GESTIÓN DE NOTAS -----------")

    #ruta del archivo csv de manera portable
    data_path = os.path.join("gradesAnalysis","data", "notes.csv") #path es una sublibreria de os que nos ayuda a indicar bien la ruta segun el sistema operativo y join coloca bien los separadores(/ mac \\ windows)

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
        tablaA = tablaAprobados(df)
        print(f"\nEl total de aprobados es: {aprobados}")
        print(f"\nLos aprobados son: \n{tablaA}")

        print("----------------------------ESTUDIANTES REPROBADOS---------------------------")
        #contarReprobados
        reprobados = contarReprobados(df)
        tablaR = tablaReprobados(df)
        print(f"\nEl total de reprobados es: {reprobados}")
        print(f"\nLos reprobados son: \n{tablaR}")

        #mejoresPromedios
        print("----------------------------MEJORES 10 PROMEDIOS---------------------------")
        
        mejorPromedio = mejoresPromedios(df)
        print(f"\nLos 10 mejores promedios son:\n {mejorPromedio}")

         #peoresPromedios
        print("----------------------------PEORES 5 PROMEDIOS---------------------------")
        
        peorPromedio = peoresPromedios(df)
        print(f"\nLos 5 peores promedios son:\n {peorPromedio}")

        #notaMaxima
        print("----------------------------MEJOR ESTUDIANTE---------------------------")
        
        notaMasAlta = notaMaxima(df)
        print(f"\nMejor estudiante:\n {notaMasAlta}\n")

        #notaMinima
        print("----------------------------PEOR ESTUDIANTE---------------------------")
        
        notaMasBaja = notaMinima(df)
        print(f"\nMejor estudiante:\n { notaMasBaja}\n")

        #graficas 
        print("----------------------------GRAFICA PORCENTAJE APROBADOS---------------------------\n")
        print(graficasPorcentaje(aprobados, reprobados))

        print("----------------------------GRAFICA NOTAS DEFINITIVAS---------------------------\n")
        print(graficasNotasDefinitivas(df))

        print("----------------------------GRAFICA 10 MEJORES---------------------------\n")
        print(graficasMejores10(df))

        print("----------------------------GRAFICA 5 PEORES---------------------------\n")
        print(graficasPeores5(df))

        print("----------------------------GRAFICA RESUMEN---------------------------\n")
        print(graficasResumen(df))

    except Exception as e: #si hay algun error al leer el archivo, la excepcion se guarda en la variable e y la muestra en el print
        print(f"❌ Error al leer el archivo CSV: {e}")

if __name__ == "__main__":
    main()

