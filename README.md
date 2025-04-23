# Sherlock Holmes y las 12 cuotas sin interés

## ¿Cómo correr los programas?

Para correr los programas, desde una powershell (obviamente abierta en la carpeta donde se encuentran los archivos), pueden correr los programas haciendo ./&lt;nombre_programa&gt; &lt;numero_tarjeta&gt;. Por ejemplo, `./programa3.exe 42` corre al programa 3 con el número de tarjeta de crédito 42.

## Parte I

Hay 6 programas en la carpeta "Parte I", de los cuales sólo 1 de los 6 programas es correcto. Para determinar cual, prueben los programas con distintos números de tarjetas de crédito. Registren las pruebas en el archivo `Registro de Pruebas.xlsx`, de la siguiente forma:

- En la columna "Programa", el número de programa que probaron (1 al 6).
- En la columna "Tarjeta", el número de tarjeta de crédito que probaron.
- En la columna "Resultado Obtenido", lo que sea que les haya devuelto el programa.
- En la columna "Resultado Obtenido", si lo que devolvió el programa era lo esperado o no.

Si se animan, vayan tratando de adivinar que está roto de los programas incorrectos.

**NO AVANZAR A LA SIGUIENTE PARTE HASTA NO PONER EN COMÚN JUNTO AL DOCENTE.**

## Parte II

En la carpeta "Parte II", están los 6 programas y un archivo de tests. Ejecutar los tests con los 6 programas. Para probar los distintos programas, tienen que modificar la variable programa al principio del archivo de tests. Lean los errores que tira. ¿Pueden determinar el programa correcto? ¿En qué fallan los incorrectos?

Para instalar pytest, pueden instalarlo con pip:

```pip install --user pytest```

Para correr el archivo de tests, desde la terminal y en la carpeta donde se encuentran los archivos, pueden hacer:

```python -m pytest test_sherlock.py```

**NO AVANZAR A LA SIGUIENTE PARTE HASTA NO PONER EN COMÚN JUNTO AL DOCENTE.**

## Parte III

Ahora aparece un séptimo programa, `programa7.exe`. Este se encuentra junto a los otros programas y el archivo de tests en la carpeta "Parte III". Determinar si es correcto o no.
