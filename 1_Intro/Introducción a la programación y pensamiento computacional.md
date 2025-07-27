# Introducción a la programación
## ¿Qué es la programación?
La programación es el proceso de diseñar y construir un conjunto de __instrucciones__ que le dicen a una computadora cómo realizar una tarea. Estas instrucciones se escriben en un __lenguaje de programación__, que es un lenguaje formal diseñado para expresar __algoritmos__ y __estructuras de datos__.

### ¿Qué es una instrucción?
Una instrucción es una orden específica que le dice a la computadora qué hacer. Por ejemplo, una instrucción puede ser "sumar dos números" o "mostrar un mensaje en la pantalla". Se puede pensar que las instrucciones son los pasos que la computadora sigue para completar una tarea. Como los humanos seguimos los pasos de una receta para cocinar, las computadoras siguen instrucciones para ejecutar programas.

### ¿Qué es un algoritmo?
Un algoritmo es un conjunto de instrucciones bien definidas y ordenadas que resuelven un problema o realizan una tarea específica. Por ejemplo, un algoritmo para sumar dos números podría ser:
1. Tomar el primer número.
2. Tomar el segundo número.
3. Sumar ambos números.
4. Mostrar el resultado.

Los algoritmos son fundamentales en la programación, ya que proporcionan una guía paso a paso para resolver problemas. Dentro del curso aprenderemos como crear algoritmos y los tipos comunes de algoritmos utilizados en la vida real. [Referencia Simple](https://www.programiz.com/dsa/algorithm) - [Referencia Completa](https://builtin.com/software-engineering-perspectives/algorithm)

### ¿Qué es un lenguaje de programación?
Un lenguaje de programación es un conjunto de reglas y símbolos que permiten a los programadores escribir instrucciones que las computadoras pueden entender. Existen muchos lenguajes de programación, cada uno con sus propias características y usos. Algunos de los lenguajes más populares incluyen Python, Java, C++, JavaScript y Ruby. Cada lenguaje tiene su propia sintaxis, que es la forma en que se estructuran las instrucciones. Más a futuro ahondaremos en los diferentes lenguajes de programación y sus aplicaciones. [Referencia](https://www.codecademy.com/resources/blog/programming-languages)

### ¿Qué es una estructura de datos?
Una estructura de datos es una forma de organizar y almacenar datos en una computadora para que puedan ser utilizados de manera eficiente. Las estructuras de datos permiten a los programadores manejar grandes cantidades de información de manera efectiva.

## ¿Por qué es importante aprender a programar?
Aprender a programar es importante por varias razones:
1. **Resolución de problemas**: La programación enseña a abordar problemas de manera lógica y estructurada, lo que es útil en muchas áreas de la vida.
2. **Creatividad**: Programar permite crear aplicaciones, juegos y sitios web, lo que fomenta la creatividad y la innovación.
3. **Automatización**: Con la programación, puedes automatizar tareas repetitivas, lo que ahorra tiempo y esfuerzo.
4. **Oportunidades profesionales**: La demanda de habilidades de programación está en aumento en el mercado laboral, y aprender a programar puede abrir puertas a diversas carreras en tecnología y más allá.

## ¿Qué es el pensamiento computacional?
El pensamiento computacional es un enfoque para resolver problemas que implica descomponer un problema en partes más pequeñas, identificar patrones, abstraer información y diseñar algoritmos. Es una habilidad fundamental que complementa la programación y se puede aplicar en diversas disciplinas, no solo en la informática.

## ¿Cómo se relacionan la programación y el pensamiento computacional?
La programación y el pensamiento computacional están estrechamente relacionados. El pensamiento computacional proporciona las bases para entender cómo resolver problemas de manera efectiva, mientras que la programación es la herramienta que se utiliza para implementar esas soluciones. Al aprender a programar, también se desarrollan habilidades de pensamiento computacional, como la lógica, la abstracción y la descomposición de problemas. [Referencia](https://www.bbc.co.uk/bitesize/guides/zp92mp3/revision/1)

## Conceptos clave dentro de la programación
- **Condicionales**: Permiten tomar decisiones en función de ciertas condiciones. Por ejemplo, "Si el número es mayor que 10, mostrar 'Mayor que 10'".
- **Bucles**: Permiten repetir un conjunto de instrucciones varias veces. Por ejemplo, "Repetir 5 veces: mostrar 'Hola'".
- **Variables**: Son espacios en la memoria donde se pueden almacenar datos. Por ejemplo, una variable llamada `edad` puede almacenar la edad de una persona.
- **Funciones**: Son bloques de código que realizan una tarea específica y pueden ser reutilizados. Por ejemplo, una función que calcule el área de un círculo dado su radio. Se pueden pensar como pequeñas "subprogramas" dentro de un programa más grande.

### Ejemplo de condicionales
```python
if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### Ejemplo de bucles
```python
for i in range(5):
    print("Hola")
```

### Ejemplo de variables
```python
edad = 25
print("Tu edad es:", edad)
```

### Ejemplo de funciones
```python
def calcular_area_circulo(radio):
    return 3.14 * radio * radio

area = calcular_area_circulo(5)
print("El área del círculo es:", area)
```

## Ejercicios prácticos
1. **Identifica un problema cotidiano**: Piensa en un problema cotidiano que podrías resolver con un algoritmo. Describe el problema y escribe un algoritmo para resolverlo. Ejemplo: "Calcular el Indice de Masa Corporal (IMC) dado el peso y la altura de una persona".
2. **Crea un pseudocódigo**: Escribe un pseudocódigo para un algoritmo que sume dos números y muestre el resultado. El pseudocódigo es una forma de escribir algoritmos en un lenguaje sencillo y comprensible, sin preocuparse por la sintaxis de un lenguaje de programación específico.
3. **Implementa el algoritmo en PSeint**: Utiliza PSeint para implementar el pseudocódigo que has creado en el ejercicio anterior. PSeint es una herramienta que permite escribir y ejecutar pseudocódigo, facilitando la comprensión de los conceptos básicos de programación. [PSeint](https://pseint.sourceforge.net/)

## ¿Cómo crear un algoritmo?
Para crear un algoritmo, sigue estos pasos:
1. **Define el problema**: Comprende claramente qué problema necesitas resolver.
2. **Descompón el problema**: Divide el problema en partes más pequeñas y manejables.
3. **Identifica los pasos**: Escribe los pasos necesarios para resolver cada parte del problema.
4. **Ordena los pasos**: Asegúrate de que los pasos estén en un orden lógico y secuencial.
5. **Revisa y prueba**: Verifica que el algoritmo resuelve el problema y prueba su funcionamiento con diferentes casos.

¿Existirá una forma de crear un algoritmo sin tener que escribirlo? Sí, existen herramientas como diagramas de flujo que permiten visualizar el algoritmo de manera gráfica. Los diagramas de flujo utilizan símbolos para representar diferentes tipos de acciones y decisiones, lo que facilita la comprensión del proceso.

## Diagrama de flujo
Un diagrama de flujo es una representación gráfica de un algoritmo. Utiliza símbolos para mostrar los pasos del algoritmo y las decisiones que se toman en cada etapa. Los diagramas de flujo son útiles para visualizar el flujo de un proceso y entender cómo se relacionan las diferentes partes del algoritmo. [Referencia](https://www.lucidchart.com/pages/es/que-es-un-diagrama-de-flujo)

## Ejercicios de diagramas de flujo
1. **Crea un diagrama de flujo para el algoritmo de suma**: Utiliza un software de diagramas de flujo o dibuja a mano un diagrama que represente el algoritmo para sumar dos números. Asegúrate de incluir los pasos para tomar los números, sumarlos y mostrar el resultado.
2. **Diseña un diagrama de flujo para el cálculo del IMC**: Crea un diagrama de flujo que muestre el proceso para calcular el Índice de Masa Corporal (IMC) a partir del peso y la altura de una persona. Incluye los pasos para tomar los datos, realizar el cálculo y mostrar el resultado.

## Ejercicio de IMC resuelto en Python
```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print("Su Índice de Masa Corporal (IMC) es:", imc)
```

## Conclusión
La programación y el pensamiento computacional son habilidades esenciales en el mundo actual. Aprender a programar no solo te permite crear aplicaciones y resolver problemas, sino que también fomenta el desarrollo de habilidades de pensamiento crítico y lógico. A medida que avances en este curso, explorarás diferentes lenguajes de programación, estructuras de datos y algoritmos, y aprenderás a aplicar el pensamiento computacional en diversas situaciones.

## Recursos adicionales
- [Codecademy](https://www.codecademy.com/): Plataforma interactiva para aprender a programar en varios lenguajes.
- [Khan Academy](https://es.khanacademy.org/computing/computer-science): Ofrece cursos gratuitos de programación y pensamiento computacional.