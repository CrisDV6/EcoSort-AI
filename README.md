# EcoSort AI

Proyecto integrador de quinto semestre de Ingeniería en Software.

EcoSort AI es un sistema inteligente para identificar y clasificar residuos reciclables de plástico y vidrio mediante una Raspberry Pi, visión artificial e inteligencia artificial. El proyecto integra hardware, un sistema experto, servicios de plataforma y nube, una interfaz web con dashboard y documentación de gestión de proyectos.

## Objetivo inicial

Construir un prototipo funcional, modular y defendible que capture imágenes de residuos, determine si corresponden a plástico o vidrio y registre los resultados para su consulta y análisis.

## Módulos del proyecto

- `backend`: API y lógica del servidor.
- `frontend`: interfaz web y dashboard.
- `ai_model`: entrenamiento, evaluación y despliegue del modelo de IA.
- `raspberry`: captura de imágenes y ejecución en Raspberry Pi.
- `database`: esquema y recursos de base de datos.
- `images`: imágenes de plástico, vidrio y pruebas.
- `docs`: documentación técnica y académica.
- `diagrams`: diagramas de arquitectura y funcionamiento.
- `presentation`: materiales para la exposición.
- `tests`: pruebas del sistema.
- `scripts`: herramientas auxiliares.
- `resources`: recursos de apoyo.
- `meeting_notes`: acuerdos, decisiones y pendientes del equipo.

## Estado

Estructura inicial creada y primera versión del sistema experto implementada.

## Primera demostración

Con Python 3 instalado, ejecutar desde la raíz del proyecto:

```powershell
python -m scripts.demo_expert_system
```

La documentación de sus reglas está en `docs/sistema_experto.md`.
