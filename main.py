import tkinter as tk
import customtkinter as ctk
import random
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        text_edit = ctk.CTkTextbox(self, height=300, width=400)
        text_edit.pack(expand=True)
        text_edit.delete(1.0, tk.END)
        with open(file="saved.txt", mode="r") as file_input:
            text = file_input.read()
            text_edit.insert(tk.END, text)
        self.title(f"MY NOTEPAD: saved.txt")
        self.after(100, self.lift)



class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.toplevel_window = None
        def generate_password():
            self.password_entry.delete(0, tk.END)
            password = [
                '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
            ]

            password_string = ""
            for _ in range(10):
                password_string += "".join(random.choice(password))
            self.password_entry.insert(0, string=password_string)

        def save():
            website = self.website_entry.get()
            email = self.username_entry.get()
            password = self.password_entry.get()
            if len(website) == 0 or len(password) == 0:
                messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            else:
                is_ok = messagebox.askokcancel(title=website,
                                               message=f"These are the details entered: \nEmail: {email} "
                                                       f"\nPassword: {password} \nIs it ok to save")
                if is_ok:
                    with open(file="saved.txt", mode="a") as data_file:
                        data_file.write(f"{website} | {email} | {password}\n")
                        self.website_entry.delete(0, tk.END)
                        self.password_entry.delete(0, tk.END)

        self.title("Password Manager")
        self.geometry("500x400")
        self.configure(padx=20, pady=20)
        # ----------------- logo ---------------------- #
        self.canvas = tk.Canvas(width=200, height=200, bg="#242423", highlightthickness=0)
        self.logo = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(100,100, image=self.logo)
        self.canvas.pack(expand=True)
        # ----------------- forms -------------------- #
        self.frame = tk.Frame(self, width=500, height=300, bg="#242423")

        # Labels
        self.website_label = ctk.CTkLabel(master=self.frame, text="Website   ")
        self.website_label.grid(row=1,column=0, sticky="w")
        self.user_name_label = ctk.CTkLabel(master=self.frame, text="User Name    ")
        self.user_name_label.grid(row=0, column=0, sticky="w")
        self.password_label = ctk.CTkLabel(master=self.frame, text="Password    ")
        self.password_label.grid(row=2, column=0, sticky="w")

        # entries
        self.website_entry = ctk.CTkEntry(master = self.frame, width=325, border_color="green",
                                          placeholder_text="Website name")
        self.website_entry.grid(row=1, column=1, sticky="e", pady=10, columnspan=2)
        self.username_entry = ctk.CTkEntry(master=self.frame, width=325, border_color="green", placeholder_text="User name/ Email ID")
        self.username_entry.grid(row=0, column=1, sticky="e", pady=10, columnspan=2)
        self.password_entry = ctk.CTkEntry(master=self.frame, width=235, border_color="green",
                                           placeholder_text="Password")
        self.password_entry.grid(row=2, column=1, sticky="e", pady=10)

        # buttons
        self.generate_button = ctk.CTkButton(master = self.frame, text="Generate", width=90, border_width=1,
                                             border_color="white", command=generate_password)
        self.generate_button.grid(row=2, column=2, sticky="e")

        self.add_button = ctk.CTkButton(master=self.frame, text="Add", width=180, border_width=1, border_color="white",
                                   command=save)
        self.add_button.grid(row=3, columns=1, columnspan=3, sticky="w", pady=20)
        self.open_file_button = ctk.CTkButton(master=self.frame, text="Open", width=180, border_width=1,
                                              border_color="white",command=self.open_toplevel)
        self.open_file_button.grid(row=3, column=1, columnspan=3, sticky="e", pady=20)
        self.frame.pack()

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


if __name__ == "__main__":
    app = Window()
    app.mainloop()