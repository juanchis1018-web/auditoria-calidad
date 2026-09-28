# Cinco reglas de codificación del equipo

1. Seguir PEP 8: nombres de funciones y variables en `snake_case`, constantes en `MAYUSCULAS`.
2. Toda función pública lleva docstring y anotaciones de tipo (type hints).
3. No se escribe código nuevo sin una prueba que falle primero (TDD); ninguna prueba se comenta ni se borra para "pasar" el CI.
4. Nada de valores mágicos: los porcentajes, tarifas y límites van en constantes con nombre (ej. `PORCENTAJE_COPAGO`).
5. Las entradas inválidas se validan al inicio de la función y lanzan una excepción con mensaje claro (`ValueError`); nunca se devuelven valores silenciosos como `None` o `-1`.
