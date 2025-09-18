📘 Manual Técnico (Markdown)
# Manual Técnico

## 📌 Descripción del proyecto
Calculadora creada en Flet que permite sumar, restar, dividir, multiplicar, sacar raíz cuadrada y sacar porcentajes.

## 🖥️ Tecnologías usadas
- Python 3.12.10
- Flet (0.28.3)

## ⚙️ Requisitos técnicos
- Tener instalado Python 3.12.10 o superior.
- Tener Python en el Path
- Instalar dependencias con pip install flet.

## 📂 Estructura de archivos

<img width="263" height="271" alt="Estructura" src="https://github.com/user-attachments/assets/f23aa72f-025e-49dd-a304-a3d104bd278f" />

## 🧩 Explicación del código
Este increíble código en flet crea una calculadora con una interfaz visual donde puedes realizar operaciones como suma, resta, multiplicación, división, porcentaje y raíz cuadrada.
## 🛠️ Posibles errores y soluciones
División por cero
Error: Intentar dividir por cero.
Solución: Verifica el divisor antes de realizar la operación. Si el divisor es cero, muestra un mensaje de error como "Error: División por cero no permitida."

Entrada no numérica
Error: Ingresar caracteres no numéricos.
Solución: Asegúrate de que solo se ingresen números. Si se detecta un carácter no numérico, muestra un mensaje de error.

Operación no soportada
Error: Intentar realizar una operación no soportada (e.j., un operador no reconocido).
Solución: Valida que el operador ingresado sea uno de los permitidos (suma, resta, multiplicación, división, porcentaje y raíz). Si no es así, muestra un mensaje de error."

Desbordamiento de número
Error: Resultado demasiado grande o pequeño para procesar.
Solución: Verifica si el número es razonable. Si no, muestra un mensaje de error.
Falta de entrada
Error: No ingresar valores para operar.
Solución: Asegurarse de que se ingresen todos los números necesarios para la operación antes de proceder.

## 🚀 Cómo ejecutar
1- Abir main.py en VSC
2- Presionar F5
3- Elegir un interprete de Python
4- Usar python debugger
5- Esperar a que cargue la página web local


👤 Manual de Usuario (Markdown)
# Manual de Usuario

## 🎯 Presentación de la aplicación
La Calculadora Básica permite realizar operaciones de suma, resta, multiplicación y división.

## 🖥️ Requisitos de uso
- Tener instalado Python 3.12+.
- Instalar la librería Flet.

## ▶️ Pasos para ejecutar
1. Descargar o clonar el proyecto desde GitHub.
2. Abrir terminal en la carpeta del proyecto.
3. Ejecutar: flet run src/main.py

## 🔢 Instrucciones de uso
1. Escribir el primer número.
2. Escribir el segundo número.
3. Presionar el botón de la operación deseada.
4. Ver el resultado.

## 📸 Ejemplo
<img width="1266" height="713" alt="calculadora 1" src="https://github.com/user-attachments/assets/59d8d63c-5279-4efc-8191-802e2ae24b80" />
<img width="1266" height="713" alt="calculadora2" src="https://github.com/user-attachments/assets/9e4083a5-acf0-4ae2-95f0-004cd4d86141" />
<img width="1266" height="713" alt="calculadora3" src="https://github.com/user-attachments/assets/51ca3427-411e-42ca-8265-c32d16ff276c" />

![clacludaldoragif](https://github.com/user-attachments/assets/a2d386bb-78cd-440c-b95d-82efdcbfd248)

## ❌ Errores comunes
- División entre cero.
- Entradas inválidas (como letras u operaciones imposibles).
- Resultado demasiado grande o pequeño para procesar.
- Ingresar carácteres no numéricos.

DIAGRAMAS:
<img width="284" height="495" alt="flujo_suma" src="https://github.com/user-attachments/assets/8fe1ecd9-3174-42d1-ba04-cd4bbc919511" />
<img width="249" height="492" alt="flujo_testa" src="https://github.com/user-attachments/assets/d02ab4e1-c9bc-4237-9f1a-d300d7c5d028" />
<img width="302" height="481" alt="flujo_division" src="https://github.com/user-attachments/assets/d45bd7c3-e4a9-40e7-91d8-1fb281d872de" />
