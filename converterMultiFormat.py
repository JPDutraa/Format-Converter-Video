import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
from moviepy.editor import *
import os

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Conversor de Vídeo")
        
        self.selected_files = []

        self.choose_button = tk.Button(self.master, text="Escolher arquivos", command=self.choose_files)
        self.choose_button.pack(pady=10)

        self.output_label = tk.Label(self.master, text="Pasta de saída:")
        self.output_label.pack()

        self.output_entry = tk.Entry(self.master)
        self.output_entry.pack(pady=5)

        self.output_button = tk.Button(self.master, text="Selecionar pasta", command=self.choose_output)
        self.output_button.pack(pady=5)

        self.format_label = tk.Label(self.master, text="Formato de saída:")
        self.format_label.pack()

        self.format_var = tk.StringVar(self.master)
        self.format_var.set("mp4")
        self.format_optionmenu = tk.OptionMenu(self.master, self.format_var, "mp4", "avi", "mkv", "mov")
        self.format_optionmenu.pack(pady=5)

        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(self.master, variable=self.progress_var, maximum=100)
        self.progress.pack(fill=tk.X, padx=5, pady=10)

        self.convert_button = tk.Button(self.master, text="Converter", command=self.convert_videos)
        self.convert_button.pack(pady=5)

    def choose_files(self):
        self.selected_files = filedialog.askopenfilenames(title="Selecione os arquivos de vídeo")
    
    def choose_output(self):
        output_folder = filedialog.askdirectory(title="Selecione a pasta de saída")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, output_folder)

    def convert_videos(self):
        output_folder = self.output_entry.get()
        if not output_folder:
            messagebox.showerror("Erro", "Por favor, selecione uma pasta de saída.")
            return

        if not self.selected_files:
            messagebox.showerror("Erro", "Por favor, selecione pelo menos um arquivo de vídeo.")
            return
        
        output_format = self.format_var.get()
        total_files = len(self.selected_files)

        codec_dict = {
            'mp4': 'libx264',
            'avi': 'mpeg4',
            'mkv': 'libx264',
            'mov': 'libx264',
        }

        codec = codec_dict.get(output_format, 'libx264')

        for index, file in enumerate(self.selected_files):
            input_video = VideoFileClip(file)
            file_name, _ = os.path.splitext(os.path.basename(file))
            output_path = os.path.join(output_folder, f"{file_name}.{output_format}")
            
            input_video.write_videofile(output_path, codec=codec)
            
            progress_percentage = (index + 1) / total_files * 100
            self.progress_var.set(progress_percentage)
            self.master.update()

        messagebox.showinfo("Sucesso", "Conversão concluída.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
