import tkinter as tk

def agregar_numero(numero):
    entrada.insert(tk.END, str(numero))

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def limpiar():
    entrada.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Calculadora")


entrada = tk.Entry(ventana, width=16, font=("Arial", 24), bd=10, insertwidth=4, bg="lightblue", justify='right')
entrada.grid(row=0, column=0, columnspan=4)


botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]


fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=calcular).grid(row=fila, column=columna)
    elif boton == "C":
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=limpiar).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=lambda num=boton: agregar_numero(num)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

ventana.mainloop()
