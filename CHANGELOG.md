# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.0] - 2026-05-17
### Added
- Implementación completa de creación de horario académico para usuarios.
- Implementación de consulta de horario con visualización en tabla.
- Agregado soporte para eliminación de entradas del horario.
- Funcionalidad de agregar materia desde el menú principal.
- Funcionalidad de eliminar materia desde el menú principal.
- Nuevas vistas para mostrar días, horas, materias y horarios con formato mejorado.
- Nuevo módulo `models/schedule.py` para gestionar datos de horario.

### Changed
- Reestructuración del menú principal en `controllers/menu_controller.py` añadiendo opciones de horario.
- Mejoras en `views/menu_view.py` y `views/auth_view.py` con documentación en español.
- Actualización de `controllers/schedule_controller.py` para manejar creación, consulta y eliminación de horario.
- Normalización de la conexión a la base de datos desde `models/db.py`.
- `main.py` mantiene la creación automática de la base de datos y el inicio del flujo de autenticación.

### Fixed
- Corrección de la lógica de presentación de materias y validación de datos.
- Manejo de errores más robusto al crear usuarios y al manipular el horario.

## [0.1.0] - Baseline
### Added
- Estructura básica del proyecto con módulos separados en `controllers/`, `models/`, `views/`, `scripts/` y `legacy/`.
- Autenticación de usuario con inicio de sesión y registro.
- Creación inicial de base de datos SQLite y tablas básicas mediante `scripts/create_db.py`.
- Visualización de materias en consola.
- Archivo `models/db.py` como punto único de conexión reutilizable a la base de datos.

### Changed
- Arquitectura inicial modular sin soporte completo de horario académico.

### Deprecated
- No se aplicó.
