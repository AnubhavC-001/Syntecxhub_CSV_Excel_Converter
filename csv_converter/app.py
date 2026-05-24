import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from converter import convert_csv_to_excel

# Set appearance mode and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CSV to Excel Converter")
        self.geometry("600x450")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Title
        self.title_label = ctk.CTkLabel(self, text="CSV to Excel Converter", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Source File Frame
        self.source_frame = ctk.CTkFrame(self)
        self.source_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.source_frame.grid_columnconfigure(1, weight=1)

        self.source_label = ctk.CTkLabel(self.source_frame, text="Source CSV:")
        self.source_label.grid(row=0, column=0, padx=10, pady=10)

        self.source_entry = ctk.CTkEntry(self.source_frame, placeholder_text="Select a .csv file")
        self.source_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.source_button = ctk.CTkButton(self.source_frame, text="Browse", width=100, command=self.browse_source)
        self.source_button.grid(row=0, column=2, padx=10, pady=10)

        # Destination File Frame
        self.dest_frame = ctk.CTkFrame(self)
        self.dest_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.dest_frame.grid_columnconfigure(1, weight=1)

        self.dest_label = ctk.CTkLabel(self.dest_frame, text="Save As:")
        self.dest_label.grid(row=0, column=0, padx=10, pady=10)

        self.dest_entry = ctk.CTkEntry(self.dest_frame, placeholder_text="Select destination .xlsx file")
        self.dest_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.dest_button = ctk.CTkButton(self.dest_frame, text="Browse", width=100, command=self.browse_dest)
        self.dest_button.grid(row=0, column=2, padx=10, pady=10)

        # Convert Button
        self.convert_button = ctk.CTkButton(self, text="Convert Now", font=ctk.CTkFont(size=16, weight="bold"), height=40, command=self.convert)
        self.convert_button.grid(row=3, column=0, padx=20, pady=20)

        # Status Label
        self.status_label = ctk.CTkLabel(self, text="Ready", text_color="gray")
        self.status_label.grid(row=4, column=0, padx=20, pady=(0, 20))

        # Theme switcher in the corner
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, values=["Dark", "Light", "System"],
                                                               command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="se")

    def browse_source(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if filename:
            self.source_entry.delete(0, "end")
            self.source_entry.insert(0, filename)
            
            # Auto-suggest destination
            if not self.dest_entry.get():
                dest = os.path.splitext(filename)[0] + ".xlsx"
                self.dest_entry.delete(0, "end")
                self.dest_entry.insert(0, dest)

    def browse_dest(self):
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if filename:
            self.dest_entry.delete(0, "end")
            self.dest_entry.insert(0, filename)

    def convert(self):
        csv_path = self.source_entry.get()
        excel_path = self.dest_entry.get()

        if not csv_path or not excel_path:
            messagebox.showwarning("Input Error", "Please select both source and destination paths.")
            return

        self.status_label.configure(text="Converting...", text_color="blue")
        self.update_idletasks()

        try:
            convert_csv_to_excel(csv_path, excel_path)
            self.status_label.configure(text="Conversion Successful!", text_color="green")
            messagebox.showinfo("Success", f"File converted successfully and saved to:\n{excel_path}")
        except Exception as e:
            self.status_label.configure(text="Conversion Failed", text_color="red")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
