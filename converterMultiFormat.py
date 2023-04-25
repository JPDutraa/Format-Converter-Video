import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
from moviepy.editor import *
import os
import webbrowser

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x600")
        self.master.title("Conversor de Vídeo")

        self.selected_files = []

        self.file_listbox = tk.Listbox(self.master, width=40, height=10)
        self.file_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.choose_button = tk.Button(self.master, text="Escolher arquivos", command=self.choose_files)
        self.choose_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.delete_button = tk.Button(self.master, text="Excluir arquivos", command=self.delete_file)
        self.delete_button.grid(row=1, column=0, padx=150, pady=10)

        self.output_label = tk.Label(self.master, text="Pasta de saída:")
        self.output_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.output_entry = tk.Entry(self.master)
        self.output_entry.grid(row=3, column=0, padx=10, columnspan=3, pady=10, sticky="we")

        self.output_button = tk.Button(self.master, text="Selecionar pasta", command=self.choose_output)
        self.output_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.format_label = tk.Label(self.master, text="Formato de saída:")
        self.format_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.format_var = tk.StringVar(self.master)
        self.format_var.set("mp4")
        self.format_optionmenu = tk.OptionMenu(self.master, self.format_var, "mp4", "avi", "mkv", "mov")
        self.format_optionmenu.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.linkedin_link = tk.Label(self.master, text="LinkedIn: João Pedro de A. Dutra", fg="blue", cursor="hand2")
        self.linkedin_link.grid(row=9, column=0, padx=10, pady=10, sticky="w")
        self.linkedin_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.linkedin.com/in/jo%C3%A3o-pedro-de-abreu-dutra-69b0651b3/"))

        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(self.master, variable=self.progress_var, maximum=100)
        self.progress.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        self.convert_button = tk.Button(self.master, text="Converter", command=self.convert_videos, width=20, height=2)
        self.convert_button.grid(row=8, column=0, padx=10, pady=10)

    def choose_files(self):
        self.selected_files = filedialog.askopenfilenames(title="Selecione os arquivos de vídeo")
        self.file_listbox.delete(0, tk.END)
        for file in self.selected_files:
            self.file_listbox.insert(tk.END, os.path.basename(file))

    def delete_file(self):
        selected_index = self.file_listbox.curselection()
        if not selected_index:
            return

        index_to_remove = selected_index[0]
        self.file_listbox.delete(index_to_remove)
        self.selected_files = list(self.selected_files)
        self.selected_files.pop(index_to_remove)

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
