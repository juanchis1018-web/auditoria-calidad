# Tablero Kanban: políticas por columna

Enlace o captura del tablero: https://trello.com/b/Ry6cVaKG/app-citas-medicas-%F0%9F%A9%BA 
| Columna | Límite WIP | Política de entrada | Política de salida |
|---|---|---|---|
| Por hacer | Sin límite (máx. 10 priorizadas) | La historia tiene criterios de aceptación y prioridad del Product Owner | Un integrante la toma y se asigna |
| En desarrollo | 3 | Hay cupo en la columna y la historia está asignada | Código escrito con pruebas (TDD) que pasan en local |
| En revisión / pruebas | 2 | Existe un pull request abierto | PR aprobado por otro integrante y workflow de CI en verde |
| Listo para desplegar | 3 | Cumple los 6 criterios de la DoD | Despliegue realizado de lunes a jueves (no se despliega los viernes) |
| Hecho | Sin límite | Desplegado y verificado en producción | — |
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/ae466650-1b8a-48a7-8ae8-5d8a15198e7b" />
