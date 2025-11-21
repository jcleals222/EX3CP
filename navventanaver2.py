# importar las bibliotecas 
import tkinter as tk

# definir las funciones 
def ir_a(pagina_actual, pagina_siguiente):
    pagina_actual.withdraw()
    pagina_siguiente.deiconify()

def regresar(pagina_actual, paginal_anterior):
    pagina_actual.withdraw()
    paginal_anterior.deiconify()    

# ventanas de bienvenida 
ventanabien = tk.Tk()
ventanabien.title("1-VENTANA DE BIENVENIDA")
ventanabien.geometry("600x400")

tk.Label(ventanabien, text=" bienvenido al software de deteccion de adicciones tecnológicas")
tk.Label(ventanabien, text=" aqui colocamos la descripcion de tu software")
btn1= tk.Button(ventanabien, text="Iniciar",command= lambda: ir_a(ventanabien, ventana2))
btn1.pack(pady=30)

#ventana de registro
ventana2= tk.Toplevel(ventanabien)
ventana2.title("2- VENTANA  DE REGISTRO")
ventanabien.geometry("600x400")

tk.Label(ventana2, text="Registro de usuario").pack(pady=20)
tk.Label(ventana2, text="Nombre:").pack()
tk.Entry(ventana2).pack()
tk.Label(ventana2, text="Edad:").pack()
tk.Entry(ventana2).pack()
tk.Label(ventana2, text="E-mail:").pack()
tk.Entry(ventana2).pack()

tk.Button(ventana2, text="Regresar", command= lambda: regresar(ventana2, ventanabien)).pack(side="left", padx=50, pady=40)
tk.Button(ventana2, text="Continuar", command= lambda: ir_a(ventana2, ventana3)).pack(side="right", padx=50, pady=40)

#ventana del test 
ventana3= tk.Toplevel(ventanabien)
ventana3.title("3- VENTANA DE TESTA ADICCIONES")
ventanabien.geometry("600x400")

tk.Label(ventana3,text="esta es la ventana donde se incluira el testa para adicciones").pack(pady=20)
tk.Label(ventana3,text="Responde las siguientes preguntas", wraplength=500).pack(pady=20)

tk.Button(ventana3, text="Regresar", command= lambda: regresar(ventana3, ventana2)).pack(side="left", padx=50, pady=40)
tk.Button(ventana3, text="Continuar", command= lambda: ir_a(ventana3, ventana4)).pack(side="right", padx=50, pady=40)         

# ventana de resultados 
ventana4= tk.Toplevel(ventanabien)
ventana4.title("4- VENTANA DE RESULTADOS")
ventana4.geometry("600x400")
#ventana de sintomas y señales 

# historias inspiradoras 

# ventana de ayuda

# mandar a traer ventanas 
for v in [ventana2, ventana3,ventana4]:
    v.withdraw()
ventanabien.mainloop()