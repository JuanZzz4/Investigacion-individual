import tkinter as tk
from tkinter import scrolledtext
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Cargar el modelo y los datos necesarios
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

# Funciones para el chatbot
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_index = np.where(res == np.max(res))[0][0]
    category = classes[max_index]
    return category

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i["tag"]==tag:
            result = random.choice(i['responses'])
            break
    return result

def send_message():
    message = entry.get()
    if message:
        entry.delete(0, tk.END)
        response = get_response(predict_class(message), intents)
        chat_history.insert(tk.END, f"You: {message}\nBot: {response}\n\n")
        chat_history.yview(tk.END)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Chatbot GUI")

# Área de historial de chat
chat_history = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entrada de mensaje
entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

# Botón para enviar mensaje
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Configurar el botón "Enter" para enviar el mensaje
root.bind('<Return>', lambda event=None: send_message())

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
