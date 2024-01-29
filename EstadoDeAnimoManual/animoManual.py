import pyttsx3
import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar la velocidad del habla
engine.setProperty('rate', 150)

# Consejos para cada estado de ánimo
consejos_feliz = [
    "¡Te sientes feliz! Sigue así.",
    "La alegría es contagiosa. Disfruta tu día.",
    "Hoy es un buen día para sonreír."
]

consejos_triste = [
    "¿Hay algo que te preocupa? Recuerda que siempre puedes hablar con alguien.",
    "Las cosas mejorarán. Ánimo.",
    "A veces, permitirse sentir tristeza es parte del proceso de curación."
]

consejos_neutro = [
    "Estás en un estado neutro. ¿Hay algo en lo que pueda ayudarte?",
    "El equilibrio es clave. Si necesitas algo, estoy aquí.",
    "A veces, estar en calma es un regalo en sí mismo."
]

consejos_enojado = [
    "Respira hondo. El enojo pasará.",
    "Intenta encontrar una salida positiva para liberar tu enojo.",
    "Es normal sentir enojo, pero trata de no dejar que te controle."
]

consejos_estresado = [
    "Tómate un descanso y relájate.",
    "Prioriza tus tareas y haz una cosa a la vez.",
    "La meditación o ejercicios de respiración pueden ayudar a reducir el estrés."
]
consejos_confianza = [
    "Confía en tus habilidades, has llegado lejos.",
    "Visualiza tus éxitos anteriores para fortalecer tu confianza.",
    "Establece metas alcanzables y celebra tus logros.",
]

consejos_gratitud = [
    "Practica la gratitud diaria, enfócate en las cosas positivas de tu vida.",
    "Expresa tu agradecimiento a las personas que te rodean.",
    "Mantén un diario de gratitud para recordar las cosas buenas.",
]

consejos_culpa = [
    "Aprende de tus errores y busca maneras de mejorar.",
    "Habla abiertamente sobre tus sentimientos de culpa con alguien de confianza.",
    "Haz cosas positivas para compensar tus acciones, cuando sea posible.",
]
def show_advice(mood):
    # Seleccionar un consejo aleatorio para el estado de ánimo
    if mood == "feliz":
        advice = random.choice(consejos_feliz)
    elif mood == "triste":
        advice = random.choice(consejos_triste)
    elif mood == "neutro":
        advice = random.choice(consejos_neutro)
    elif mood == "enojado":
        advice = random.choice(consejos_enojado)
    elif mood == "estresado":
        advice = random.choice(consejos_estresado)
    elif mood == "confianza":
        advice = random.choice(consejos_confianza)
    elif mood == "gratitud":
        advice = random.choice(consejos_gratitud)
    elif mood == "culpa":
        advice = random.choice(consejos_culpa)
    else:
        advice = "No reconozco ese estado de ánimo."

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
        mood = simpledialog.askstring("Estado de Ánimo", "Ingresa tu estado de ánimo (feliz, triste, neutro, enojado, estresado, confianza, gratitud, culpa):")

        if mood is None:  # Si el usuario cierra la ventana de entrada
            break

        # Validar que el estado de ánimo ingresado sea válido
        if mood.lower() in ["feliz", "triste", "neutro", "enojado", "estresado","confianza","gratitud","culpa"]:
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
