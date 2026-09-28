# Bloque 1: problemas del caso y atributos ISO/IEC 25010:2023

Atributos: adecuación funcional, eficiencia de desempeño, compatibilidad, capacidad de interacción, fiabilidad, seguridad, mantenibilidad, flexibilidad, seguridad operacional (safety).

| Problema del caso | Atributo afectado | Subcaracterística | Métrica propuesta |
|---|---|---|---|
| Defectos que llegan a producción | Adecuación funcional / Fiabilidad | Corrección funcional / Madurez | Defectos escapados por sprint; tasa de fallo de cambios (DORA) |
| Pruebas solo manuales | Mantenibilidad | Capacidad de ser probado (testeabilidad) | % de cobertura de pruebas automatizadas |
| Despliegues los viernes sin control | Fiabilidad | Disponibilidad / Capacidad de recuperación | Tiempo medio de recuperación (MTTR, DORA) |
| Datos de pacientes (historia clínica, citas) expuestos a cambios sin revisión | Seguridad | Confidencialidad / Integridad | Vulnerabilidades abiertas detectadas por análisis automático |
