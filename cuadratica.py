import tkinter
from tkinter import messagebox
import cmath

#funcion de app
def salir():
    messagebox.showinfo("Cuadratica 1.0", "hiciste click en el boton de cerrar")
    ventana_principal.destroy()

def borrar():
    messagebox.showinfo("Cuadratica 1.0", "Los digitos ingresados seran borrados :D")
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
        messagebox.showinfo("Cuadratica 1.0", "Por favor ingresa numeros validos en A, B y C")
        return

    if va == 0:
        messagebox.showinfo("Cuadratica 1.0", "El valor de A no puede ser 0 (no seria una ecuacion cuadratica)")
        return

    discriminante = (vb ** 2) - (4 * va * vc)

    t_result.insert(tkinter.INSERT, "Ecuacion: " + str(va) + "x^2 + " + str(vb) + "x + " + str(vc) + " = 0\n")
    t_result.insert(tkinter.INSERT, "Discriminante = " + str(discriminante) + "\n")

    if discriminante > 0:
        raiz1 = (-vb + discriminante ** 0.5) / (2 * va)
        raiz2 = (-vb - discriminante ** 0.5) / (2 * va)
        t_result.insert(tkinter.INSERT, "Dos raices reales distintas:\n")
        t_result.insert(tkinter.INSERT, "x1 = " + str(raiz1) + "\n")
        t_result.insert(tkinter.INSERT, "x2 = " + str(raiz2) + "\n\n")

    elif discriminante == 0:
        raiz = -vb / (2 * va)
        t_result.insert(tkinter.INSERT, "Una raiz real (doble):\n")
        t_result.insert(tkinter.INSERT, "x = " + str(raiz) + "\n\n")

    else:
        raiz1 = (-vb + cmath.sqrt(discriminante)) / (2 * va)
        raiz2 = (-vb - cmath.sqrt(discriminante)) / (2 * va)
        t_result.insert(tkinter.INSERT, "Dos raices complejas:\n")
        t_result.insert(tkinter.INSERT, "x1 = " + str(raiz1) + "\n")
        t_result.insert(tkinter.INSERT, "x2 = " + str(raiz2) + "\n\n")

#ventana
ventana_principal= tkinter.Tk()

#titulo
ventana_principal.title("Cuadratica Test")

#tamaño
ventana_principal.geometry("500x500")

#color
ventana_principal.config(bg="black")

#tamaño fijo
ventana_principal.resizable(0,0)


#variables de app (coeficientes de la ecuacion ax^2 + bx + c = 0)
a= tkinter.StringVar()
b= tkinter.StringVar()
c= tkinter.StringVar()


#-------------------
#frame de data input
#-------------------
frame_input= tkinter.Frame(ventana_principal)
frame_input.config(bg="gray",width=480,height=240)
frame_input.place(x=10,y=10)

#imagen del frame
escudo= tkinter.PhotoImage(file="img/a.png")
lb_escudo= tkinter.Label(frame_input, image=escudo)
lb_escudo.place(x=10,y=20)

#label app
titulo= tkinter.Label(frame_input, text="Ecuacion Cuadratica")
titulo.config(bg="white", fg="black", font=("Arial", 16))
titulo.place(x=170, y=5)

#label A=
a_text= tkinter.Label(frame_input, text="A=")
a_text.config(bg="black", fg="white", font=("Arial", 16))
a_text.place(x=180, y=40)

# Entrada para el valor de A
entry_a = tkinter.Entry(frame_input, textvariable=a)
entry_a.config(bg="white", fg="black", font=("Times New Roman",16))
entry_a.focus_set()
entry_a.place(x=213, y=40, width=200, height=30)

#label B=
b_text= tkinter.Label(frame_input, text="B=")
b_text.config(bg="black", fg="white", font=("Arial", 16))
b_text.place(x=180, y=75)

# Entrada para el valor de B
entry_b = tkinter.Entry(frame_input, textvariable=b)
entry_b.config(bg="white", fg="black", font=("Times New Roman",16))
entry_b.place(x=213, y=75, width=200, height=30)

#label C=
c_text= tkinter.Label(frame_input, text="C=")
c_text.config(bg="black", fg="white", font=("Arial", 16))
c_text.place(x=180, y=110)

# Entrada para el valor de C
entry_c = tkinter.Entry(frame_input, textvariable=c)
entry_c.config(bg="white", fg="black", font=("Times New Roman",16))
entry_c.place(x=213, y=110, width=200, height=30)

# boton para borrar
bt_borrar = tkinter.Button(frame_input, text="Borrar", command=borrar)
bt_borrar.place(x=213,y =160, width=100, height=30)

# boton para salir
bt_salir = tkinter.Button(frame_input, text="Salir", command=salir)
bt_salir.place(x=335,y =160, width=100, height=30)


#-------------------
#frame de data work
#-------------------
frame_work= tkinter.Frame(ventana_principal)
frame_work.config(bg="white",width=480,height=120)
frame_work.place(x=10,y=260)

# boton para resolver la ecuacion
bt_resolver = tkinter.Button(frame_work, text="Resolver", command=resolver)
bt_resolver.place(x=190,y =45, width=100, height=30)


#--------------------
#frame de data answer
#--------------------
frame_answer= tkinter.Frame(ventana_principal)
frame_answer.config(bg="gray",width=480,height=100)
frame_answer.place(x=10,y=390)

#resultado
t_result= tkinter.Text(frame_answer)
t_result.config(bg="white", fg="black", font=("Arial", 9))
t_result.place(x=10, y=10, width=460, height= 80)

#bucle
ventana_principal.mainloop()