import tkinter as tk
from tkinter import ttk
import speedtest

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Test App - Desarrollado por Estudiantes de E.E.S.T N°2")

        self.status_label = tk.Label(root, text="Presiona 'Iniciar' para medir la velocidad de conexión")
        self.status_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Iniciar", command=self.medir_velocidad)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.speed_test = speedtest.Speedtest()

    def medir_velocidad(self):
        self.status_label.config(text="Realizando prueba de velocidad...")
        self.root.update()

        self.speed_test.get_best_server()

        download_speed = self.speed_test.download() / 1024 / 1024  # Convertir a Mbps
        upload_speed = self.speed_test.upload() / 1024 / 1024  # Convertir a Mbps

        result_text = f"Velocidad de descarga: {download_speed:.2f} Mbps\n"
        result_text += f"Velocidad de carga: {upload_speed:.2f} Mbps"

        self.result_label.config(text=result_text)
        self.status_label.config(text="Prueba de velocidad completada")
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()