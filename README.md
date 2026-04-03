# 🎓 Academic Schedule System

Sistema de gestión de horarios académicos desarrollado en Python utilizando SQLite.

## Descripción

Este proyecto permite a los usuarios gestionar materias y crear horarios académicos de manera sencilla desde la consola.

Incluye autenticación de usuarios, diferenciación de roles y conexión a base de datos.

#### (Proximamente interfaz visual).

---

## Funcionalidades

### Autenticación

* Inicio de sesión
* Creación de usuarios
* Validación de credenciales

### Administrador

* Ver materias
* Agregar materias *(en desarrollo)*
* Eliminar materias *(en desarrollo)*

### Estudiante

* Ver materias
* Crear horario *(en desarrollo)*
* Consultar horario *(en desarrollo)*

---

## Tecnologías utilizadas

* Python 3.14.3
* SQLite3
* Programación modular

---

## 📂 Estructura del proyecto

```txt
project/
├── connection_db.py
├── login.py
├── main_menu.py
├── main.py
├── schedule_manager.py
├── README.md
│── .gitignore
├── database/
└── scripts/
    └── create_db.py
```

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio:

```
git clone https://github.com/LinoSimon20/academic-schedule-system.git
```

2. Ejecutar el programa:

```
python3 main.py
```

---

## Base de datos

El sistema utiliza SQLite.
La base de datos contiene tablas como:

* usuarios
* materias
* horarios
* carreras
* menciones

> La base de datos `.db` no está incluida en el repositorio.
> Se recomienda generar una nueva mediante script (create_db.py) en: scripts/.

```bash
python3 scripts/create_db.py
```
---

## Usuarios de prueba

| Usuario    | Contraseña | Rol           |
| ---------- | ---------- | ------------- |
| admin      | 1234       | Administrador |
| estudiante | 1234       | Estudiante    |

---

## Estado del proyecto

En desarrollo...

Próximas mejoras:

* Gestión completa de materias
* Sistema de horarios sin conflictos
* Mejoras en interfaz de usuario
* Validaciones adicionales

---

## Autor

Desarrollado por Lino 💻
