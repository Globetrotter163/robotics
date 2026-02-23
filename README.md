# ROS 2 Packages – IMT-342 Robótica

## Overview

Este repositorio contiene **packages desarrollados en ROS 2** como parte de la materia **IMT-342 Robótica**. El objetivo principal es **documentar el progreso académico**, incluyendo **tareas, prácticas y evaluaciones**, utilizando una estructura clara y estandarizada acorde a proyectos ROS 2.

El repositorio está pensado **exclusivamente con fines educativos** y no como un framework listo para producción.

---

## ROS 2 Distribution

* **ROS 2 Jazzy**

---

## Repository Structure

El repositorio se utiliza como contenedor de packages dentro de un workspace ROS 2:

```text
ros2_ws/
└── src/
    └── mypkg/
        ├── package.xml
        ├── CMakeLists.txt
        ├── src/
        ├── launch/
        └── ...
```

Cada package refleja el avance en distintos temas vistos en clase (nodos, tópicos, servicios, parámetros, launch files, etc.).

---

## Build Instructions

Se asume que el usuario ya tiene **ROS 2 Jazzy correctamente instalado**.

### 1. Clonar el repositorio

Desde el directorio `src` del workspace:

```bash
cd ros2_ws/src
git clone git@github.com:CarlosMenacho/mypkg.git
```

### 2. Compilar el workspace

```bash
cd ros2_ws
colcon build
```

### 3. Source del workspace

```bash
source install/setup.bash
```

---

## Usage

El uso específico depende del package evaluado (tarea, práctica o examen). Cada uno puede incluir:

* Nodos en C++ y/o Python
* Launch files
* Configuración de parámetros

Cuando sea relevante, cada package incluirá instrucciones propias en su directorio.

---

## Scope and Limitations

* Proyecto **educativo**, no orientado a uso industrial
* El código puede cambiar frecuentemente
* No se garantiza compatibilidad con otras distribuciones ROS 2
* Algunas implementaciones priorizan claridad didáctica sobre eficiencia

---

## Evaluation Context

Este repositorio se utiliza para:

* Seguimiento de progreso académico
* Entrega de tareas y evaluaciones
* Revisión de buenas prácticas básicas en ROS 2

---

## Roadmap

* [ ] Incorporar descripciones breves por package
* [ ] Añadir diagramas simples de nodos cuando aplique
* [ ] Mejorar comentarios y documentación interna

---

## Author

**Carlos Menacho**
Estudiante – IMT-342 Robótica
