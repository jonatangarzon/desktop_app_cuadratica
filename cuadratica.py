from cProfile import label
from tkinter import *
from tkinter import messagebox


# Ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("HOLA MUNDO")

# tamaño de la ventana 
ventana_principal.geometry("900x500")

# color de fondo a la ventana
ventana_principal.config(bg="black")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# ------------------------------------------
# Frame entrada de datos
# ------------------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue", width=900, height=600)
frame_entrada.place(x=0,y=0)

# Agregamos una imagen al frame
escudo = PhotoImage(file="img/hola.png")
lb_escudo = Label(frame_entrada, image=escudo)
lb_escudo.place(x=10, y=20)

# labbel para titulo de app
lb_x= Label(frame_entrada, text="a =")                                                                                                 
lb_x.config(bg="yellow", fg="blue", font=("ARIAL",16))                          
lb_x.place(x=25, y=200)                                                                                                         

lb_y= Label(frame_entrada, text="b =")
lb_y.config(bg="yellow", fg="blue", font=("ARIAL",16)) 
lb_y.place(x=255, y=200)

lb_z= Label(frame_entrada, text="c =")
lb_z.config(bg="yellow", fg="blue", font=("ARIAL",16)) 
lb_z.place(x=555, y=200)



# Entrada para el valor de X
entry_x = Entry(frame_entrada, textvariable=X)
entry_x.config(bg="white", fg="black", font=("ARIAL",16))
entry_x.focus_set()
entry_x.place(x=60, y=200, width=150, height=50)                        

# Entrada para el valor de y
entry_y = Entry(frame_entrada, textvariable=Y)
entry_y.config(bg="white", fg="black", font=("ARIAL",16))
entry_y.focus_set()
entry_y.place(x=300, y=200, width=150, height=50)

# Entrada para el valor de z
entry_z = Entry(frame_entrada, textvariable=Y)
entry_z.config(bg="white", fg="black", font=("ARIAL",16))
entry_z.focus_set()
entry_z.place(x=600, y=200, width=150, height=50)



# bucle principal
ventana_principal.mainloop()  
