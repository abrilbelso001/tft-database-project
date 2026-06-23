# TFT Database Project

Proyecto de base de datos relacional inspirado en **Teamfight Tactics (TFT)**, desarrollado para la asignatura de **Sistemas de Información**.

El objetivo del proyecto es aplicar los conocimientos adquiridos durante la asignatura mediante el diseño, normalización e implementación de una base de datos relacional. Para ello, se ha elegido como contexto el videojuego Teamfight Tactics, modelando información relacionada con sets, campeones, rasgos, composiciones, ítems, componentes y posicionamiento.

## Contexto académico

Este proyecto ha sido realizado como trabajo individual para la asignatura de **Sistemas de Información**.

A través de este trabajo se ponen en práctica conceptos fundamentales del diseño de bases de datos, como:

- Análisis de requisitos.
- Diseño del modelo Entidad-Relación.
- Transformación al modelo relacional.
- Normalización del modelo.
- Creación de tablas en SQL.
- Consultas sobre una o varias tablas.
- Subconsultas.
- Consultas agrupadas.
- Cuantificación universal.
- Integración de SQL con Python.

Además, el proyecto incluye una pequeña aplicación de consola en Python que permite interactuar con la base de datos y ejecutar algunas consultas de forma sencilla.

## Descripción

Teamfight Tactics es un videojuego de estrategia tipo *auto battler* en el que los jugadores crean composiciones combinando campeones, rasgos, ítems, componentes y posicionamiento.

A partir de este contexto, se ha diseñado una base de datos relacional que permite organizar la información principal del juego de forma estructurada. El proyecto no solo se centra en crear las tablas, sino también en justificar el diseño mediante el modelo Entidad-Relación, comprobar la normalización y realizar consultas SQL que permitan obtener información relevante.

La elección de TFT como temática permite trabajar con relaciones variadas entre entidades, como relaciones 1:N, N:M y relaciones entre composiciones, campeones e ítems.

## Tecnologías utilizadas

- MySQL
- SQL
- Python
- mysql-connector-python
- draw.io
- GitHub

## Estructura del proyecto

```text
TFT-DATABASE-PROJECT/
│
├── database/
│   └── tft.sql
│
├── docs/
│   └── TFT.pdf
│
├── src/
│   └── tft.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Contenido del proyecto

### Base de datos

El archivo `database/tft.sql` contiene la creación de la base de datos y sus tablas.

La base de datos almacena información sobre:

- Sets
- Campeones
- Rasgos
- Escalones de rasgo
- Composiciones
- Ítems
- Componentes
- Posicionamiento
- Builds de campeones

### Documentación

En la carpeta `docs/` se incluye la presentación del proyecto:

- [`TFT.pdf`](docs/TFT.pdf)

En ella se explica el contexto del proyecto, la normalización del modelo, consultas SQL y la demostración con Python.

### Programa en Python

El archivo `src/tft.py` contiene un programa de consola que se conecta a MySQL y permite ejecutar consultas sobre la base de datos.

Funcionalidades principales:

1. Buscar composiciones donde aparece un campeón.
2. Ver la build de un campeón en una composición.
3. Contar campeones por composición.

## Normalización

El modelo ha sido normalizado aplicando:

- 1FN: atributos atómicos.
- 2FN: dependencia completa de la clave primaria.
- 3FN: ausencia de dependencias transitivas.
- BCNF: los determinantes son claves.

Además, las relaciones N:M se han separado en tablas intermedias, como:

- `ComposicionCampeon`
- `ComposicionCampeonItem`
- `ItemComponente`

## Ejemplos de consultas SQL

### Buscar composiciones donde aparece un campeón

```sql
SELECT c.nombreComposicion, c.tier
FROM composicion c
JOIN composicioncampeon cc
    ON c.idComposicion = cc.idComposicion
JOIN campeon ca
    ON cc.idCampeon = ca.idCampeon
WHERE ca.nombreCampeon = 'Ashe';
```

### Contar campeones por composición

```sql
SELECT c.nombreComposicion,
       COUNT(cc.idCampeon) AS numCampeones
FROM composicion c
LEFT JOIN composicioncampeon cc
    ON c.idComposicion = cc.idComposicion
GROUP BY c.idComposicion, c.nombreComposicion
ORDER BY numCampeones DESC;
```

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tft-database-project.git
cd tft-database-project
```

Cambia `tu-usuario` por tu usuario real de GitHub.

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Importar la base de datos

Importa el archivo SQL en MySQL o phpMyAdmin:

```text
database/tft.sql
```

### 4. Configurar la conexión

En el archivo `src/tft.py`, revisa los datos de conexión:

```python
host="localhost"
user="root"
password=""
database="tft"
```

Si tu usuario o contraseña de MySQL son diferentes, cámbialos antes de ejecutar el programa.

### 5. Ejecutar el programa

```bash
python src/tft.py
```

## Ejemplo de uso

```text
--- MENÚ TFT ---
1. Buscar composiciones donde aparece un campeón
2. Ver la build de un campeón en una composición
3. Contar campeones por composición
4. Salir
```

## Objetivo del proyecto

El objetivo principal es demostrar el proceso completo de diseño de una base de datos relacional, desde el análisis inicial hasta su implementación y uso mediante consultas.

Con este proyecto se busca:

- Representar correctamente las entidades y relaciones del sistema.
- Evitar redundancias mediante la normalización.
- Crear una base de datos funcional en MySQL.
- Realizar consultas SQL de distinto nivel de complejidad.
- Conectar la base de datos con un programa en Python.
- Presentar el trabajo de forma clara y organizada.

## Autora

Proyecto desarrollado por **Abril Belso Sánchez** como trabajo individual para la asignatura de **Sistemas de Información**.

Grado en Ingeniería de la Ciberseguridad con Ingeniería Informática.

## Aviso

Este proyecto tiene fines educativos y no está afiliado oficialmente con Riot Games ni con Teamfight Tactics.