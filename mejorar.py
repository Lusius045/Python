import psutil
import time
import tkinter as tk
from tkinter import scrolledtext
import threading

class TraficoRedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medidor de Tráfico de Red")

        self.text_area = scrolledtext.ScrolledText(root, width=40, height=10)
        self.text_area.pack()

        self.start_button = tk.Button(root, text="Iniciar Medición", command=self.iniciar_medicion)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Detener Medición", command=self.detener_medicion)
        self.stop_button.pack()
       
        self.running = False
        self.thread = None

    def iniciar_medicion(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.medir_trafico_red)
            self.thread.start()

    def detener_medicion(self):
        self.running = False

    def medir_trafico_red(self):
        while self.running:
            net_stats = psutil.net_io_counters(pernic=True)
            self.text_area.delete(1.0, tk.END)
            for interface, stats in net_stats.items():
                text = f"Interface: {interface}\n"
                text += f"Bytes enviados: {stats.bytes_sent}\n"
                text += f"Bytes recibidos: {stats.bytes_recv}\n"
                text += "=" * 30 + "\n"
                self.text_area.insert(tk.END, text)
            self.root.update()
            time.sleep(5) 

def on_cerrar():
    app.detener_medicion()
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TraficoRedApp(root)
    root.protocol("WM_DELETE_WINDOW", on_cerrar)
    root.mainloop()