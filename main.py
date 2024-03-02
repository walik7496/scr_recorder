# Download ffmpeg.exe!
import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import time
import pyautogui

class ScreenRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Screen Recorder")
        self.master.geometry("300x100")

        self.recording = False
        self.start_time = None
        self.counter = tk.StringVar()
        self.counter.set("00:00:00")

        self.record_button = tk.Button(self.master, text="Record", command=self.start_recording)
        self.record_button.pack()

        self.counter_label = tk.Label(self.master, textvariable=self.counter)
        self.counter_label.pack()

        self.update_timer()

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.record_button.config(state=tk.DISABLED)
            self.start_time = time.time()

            threading.Thread(target=self.record_screen).start()

    def stop_recording(self):
        if self.recording:
            self.recording = False
            self.master.destroy()

    def record_screen(self):
        output_filename = 'output.mp4'
        screen_width, screen_height = pyautogui.size()
        cmd = [
            'ffmpeg', '-y',
            '-f', 'gdigrab', '-framerate', '30', '-video_size', f'{screen_width}x{screen_height}', '-i', 'desktop',
            '-preset', 'ultrafast', output_filename
        ]
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                raise Exception("Recording failed.")

        except Exception as e:
            self.show_recording_error(str(e))
        else:
            self.show_recording_completed()

    def show_recording_error(self, error_message):
        messagebox.showerror("Error", f"Recording failed: {error_message}")
        self.stop_recording()

    def show_recording_completed(self):
        messagebox.showinfo("Info", "Recording completed.")
        self.stop_recording()

    def update_timer(self):
        if self.recording:
            elapsed_time = time.time() - self.start_time
            self.counter.set(self.format_time(elapsed_time))
        self.master.after(1000, self.update_timer)

    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def main():
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
