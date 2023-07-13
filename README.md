# Finkargo Test

Este es un proyecto de ejemplo que demuestra el uso de: 

1 . los principios SOLID 
2 . uso de repositories 
3 . el patrón Singleton.
4 . Arquitectura Hexagonal

## CI
Se implemento un flujo para CI para la validacion de pruebas unitarias , linter y formato del codigo para pririzar la calidad al momento de realizar el merge a la rama master


![Screenshot 2023-07-13 at 3 50 16 AM](https://github.com/SebastianNorenaMarquezMiso/Finkargo/assets/78800255/bc53b325-dff2-4070-837e-6cf721cd0c4a)


## Coleccion de postman 
https://github.com/SebastianNorenaMarquezMiso/Finkargo/blob/main/TEST.postman_collection.json

## Requisitos

- Python 3.8 o superior

## Instalación

1. Clona este repositorio:

git clone https://github.com/SebastianNorenaMarquezMiso/Finkargo.git

2. Accede al directorio del proyecto:
cd Finkargo

3. instalar poetry:
brew install poetry

4. Instala las dependencias del proyecto utilizando `poetry`:

poetry install

## Ejecución

Para ejecutar el proyecto, asegúrate de tener las dependencias instaladas siguiendo los pasos anteriores. Luego, puedes ejecutar el siguiente comando:


poetry run python main.py

Esto iniciará la aplicación y estará disponible en `http://localhost:5000`.

## Unit Tests

El proyecto utiliza `pytest` para ejecutar las pruebas unitarias. Asegúrate de tener las dependencias de desarrollo instaladas siguiendo los pasos anteriores. Para ejecutar las pruebas, utiliza el siguiente comando:


poetry run pytest
Esto ejecutará todas las pruebas unitarias y mostrará los resultados.

## Dependencias

El proyecto utiliza las siguientes librerías y herramientas:

- Flask : Un framework web para crear APIs rápidas en Python.
- Poetry: Una herramienta para administrar dependencias y entornos virtuales de Python.
- Pytest: Un marco de pruebas para escribir y ejecutar pruebas unitarias en Python.

## Uso de Repositories

En este proyecto, se utiliza el patrón Repository para separar la lógica de acceso a datos de la lógica de negocio. Los repositories proporcionan una abstracción sobre el almacenamiento de datos y permiten intercambiar fácilmente implementaciones sin afectar otras partes del código.

## Uso de Singleton

El patrón Singleton se utiliza en el archivo `database.py` en el directorio `database` para asegurar que solo exista una única instancia de la base de datos en toda la aplicación. Esto garantiza que el acceso a la base de datos sea consistente y evita problemas de concurrencia.

## Principios SOLID

El proyecto sigue los principios SOLID para escribir código modular, extensible y mantenible. Estos principios incluyen:

- **Single Responsibility Principle (SRP)**: Cada clase tiene una única responsabilidad.
- **Open-Closed Principle (OCP)**: Las entidades deben estar abiertas para extensión pero cerradas para modificación.
- **Liskov Substitution Principle (LSP)**: Los objetos de un programa deben ser reemplazables por instancias de sus subtipos sin alterar la corrección del programa.
- **Interface Segregation Principle (ISP)**: Los clientes no deben verse obligados a depender de interfaces que no usan.
- **Dependency Inversion Principle (DIP)**: Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
