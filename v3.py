# importamos las bibliotecas necesarias
import tkinter as tk
from tkinter import ttk, messagebox
# Nota: `csv` y `datetime` no se usan en esta versión simplificada, pero puedes agregarlos si vuelves a incluir el guardado de resultados.

# -------- CONFIGURACIÓN DE COLORES Y FUENTE --------
COLOR_FONDO = "#D3CECE"
COLOR_MENU="#2951D3"
COLOR_TEXTO="#FFFFFF"
FUENTE_TITULO =("Arial",16,"bold")
FUENTE_TEXTO= ("Arial",12)

# -------- VARIABLES GLOBALES (Para almacenar datos del usuario y respuestas) --------
usuario = {"nombre": "", "edad": ""}
respuestas = []  # Almacena las variables de respuesta del test

# -------- INTERFAZ PRINCIPAL --------
root=tk.Tk()
root.title("Software de Detección de Adicciones")
root.geometry("900x700") # Aumentado para mejor visualización
root.config(bg=COLOR_FONDO)

# configuramos el frame del menú lateral
menu_frame=tk.Frame(root,bg=COLOR_MENU,width=200)
menu_frame.pack(side="left", fill="y")

# contenido del frame de la derecha
contenido_frame=tk.Frame(root,bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# -------- CAMBIO DE PÁGINAS (Función corregida) --------
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# ----------- PÁGINAS -----------

# Página de bienvenida 
def pagina_bienvenida():
    tk.Label(contenido_frame, text="🧠 Bienvenido al Test de Detección", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="Este software te ayudará a evaluar tus patrones de conducta relacionados con posibles adicciones.", bg=COLOR_FONDO, font=FUENTE_TEXTO, wraplength=600).pack(pady=10)
    tk.Label(contenido_frame, text="Por favor, regístrate para comenzar el test.", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=20)

# Página de registro 
def pagina_registro():
    tk.Label(contenido_frame, text="🧾 Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)

    tk.Label(contenido_frame, text="Nombre:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
    entry_nombre = tk.Entry(contenido_frame, width=40)
    entry_nombre.pack(pady=5)

    tk.Label(contenido_frame, text="Edad:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
    entry_edad = tk.Entry(contenido_frame, width=40)
    entry_edad.pack(pady=5)

    def guardar_datos():
        nombre = entry_nombre.get().strip()
        edad = entry_edad.get().strip()

        if not nombre or not edad or not edad.isdigit():
            messagebox.showwarning("Error", "Por favor, ingresa un nombre y una edad válida.")
            return

        usuario["nombre"] = nombre
        usuario["edad"] = edad

        messagebox.showinfo("Registro exitoso", f"¡Bienvenido, {nombre}! Puedes iniciar el test.")
        mostrar_pagina("Test")

    ttk.Button(contenido_frame, text="Guardar y Continuar", command=guardar_datos).pack(pady=20)

# Página del test 
def pagina_test():
    if usuario["nombre"] == "":
        messagebox.showwarning("Registro necesario", "Por favor, regístrate antes de iniciar el test.")
        mostrar_pagina("Registro")
        return

    tk.Label(contenido_frame, text=f"⚠️ Test de Adicciones - {usuario['nombre']}", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=10)
    tk.Label(contenido_frame, text="Evalúa tu comportamiento en una escala del 1 (Nunca) al 5 (Siempre):", bg=COLOR_FONDO).pack(pady=5)

    # --- Configuración del Canvas y la Barra de Scroll ---
    canvas = tk.Canvas(contenido_frame, bg=COLOR_FONDO)
    canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(contenido_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    scrollable_frame = tk.Frame(canvas, bg=COLOR_FONDO)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    def on_frame_configure(event):
        # Ajusta la región de scroll para abarcar todo el contenido
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", on_frame_configure)
    
    # Ajustar el ancho del scrollable_frame para que ocupe todo el ancho del canvas
    def on_canvas_configure(event):
        canvas_width = event.width
        canvas.itemconfig(canvas.winfo_children()[0], width=canvas_width)

    canvas.bind('<Configure>', on_canvas_configure)
    
    # Soporte para scroll con la rueda del ratón
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    # --- Preguntas de Opción Múltiple (10 preguntas) ---
    preguntas = [
        "1. ¿Con qué frecuencia sientes la necesidad urgente de realizar una actividad específica (juego, red social, sustancia)?",
        "2. ¿Has intentado reducir o controlar el tiempo que dedicas a esa actividad sin éxito?",
        "3. ¿Tu uso de la actividad/sustancia interfiere con tus responsabilidades (trabajo, estudios, familia)?",
        "4. ¿Buscas esa actividad/sustancia como principal forma de aliviar el estrés o la tristeza?",
        "5. ¿Mientes u ocultas a tus seres queridos la cantidad de tiempo/dinero que dedicas a la actividad?",
        "6. ¿Experimentas síntomas de ansiedad o irritabilidad cuando no puedes acceder a la actividad/sustancia?",
        "7. ¿Has notado que necesitas una dosis o cantidad mayor para obtener el mismo efecto (tolerancia)?",
        "8. ¿Has sacrificado actividades importantes (hobbies, ejercicio, relaciones) por dedicarte a esta actividad?",
        "9. ¿Continuas con la actividad/sustancia a pesar de saber que te está causando problemas físicos o mentales?",
        "10. ¿Crees que has perdido el control sobre la actividad o sustancia, sintiéndote incapaz de parar?"
    ]

    opciones = [
        ("1 (Nunca)", 1), ("2 (Rara vez)", 2), ("3 (A veces)", 3), ("4 (Frecuentemente)", 4), ("5 (Siempre)", 5)
    ]

    respuestas.clear()
    for p_num, p_texto in enumerate(preguntas):
        var = tk.IntVar()
        respuestas.append(var)
        
        pregunta_frame = tk.Frame(scrollable_frame, bg=COLOR_FONDO, padx=10, pady=5)
        pregunta_frame.pack(fill="x", anchor="w")
        
        tk.Label(pregunta_frame, text=p_texto, bg=COLOR_FONDO, font=FUENTE_TEXTO, justify="left", wraplength=600).pack(anchor="w", pady=5)
        
        radio_container = tk.Frame(pregunta_frame, bg=COLOR_FONDO)
        radio_container.pack(pady=5, anchor="w")
        
        for texto, valor in opciones:
            ttk.Radiobutton(radio_container, text=texto, variable=var, value=valor).pack(side="left", padx=10)
    
    # --- Lógica de Resultado (Simple) ---
    def calcular_resultado():
        if any(r.get() == 0 for r in respuestas):
            messagebox.showwarning("Incompleto", "Por favor, responde todas las preguntas antes de ver el resultado.")
            return

        puntaje = sum(r.get() for r in respuestas)
        
        # Puntuación máxima: 50. Rangos: Bajo (10-20), Moderado (21-35), Alto (36-50)
        if puntaje <= 20:
            nivel = "Riesgo Bajo/Control Alto ✅"
            consejo = "Tus respuestas sugieren un alto control sobre tus hábitos. ¡Mantente atento a cualquier cambio!"
        elif puntaje <= 35:
            nivel = "Riesgo Moderado/Atención ⚠️"
            consejo = "Existe un riesgo moderado. Revisa las áreas donde marcaste 4 o 5 y considera buscar un balance."
        else:
            nivel = "Riesgo Alto/Se recomienda Asistencia 🚨"
            consejo = "El puntaje indica un riesgo significativo. Es crucial buscar apoyo profesional para evaluar tus patrones de conducta."

        messagebox.showinfo("Resultado del Test", f"Puntaje Total: {puntaje}/50\nNivel de Riesgo: {nivel}\n\nRecomendación: {consejo}")
        
    ttk.Button(scrollable_frame, text="Ver Resultado", command=calcular_resultado).pack(pady=30)

# ----------- DICCIONARIO DE PÁGINAS -----------
paginas={
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
}

# ----------- BOTONES DE MENÚ LATERAL -----------
for nombre in paginas:
    style = ttk.Style()
    style.configure("TButton", font=FUENTE_TEXTO, background=COLOR_MENU, foreground=COLOR_MENU)
    
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

# mandamos a llamar a la ventana
mostrar_pagina("Bienvenida")
root.mainloop()