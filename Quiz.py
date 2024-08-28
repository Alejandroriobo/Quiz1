import tkinter as tk
from tkinter import messagebox
import clips

# Cargar el archivo CLIPS
def cargar_reglas():
    engine = clips.Environment()
    engine.load("recomendaciones.clp")
    engine.reset()
    return engine

# Función para obtener la recomendación
def obtener_recomendacion():
    preferencia = preferencia_entry.get()
    presupuesto = presupuesto_entry.get()

    # Validar la entrada
    if not preferencia or not presupuesto.isdigit():
        messagebox.showerror("Error", "Por favor, ingrese una preferencia válida y un presupuesto numérico.")
        return

    presupuesto = int(presupuesto)
    engine.assert_string(f"(preferencia {preferencia})")
    engine.assert_string(f"(presupuesto {presupuesto})")

    engine.run()

    # Obtener la recomendación desde los hechos
    recomendacion = "No disponible"
    for fact in engine.facts():
        if fact.template.name == "recomendacion":
            recomendacion = fact[0].destino
            break

    messagebox.showinfo("Recomendación", f"Destino recomendado: {recomendacion}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto de Recomendación de Destinos")

# Crear y colocar widgets
tk.Label(ventana, text="Preferencia (playa, montaña, etc.):").pack()
preferencia_entry = tk.Entry(ventana)
preferencia_entry.pack()

tk.Label(ventana, text="Presupuesto ($):").pack()
presupuesto_entry = tk.Entry(ventana)
presupuesto_entry.pack()

tk.Button(ventana, text="Obtener Recomendación", command=obtener_recomendacion).pack()

# Cargar el motor CLIPS
engine = cargar_reglas()

# Ejecutar la interfaz
ventana.mainloop()
