import tkinter as tk
import psutil

class BandwidthMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bandwidth Monitor")

        self.label = tk.Label(root, text="Ancho de banda actual (en bytes/s):")
        self.label.pack(pady=10)

        self.bandwidth_label = tk.Label(root, text="")
        self.bandwidth_label.pack()

        self.update_bandwidth()

    def update_bandwidth(self):
        network_stats = psutil.net_io_counters()
        received_bytes = network_stats.bytes_recv
        sent_bytes = network_stats.bytes_sent
        total_bandwidth = received_bytes + sent_bytes
        bandwidth_text = f"Total: {total_bandwidth} B/s\nRecibidos: {received_bytes} B/s\nEnviados: {sent_bytes} B/s"
        self.bandwidth_label.config(text=bandwidth_text)

        self.root.after(1000, self.update_bandwidth)  # Actualizar cada segundo (1000 ms)

if __name__ == "__main__":
    root = tk.Tk()
    app = BandwidthMonitorApp(root)
    root.mainloop()