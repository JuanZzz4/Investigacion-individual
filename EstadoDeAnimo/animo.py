import cv2
import pyttsx3
import dlib
import tkinter as tk
from tkinter import messagebox

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar la velocidad del habla
engine.setProperty('rate', 150)

# Cargar el detector de rostros de dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Asegúrate de tener el archivo

# Variable para almacenar el estado de ánimo anterior
previous_mood = None

def show_advice(mood):
    # Dar un consejo basado en el estado de ánimo
    advice = ""
    if mood == "feliz":
        advice = "¡Te ves feliz! Sigue así."
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
    global previous_mood  # Declarar que estamos usando la variable global

    # Iniciar la captura de video
    cap = cv2.VideoCapture(0)

    while True:
        # Capturar un frame de la cámara
        ret, frame = cap.read()

        # Verificar si el frame se capturó correctamente
        if not ret:
            print("Error al capturar el frame.")
            break

        # Convertir la imagen a escala de grises para la detección facial
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostros en la imagen con dlib
        faces = detector(gray)

        mood = None  # Inicializar mood en None

        for face in faces:
            # Obtener los puntos de referencia faciales (68 puntos)
            landmarks = predictor(gray, face)

            # Extraer la posición del mentón (punto 8) y la boca (puntos 49 y 55)
            chin = landmarks.part(8).y
            mouth_left = landmarks.part(49).y
            mouth_right = landmarks.part(55).y

            # Calcular el rango de la boca
            mouth_range = mouth_right - mouth_left

            # Determinar el estado de ánimo basándose en la posición vertical de la boca
            if chin + mouth_range < frame.shape[0] // 3:
                mood = "feliz"
            elif chin > 2 * frame.shape[0] // 3:
                mood = "triste"
            else:
                mood = "neutro"

        # Mostrar el estado de ánimo detectado en la consola solo si es diferente al anterior
        if mood != previous_mood:
            print(f"Estado de ánimo: {mood}")
            show_advice(mood)
            previous_mood = mood

            # Preguntar si se quiere ingresar otro estado de ánimo
            if not ask_to_retry():
                # Si la respuesta es no, salir del bucle y cerrar la interfaz
                cap.release()
                cv2.destroyAllWindows()
                return

        # Mostrar el frame en una ventana
        cv2.imshow('Camera', frame)

        # Romper el bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura de video y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

# Iniciar la interfaz gráfica
root = tk.Tk()
root.title("Estado de Ánimo")
root.geometry("300x100")

# Etiqueta en la interfaz gráfica
label = tk.Label(root, text="Presiona 'Iniciar' para conocer tu estado de ánimo.")
label.pack()

# Botón para iniciar el programa
start_button = tk.Button(root, text="Iniciar", command=main)
start_button.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
