# Informe sobre la API de ReqRes y OpenWeatherMap

## Índice
- [1. Introducción](#1-introducción)
- [2. Descripción de la API Reqres](#2-descripción-de-la-api-reqres)
- [3. Descripción de la API OpenWeatherMap](#3-descripción-de-la-api-openweathermap)
- [4. Bibliografía](#4-bibliografía)
- [5. Ejercicios](#5-ejercicios)

## 1. Introducción
Este informe proporciona una visión detallada de la API de ReqRes, una plataforma diseñada para pruebas de interacciones API mediante el uso de datos simulados de usuarios. Se discutirá su estructura, funcionalidades y los tipos de operaciones que soporta.

## 2. Descripción de la API Reqres
ReqRes es una API gratuita que simula cómo una aplicación real manejaría llamadas API en un entorno de producción. La API permite a los desarrolladores probar varios endpoints que simulan operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre datos de usuario. Las principales características incluyen:

- **Operaciones CRUD**: Permite a los usuarios crear, leer, actualizar y eliminar información de usuarios en un formato simplificado.
- **Paginación**: Soporta la navegación paginada de datos, lo cual es útil para simular escenarios del mundo real donde los conjuntos de datos son extensos.
- **Respuestas Diferidas**: Capacidad para simular tiempos de respuesta retrasados, permitiendo a los desarrolladores probar cómo sus aplicaciones manejarían las latencias.
- **Autenticación y Registro**: Provee endpoints para simular la autenticación y el registro de usuarios.


## 3. Descripción de la API OpenWeatherMap
OpenWeatherMap proporciona datos meteorológicos exhaustivos a través de diversas APIs. Estos datos incluyen información del clima en tiempo real, pronósticos y registros históricos. Algunas de sus principales características son:

- **Datos en tiempo real**: Temperatura, humedad, presión atmosférica, etc.
- **Pronósticos meteorológicos**: Pronósticos a corto y largo plazo.
- **Datos históricos**: Acceso a información climática pasada.

### 4. Bibliografía:

- [Reqres](https://reqres.in/)
- [OpenWeatherMap](https://openweathermap.org/api)

### 5. Ejercicios:

- **Ejercicio 2**
![apikey](apikey.png)

- **Ejercicio 3a**
![GET](GET.png)

- **Ejercicio 3b**
![POST](POST.png)
![PUT](PUT.png)

- **Ejercicio 3c**
![parametroID](parametroID.png)

- **Ejercicio 3d**
![consultas](consultas.png)

- **Ejercicio 3e**
![consultalogica](consultalogica.png)

- **Ejercicio 5**
```python
import requests
import pandas as pd
from weasyprint import HTML
response = requests.get("https://reqres.in/api/users")
data = response.json()["data"]
df = pd.DataFrame(data)
html_table = df.to_html()
HTML(string=html_display).write_pdf("usuarios.pdf")




