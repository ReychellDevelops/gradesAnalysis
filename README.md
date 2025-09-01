# 📘 Proyecto de Gestión de Notas

Este es un proyecto en **Python** que permite analizar y gestionar las notas de un curso a partir de un archivo CSV.

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/TU_USUARIO/gradesAnalysis.git
   cd gradesAnalysis
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   # En Windows PowerShell
   venv\Scripts\Activate.ps1
   # En Linux/Mac
   source venv/bin/activate
   ```

3. Instalar dependencias:

   ```bash
   pip install pandas
   ```

4. Ejecutar el programa principal:

   ```bash
   python src/main.py
   ```

---

## 📂 Estructura del proyecto

```
gradesAnalysis/
│── data/
│   └── notes.csv      # Archivo CSV con las notas
│── src/
│   └── main.py        # Programa principal
│── venv/              # Entorno virtual (ignorar en Git)
│── README.md          # Este archivo
```

---

## 👥 Colaboración en equipo con Git

### 🔹 Crear tu propia rama

Cada integrante debe crear una rama para trabajar en su parte:

```bash
git checkout -b feature/tu-funcion
```

Ejemplo:

```bash
git checkout -b feature/contar_aprobados
```

---

### 🔹 Guardar cambios en tu rama

```bash
git add .
git commit -m "Implementé la función contar_aprobados"
git push origin feature/contar_aprobados
```

---

### 🔹 Hacer un Pull Request

1. Entra a GitHub.
2. Te aparecerá un botón para **abrir un Pull Request (PR)**.
3. Describe qué hiciste y pide revisión.

---

## 📌 Funciones por desarrollar

Cada integrante debe implementar una función en `main.py` (o en un nuevo archivo dentro de `src/` si prefieren modularizar):

* [✅] **contarEstudiantes(df)** → Total de estudiantes (hecho ✅).
* [✅] **calcularPromedio(df)** → Promedios de cada estudiante.(hecho ✅)
* [✅] **calcularPromedioGeneral(df)** → Promedio general del curso. (hecho ✅)
* [✅] **contarAprobados(df)** → Número de estudiantes que aprobaron. (hecho ✅)
* [✅] **contarReprobados(df)** → Número de estudiantes que perdieron. (hecho ✅)
* [✅] **mejoresPromedios(df)** → Mejores 5 promedios del curso. (hecho ✅)
* [✅ ] **peoresPromedios(df)** → Peores 5 promedios del curso. (hecho ✅)
* [✅ ] **notaMaxima(df)** → Nota más alta. (hecho ✅)
* [✅ ] **notaMinima(df)** → Nota más baja. (hecho ✅)
* [ ] **graficasPorcentajeAprobados** → Grafica el porcentaje de estudiantes que aprobaron y perdieron

---

## 📧 Equipo

* Juan Aldana
* Erick Rodriguez
* Reychell Veloza
