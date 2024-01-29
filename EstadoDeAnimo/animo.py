import pyttsx3
import tkinter as tk
from tkinter import simpledialog, messagebox

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar la velocidad del habla
engine.setProperty('rate', 150)

def show_advice(mood):
    # Dar un consejo basado en el estado de ánimo
    advice = ""
    if mood == "feliz":
        advice = "¡Te sientes feliz! Sigue así."
    elif mood == "triste":
        advice = "¿Hay algo que te preocupa? Recuerda que siempre puedes hablar con alguien."
    else:
        advice = "Estás en un estado neutro. ¿Hay algo en lo que pueda ayudarte?"

    # Pronunciar el consejo a través de la asistente virtual
    engine.say(advice)
    engine.runAndWait()

    # Mostrar mensaje en la interfaz
    messagebox.showinfo("Consejo", advice)

# Función para preguntar si se quiere ingresar otro estado de ánimo
def ask_to_retry():
    answer = messagebox.askyesno("Pregunta", "¿Quieres ingresar otro estado de ánimo?")
    return answer

# Función principal
def main():
    while True:
        # Solicitar al usuario ingresar su estado de ánimo
        mood = simpledialog.askstring("Estado de Ánimo", "Ingresa tu estado de ánimo (feliz, triste, neutro):")

        if mood is None:  # Si el usuario cierra la ventana de entrada
            break

        # Validar que el estado de ánimo ingresado sea válido
        if mood.lower() in ["feliz", "triste", "neutro"]:
            print(f"Estado de ánimo: {mood}")
            show_advice(mood)

            # Preguntar si se quiere ingresar otro estado de ánimo
            if not ask_to_retry():
                break
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un estado de ánimo válido.")

# Iniciar la interfaz gráfica
root = tk.Tk()
root.title("Estado de Ánimo")

# Etiqueta en la interfaz gráfica
label = tk.Label(root, text="Presiona 'Iniciar' para ingresar tu estado de ánimo manualmente.")
label.pack()

# Botón para iniciar el programa
start_button = tk.Button(root, text="Iniciar", command=main)
start_button.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
