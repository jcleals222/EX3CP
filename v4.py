import tkinter as tk
from tkinter import ttk, messagebox

# -------- CONFIGURACIÓN DE COLORES Y FUENTE --------
COLOR_FONDO = "#F5F5F5"
COLOR_MENU = "#007ACC"
COLOR_TEXTO = "#FFFFFF"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# -------- VARIABLES GLOBALES --------
usuario = {"nombre": "", "edad": "", "correo": ""}
respuestas = []  # para almacenar las respuestas del test

# -------- VENTANA PRINCIPAL --------
root = tk.Tk()
root.title("Bienestar Total")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# -------- FRAME MENÚ LATERAL --------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# -------- FRAME CONTENIDO --------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# -------- FUNCIÓN PARA CAMBIAR DE PÁGINA --------
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# ----------- PÁGINAS -----------

def pagina_bienvenida():
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    tk.Label(contenido_frame, text="🏥 Bienvenido a Bienestar Total", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="Tu espacio de apoyo, información y salud emocional.", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    for widget in contenido_frame.winfo_children():
        widget.destroy()

    tk.Label(contenido_frame, text="🧾 Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)

    tk.Label(contenido_frame, text="Nombre:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
    entry_nombre = tk.Entry(contenido_frame, width=40)
    entry_nombre.pack(pady=5)

    tk.Label(contenido_frame, text="Edad:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
    entry_edad = tk.Entry(contenido_frame, width=40)
    entry_edad.pack(pady=5)

    tk.Label(contenido_frame, text="Correo:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
    entry_correo = tk.Entry(contenido_frame, width=40)
    entry_correo.pack(pady=5)

    def guardar_datos():
        nombre = entry_nombre.get().strip()
        edad = entry_edad.get().strip()
        correo = entry_correo.get().strip()

        if not nombre or not edad or not correo:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")
            return

        usuario["nombre"] = nombre
        usuario["edad"] = edad
        usuario["correo"] = correo

        messagebox.showinfo("Registro exitoso", f"¡Bienvenido, {nombre}!")
        mostrar_pagina("Test")

    ttk.Button(contenido_frame, text="Guardar y continuar", command=guardar_datos).pack(pady=20)

def pagina_test():
    for widget in contenido_frame.winfo_children():
        widget.destroy()

    if usuario["nombre"] == "":
        messagebox.showwarning("Registro necesario", "Por favor, regístrate antes de iniciar el test.")
        mostrar_pagina("Registro")
        return

    tk.Label(contenido_frame, text=f"🧠 Test de Bienestar - {usuario['nombre']}", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Responde del 1 (Nunca) al 5 (Siempre):", bg=COLOR_FONDO).pack(pady=5)

    preguntas = [
        "1️⃣ ¿Te sientes motivado para realizar tus actividades diarias?",
        "2️⃣ ¿Te relacionas de forma positiva con los demás?",
        "3️⃣ ¿Duermes bien y descansas lo suficiente?",
        "4️⃣ ¿Sientes control sobre tus emociones?",
        "5️⃣ ¿Tienes tiempo para ti y para relajarte?"
    ]

    respuestas.clear()
    for p in preguntas:
        tk.Label(contenido_frame, text=p, bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=5)
        var = tk.IntVar()
        respuestas.append(var)
        for i in range(1, 6):
            ttk.Radiobutton(contenido_frame, text=str(i), variable=var, value=i).pack(anchor="w")

    def calcular_resultado():
        if any(r.get() == 0 for r in respuestas):
            messagebox.showwarning("Incompleto", "Por favor, responde todas las preguntas.")
            return

        puntaje = sum(r.get() for r in respuestas)
        if puntaje <= 10:
            nivel = "Bajo bienestar emocional 😔"
            consejo = "Te sugerimos hablar con alguien de confianza o buscar orientación profesional."
        elif puntaje <= 18:
            nivel = "Bienestar medio 😐"
            consejo = "Podrías mejorar tu descanso, tus relaciones o tu autocuidado."
        else:
            nivel = "Alto bienestar emocional 😊"
            consejo = "¡Excelente! Continúa con tus hábitos saludables."

        usuario["resultado"] = nivel
        usuario["consejo"] = consejo

### al parecer aqui 
import csv
from datetime import datetime

# --- Guardar resultados en archivo CSV ---
def guardar_resultado_csv(usuario, puntaje):
    with open("resultados_bienestar.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            usuario["nombre"],
            usuario["edad"],
            usuario["correo"],
            puntaje,
            usuario["resultado"]
        ])

##

        mostrar_pagina("Resultados")

    ttk.Button(contenido_frame, text="Ver resultados", command=calcular_resultado).pack(pady=20)

def pagina_resultados():
    for widget in contenido_frame.winfo_children():
        widget.destroy()

    resultado = usuario.get("resultado", "Sin datos")
    consejo = usuario.get("consejo", "")

    tk.Label(contenido_frame, text="📊 Resultados del Test", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text=f"Resultado: {resultado}", bg=COLOR_FONDO, font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(contenido_frame, text=consejo, wraplength=600, bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_sintomas():
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    tk.Label(contenido_frame, text="⚠️ Síntomas y Señales", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    texto = """Conoce los signos de alerta:
- Cambios de ánimo repentinos
- Aislamiento social
- Insomnio o falta de energía
- Pérdida de interés en actividades"""
    tk.Label(contenido_frame, text=texto, justify="left", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_historias():
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    tk.Label(contenido_frame, text="💬 Historias Inspiradoras", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Lee testimonios de personas que superaron dificultades y encontraron ayuda.", wraplength=600, bg=COLOR_FONDO).pack(pady=10)

def pagina_ayuda():
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    tk.Label(contenido_frame, text="👩‍⚕️ Ayuda de Expertos", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    texto = """📞 Línea de la Vida: 800 911 2000  
💬 Orientación Psicológica UNAM: 55 5025 0855  
🏥 Centros de salud cercanos: Secretaría de Salud local"""
    tk.Label(contenido_frame, text=texto, justify="left", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

# ----------- DICCIONARIO DE PÁGINAS -----------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
    "Resultados": pagina_resultados,
    "Síntomas": pagina_sintomas,
    "Historias": pagina_historias,
    "Ayuda": pagina_ayuda
}

# ----------- BOTONES DE MENÚ LATERAL -----------
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

# ----------- MOSTRAR PÁGINA INICIAL -----------
pagina_bienvenida()

root.mainloop()
