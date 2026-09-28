# Definition of Done (6 criterios)

Cada criterio debe ser verificable (sí/no) y estar ligado a un atributo de calidad.

| # | Criterio | Atributo ISO 25010 | Evidencia |
|---|---|---|---|
| 1 | El código cumple los criterios de aceptación de la historia de usuario | Adecuación funcional | Historia aprobada por el Product Owner en el tablero |
| 2 | Existen pruebas unitarias automatizadas y todas pasan | Fiabilidad | Ejecución en verde en GitHub Actions |
| 3 | La cobertura de pruebas es mayor o igual al 80 % | Mantenibilidad (testeabilidad) | Reporte de `pytest --cov` en el workflow |
| 4 | El código fue revisado por otro integrante (pull request aprobado) | Mantenibilidad (analizabilidad) | Pull request con al menos 1 aprobación |
| 5 | El código cumple las 5 reglas de codificación del equipo | Mantenibilidad (modificabilidad) | Checklist de revisión en el pull request |
| 6 | No se exponen datos sensibles de pacientes (sin claves ni datos reales en el código) | Seguridad (confidencialidad) | Revisión del pull request y alertas de seguridad de GitHub sin hallazgos |
