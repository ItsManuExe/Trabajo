from tkinter import *
import math

# Función para manejar el clic en los botones
def click(event):
    # Obtener el texto del botón clicado
    text = event.widget.cget("text")
   
    # Manejar las operaciones según el texto del botón
    if text == "=":
        try:
            expression = screen.get().replace("^", "**")  # Reemplazar ^ con **
            result = str(eval(expression))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "√":
        try:
            number = float(screen.get())
            result = math.sqrt(number)
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "←":
        current_text = screen.get()
        if len(current_text) > 0:
            screen.set(current_text[:-1])
    else:
        screen.set(screen.get() + text)

# Crear la ventana principal de la calculadora
JAOC = Tk()
JAOC.title("Calculadora Basica")
JAOC.config(bg="#ADB6B6")

# Crear un marco (Frame) para organizar los elementos
ourframe = Frame()

ourframe.config(bg="")
ourframe.config(width="400", height="600")
ourframe.config(bd=50)
ourframe.config(relief="ridge")
ourframe.config(cursor="hand2")

# Definir la disposición de los botones y sus propiedades
buttons = [
    ("7", 2, 1, "#9CA7A5"), ("8", 2, 2, "#9CA7A5"), ("9", 2, 3, "#9CA7A5"), ("/", 5, 4, "#676767"),
    ("4", 3, 1, "#9CA7A5"), ("5", 3, 2, "#9CA7A5"), ("6", 3, 3, "#9CA7A5"), ("*", 2, 4, "#676767"),
    ("1", 4, 1, "#9CA7A5"), ("2", 4, 2, "#9CA7A5"), ("3", 4, 3, "#9CA7A5"), ("-", 3, 4, "#676767"),
    ("0", 5, 2, "#9CA7A5"), (".", 5, 3, "#676767"), ("C", 1, 1, "#FF4500"), ("+", 4, 4, "#676767"),
    ("=", 5, 1, "#D0E02A"), ("√", 1, 2, "#676767"), ("^", 1, 3, "#676767"), ("←", 1, 4, "#FF4500")
]

# Crear una variable para almacenar el contenido de la pantalla
screen = StringVar()

# Muestra el contenido de la pantalla
entry = Entry(JAOC, textvar=screen, font="Arial 38", bd=10, insertwidth=1, width=14, justify="right", bg="#D0E02A")
entry.grid(row=0, column=1, columnspan=4)

# Configura los botones y sus eventos de clic
for (text, row, col, color, *span) in buttons:
    button = Button(JAOC, text=text, font="Arial 15", padx=20, pady=20, bg=color, bd=8)
    rowspan = span[0] if span else 1
    columnspan = span[1] if len(span) > 1 else 1
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    button.bind("<Button-1>", click)

# Configura la distribución de filas y columnas
for i in range(1, 5):
    JAOC.grid_rowconfigure(i, weight=1)

for i in range(1, 5):
    JAOC.grid_columnconfigure(i, weight=1)

# Iniciar el bucle principal para mostrar la interfaz
JAOC.mainloop()