# Bloque 5: métricas

## Métricas DORA (datos en `datos/despliegues.csv`, periodo de 28 días)
- Frecuencia de despliegue: 20 despliegues / 28 días ≈ 0,71 por día (≈ 5 por semana) → nivel alto
- Lead time de cambios (mediana, en horas): 20 h (media 24,7 h)
- Tasa de fallo de cambios: 4 fallos / 20 despliegues = 20 %
- Tiempo medio de recuperación (horas): (5 + 3 + 2 + 8) / 4 fallos = 4,5 h

Observación: 3 de los 4 fallos ocurren en despliegues de viernes (ids 3, 8 y 17) y el cuarto (id 13) es un commit del viernes por la noche desplegado el sábado. Esto respalda la política de no desplegar al final de la semana.

## Cuatro métricas por enfoque
| Enfoque | Métrica | Qué atributo ISO 25010 respalda |
|---|---|---|
| Scrum | Defectos escapados por sprint | Adecuación funcional (corrección) |
| Kanban | Tiempo de ciclo (cycle time) por tarjeta | Eficiencia de desempeño del proceso / Fiabilidad de la entrega |
| XP | % de cobertura de pruebas unitarias | Mantenibilidad (testeabilidad) |
| DevOps | Tasa de fallo de cambios y MTTR | Fiabilidad (madurez y capacidad de recuperación) |
