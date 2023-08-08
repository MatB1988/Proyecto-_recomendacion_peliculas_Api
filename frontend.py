import tkinter as tk
from tkinter import messagebox
import requests

class MovieInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Información de Películas")
        
        self.label_idioma = tk.Label(root, text="Idioma:")
        self.label_idioma.pack()
        
        self.entry_idioma = tk.Entry(root)
        self.entry_idioma.pack()
        
        self.button_idioma = tk.Button(root, text="Consultar Películas por Idioma", command=self.consultar_idioma)
        self.button_idioma.pack()
        
        self.label_pelicula = tk.Label(root, text="Película:")
        self.label_pelicula.pack()
        
        self.entry_pelicula = tk.Entry(root)
        self.entry_pelicula.pack()
        
        self.button_pelicula = tk.Button(root, text="Consultar Duración de Película", command=self.consultar_duracion)
        self.button_pelicula.pack()
        
    def consultar_idioma(self):
        idioma = self.entry_idioma.get()
        url = f"http://127.0.0.1:8000/peliculas_idioma/{idioma}"
        
        response = requests.get(url)
        message = response.text
        
        messagebox.showinfo("Resultado", message)
        
    def consultar_duracion(self):
        pelicula = self.entry_pelicula.get()
        url = f"http://127.0.0.1:8000/peliculas_duracion/{pelicula}"
        
        response = requests.get(url)
        message = response.text
        
        messagebox.showinfo("Resultado", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieInfoApp(root)
    root.mainloop()
