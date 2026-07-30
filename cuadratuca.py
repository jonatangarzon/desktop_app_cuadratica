import cmath
import tkinter
from tkinter import messagebox


# --- Funciones de la app ---
def salir():
    messagebox.showinfo("Cuadrática 1.0", "Hiciste clic en el botón de cerrar")
    ventana_principal.destroy()


def borrar():
    messagebox.showinfo(
        "Cuadrática 1.0", "Los dígitos ingresados serán borrados :D"
    )
    a.set("")
    b.set("")
    c.set("")
    t_result.delete("1.0", "end")


def resolver():
    try:
        va = float(a.get())
        vb = float(b.get())
        vc = float(c.get())
    except ValueError:
        messagebox.showinfo("Cuadrática 1.0", "Por favor ingresa números válidos en A, B y C")
        return

    if va == 0:
        messagebox.showinfo("Cuadrática 1.0","El valor de A no puede ser 0 (no sería una ecuación cuadrática)",)
        return

    discriminante = (vb**2) - (4 * va * vc)

    t_result.insert(tkinter.END, f"Ecuación: {va}x² + {vb}x + {vc} = 0\n")
    t_result.insert(tkinter.END, f"Discriminante = {discriminante}\n")

    if discriminante > 0:
        raiz1 = (-vb + discriminante**0.5) / (2 * va)
        raiz2 = (-vb - discriminante**0.5) / (2 * va)
        t_result.insert(tkinter.END, "Dos raíces reales distintas:\n")
        t_result.insert(tkinter.END, f"x1 = {raiz1}\n")
        t_result.insert(tkinter.END, f"x2 = {raiz2}\n\n")

    elif discriminante == 0:
        raiz = -vb / (2 * va)
        t_result.insert(tkinter.END, "Una raíz real (doble):\n")
        t_result.insert(tkinter.END, f"x = {raiz}\n\n")

    else:
        raiz1 = (-vb + cmath.sqrt(discriminante)) / (2 * va)
        raiz2 = (-vb - cmath.sqrt(discriminante)) / (2 * va)
        t_result.insert(tkinter.END, "Dos raíces complejas:\n")
        t_result.insert(tkinter.END, f"x1 = {raiz1}\n")
        t_result.insert(tkinter.END, f"x2 = {raiz2}\n\n")


# --- Ventana principal ---
ventana_principal = tkinter.Tk()
ventana_principal.title("Ecuación Cuadrática - Dark Mode")
ventana_principal.geometry("500x500")
ventana_principal.config(bg="#121212")  # Fondo general súper oscuro
ventana_principal.resizable(0, 0)

# Variables de coeficientes
a = tkinter.StringVar()
b = tkinter.StringVar()
c = tkinter.StringVar()

# -------------------
# Frame de entrada (Superior)
# -------------------
frame_input = tkinter.Frame(ventana_principal, bg="#1e1e1e", width=480, height=180)
frame_input.place(x=10, y=10)

# Título
titulo = tkinter.Label(
    frame_input,
    text="Ecuación Cuadrática",bg="#1e1e1e",fg="#00e676",  # Verdecito estilo consolafont=("Arial", 16, "bold"),
)
titulo.place(x=140, y=10)

# Estilos de etiquetas e inputs
lbl_bg = "#2d2d2d"
lbl_fg = "#ffffff"
entry_bg = "#000000"
entry_fg = "#00e676"  # Texto verde neón al escribir

# Label y Entry para A
a_text = tkinter.Label(
    frame_input, text="A =", bg=lbl_bg, fg=lbl_fg, font=("Arial", 14, "bold")
)
a_text.place(x=120, y=50, width=40, height=30)
entry_a = tkinter.Entry(
    frame_input,
    textvariable=a,bg=entry_bg,fg=entry_fg,insertbackground="white",font=("Consolas", 14),)
entry_a.focus_set()
entry_a.place(x=170, y=50, width=180, height=30)

# Label y Entry para B
b_text = tkinter.Label(
    frame_input, text="B =", bg=lbl_bg, fg=lbl_fg, font=("Arial", 14, "bold")
)
b_text.place(x=120, y=90, width=40, height=30)
entry_b = tkinter.Entry(
    frame_input,
    textvariable=b,bg=entry_bg,fg=entry_fg,insertbackground="white",font=("Consolas", 14),)
entry_b.place(x=170, y=90, width=180, height=30)

# Label y Entry para C
c_text = tkinter.Label(
    frame_input, text="C =", bg=lbl_bg, fg=lbl_fg, font=("Arial", 14, "bold"))
c_text.place(x=120, y=130, width=40, height=30)
entry_c = tkinter.Entry(
    frame_input,
    textvariable=c,bg=entry_bg, fg=entry_fg,insertbackground="white",font=("Consolas", 14),)
entry_c.place(x=170, y=130, width=180, height=30)

# -------------------
# Frame de trabajo (Inferior)
# -------------------
frame_work = tkinter.Frame(ventana_principal, bg="#1e1e1e", width=480, height=280)
frame_work.place(x=10, y=200)

# Botones con estilo oscuro
btn_bg = "#333333"
btn_fg = "#ffffff"
btn_active_bg = "#444444"

bt_resolver = tkinter.Button(
    frame_work,text="Resolver",command=resolver,font=("Arial", 10, "bold"),bg="#008040",  # Botón destacado verdefg="white",activebackground="#00aa55",relief="flat",
    )
bt_resolver.place(x=30, y=15, width=120, height=35)

bt_borrar = tkinter.Button(
    frame_work,text="Borrar",command=borrar,font=("Arial", 10),bg=btn_bg,fg=btn_fg,activebackground=btn_active_bg,relief="flat",)
bt_borrar.place(x=180, y=15, width=120, height=35)

bt_salir = tkinter.Button(
    frame_work,text="Salir",command=salir,font=("Arial", 10),bg="#a00000",  #Botón rojo para salirfg="white",activebackground="#d00000",relief="flat",
)
bt_salir.place(x=330, y=15, width=120, height=35)

# Caja de texto para resultados
t_result = tkinter.Text(
    frame_work,bg="#0d0d0d",fg="#00e676",insertbackground="white",font=("Consolas", 10),relief="solid",bd=1,)
t_result.place(x=15, y=65, width=450, height=200)

# Bucle principal
ventana_principal.mainloop()