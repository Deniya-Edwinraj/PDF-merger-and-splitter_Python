import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pdf_operations import merge_pdfs, split_pdf

class PDFMergerSplitter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PDF Merger and Splitter")
        self.root.geometry("400x300")
        self.file_paths = []

        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 10), padding=10)
        self.style.configure("TLabel", font=("Arial", 12))

        self.create_widgets()

    def create_widgets(self):
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=10)

        ttk.Label(header_frame, text="PDF Merger and Splitter", font=("Arial", 16)).pack()

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        merge_button = ttk.Button(button_frame, text="Select PDFs to Merge", command=self.select_files)
        merge_button.grid(row=0, column=0, padx=5, pady=5)

        merge_action_button = ttk.Button(button_frame, text="Merge PDFs", command=self.merge_pdfs)
        merge_action_button.grid(row=0, column=1, padx=5, pady=5)

        split_button = ttk.Button(button_frame, text="Select PDF to Split", command=self.select_split_file)
        split_button.grid(row=1, column=0, padx=5, pady=5)

        split_action_button = ttk.Button(button_frame, text="Split PDF", command=self.split_pdf)
        split_action_button.grid(row=1, column=1, padx=5, pady=5)

        self.result_label = ttk.Label(self.root, text="", font=("Arial", 10))
        self.result_label.pack(pady=10)

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if self.file_paths:
            self.result_label.config(text=f"Selected {len(self.file_paths)} PDFs.")

    def merge_pdfs(self):
        if not self.file_paths:
            messagebox.showwarning("Warning", "Please select PDF files to merge.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            merge_pdfs(self.file_paths, output_path)
            self.result_label.config(text=f"Merged PDFs saved to {output_path}.")

    def select_split_file(self):
        self.split_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.split_file_path:
            self.result_label.config(text=f"Selected PDF to split: {self.split_file_path}")

    def split_pdf(self):
        if not hasattr(self, 'split_file_path'):
            messagebox.showwarning("Warning", "Please select a PDF file to split.")
            return
        page_range = filedialog.askstring("Input", "Enter page range to split (e.g., 1,2,3 or 1-3):")
        if page_range:
            output_folder = filedialog.askdirectory()
            if output_folder:
                split_pdf(self.split_file_path, page_range, output_folder)
                self.result_label.config(text="Split PDFs saved in the selected folder.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PDFMergerSplitter()
    app.run()
