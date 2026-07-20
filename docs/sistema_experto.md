# Sistema experto de EcoSort AI

## Propósito

El sistema experto recibe los hechos generados por la visión artificial y
decide si el prototipo debe clasificar el residuo, repetir la captura o
rechazar la decisión. Su función es impedir que una predicción incierta mueva
la compuerta equivocada.

## Hechos de entrada

- Material predicho: plástico, vidrio u otra clase.
- Confianza del modelo: valor entre 0 y 1.
- Presencia del objeto: verdadero o falso.

## Conclusiones posibles

- Clasificar como plástico.
- Clasificar como vidrio.
- Repetir la captura.
- Rechazar el objeto o enviarlo a revisión manual.

## Base de conocimiento

| Regla | Condición | Conclusión |
|---|---|---|
| R1 | No se detecta un objeto | No mover la compuerta |
| R2 | El material no es plástico ni vidrio | Rechazar el objeto |
| R3 | Confianza menor que 0.60 | Revisión manual |
| R4 | Confianza desde 0.60 y menor que 0.85 | Repetir la captura |
| R5 | Plástico con confianza igual o mayor que 0.85 | Clasificar como plástico |
| R6 | Vidrio con confianza igual o mayor que 0.85 | Clasificar como vidrio |

## Método de inferencia

Se utiliza encadenamiento hacia adelante. El motor comienza con los hechos
observados y evalúa las reglas por prioridad hasta encontrar la primera cuya
condición se cumpla. El resultado conserva el identificador de la regla para
que la decisión sea explicable durante las pruebas y la exposición.

## Ejecución local

Desde la raíz del proyecto:

```powershell
python -m scripts.demo_expert_system
```

Para ejecutar las pruebas:

```powershell
python -m unittest discover -s tests -v
```

