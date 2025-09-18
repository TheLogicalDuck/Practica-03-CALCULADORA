import flet as ft
import math

def main(page: ft.Page):
    page.title = "Claculadoradoradora la exploradora"
    page.bgcolor = ft.Colors.GREEN_500

    #Título
    titulo = ft.Text(
        "Calculadora Bieeen Básica",
        size=20,
        color=ft.Colors.BLACK,
        text_align="center",
        weight="bold"
    )

    #Entradas
    num1 = ft.TextField(
        label="Número 1",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors.RED_100)
    )
    num2 = ft.TextField(
        label="Número 2",
        width=200,
        text_style=ft.TextStyle(color=ft.Colors.AMBER_300)
    )
    resultado = ft.Text(
        value="Resultado: ",
        size=20,
        color=ft.Colors.PINK_100,
        text_align="center"
    )

    #Label informativo meeejorado
    info = ft.Container(
        content=ft.Text(
            "Para el botón porcentaje: el campo de arriba es el número base y el de abajo es el porcentaje",
            size=13,
            color=ft.Colors.PURPLE_100,
            text_align="center",
            italic=True,
            max_lines=2,
            overflow="clip"
        ),
        alignment=ft.alignment.center,
        width=400,
        padding=5
    )

    # Función para mostrar el resultado
    def mostrar_resultado(valor):
        resultado.value = f"Resultado: {valor}"
        page.update()

    # Funciones de operaciones
    def suma(e):
        try:
            res=float(num1.value) + float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")

    def resta(e):
        try:
            res = float(num1.value) - float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Errroooor")
    def multiplicacion(e):
        try:
            res = float(num1.value) * float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
    
    def division(e):
        try:
            if float(num2.value) == 0:
                mostrar_resultado("División inválida (por cero)")
            else:
                res=float(num1.value) / float(num2.value)
                mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
    
    def porcentaje (e):
        try:
            res = (float(num1.value) * float(num2.value)) / 100
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error!11!!1111!!'1")

    def raiz_cuadrada(e):
        try:
            res1 = math.sqrt(float(num1.value))
            res2 = math.sqrt(float(num2.value))
            mostrar_resultado(f"✔{num1.value}={res1:.2f}  ✔{num2.value}={res2:.2f}")
        except:
            mostrar_resultado("Error")

    #Layout general, todo todito centradito
    page.add(
        ft.Column(
            [
                ft.Row([titulo], alignment="center"),
                ft.Row([num1], alignment="center"),
                ft.Row([num2], alignment="center"),
                ft.Row(
                    [
                        ft.ElevatedButton("➕ Sumar", on_click=suma, width=120),
                        ft.ElevatedButton("➖ Restar", on_click=resta, width=120),
                        ft.ElevatedButton("✖ Multiplicar", on_click=multiplicacion, width=120),
                    ],
                    spacing=10,
                    alignment="center"
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("➗ Dividir", on_click=division, width=120),
                        ft.ElevatedButton("🔘 Porcentaje", on_click=porcentaje, width=120),
                        ft.ElevatedButton("✔ Raíz Cuadrada", on_click=raiz_cuadrada, width=120),
                    ],
                    spacing=10,
                    alignment="center"
                ),
                ft.Row([resultado], alignment="center"),
                ft.Row([info], alignment="center"), # Label informativo al final y centrado
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True,
            spacing=15
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)