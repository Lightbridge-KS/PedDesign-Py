import customtkinter

class MyOptionMenu(customtkinter.CTkFrame):
    def __init__(self, master, values=["option 1", "option 2"], label_text="Options:"):
        super().__init__(master)

        ## Label
        self.optionmenu_label = customtkinter.CTkLabel(self, text=label_text, font=customtkinter.CTkFont(size=15, weight="bold"), anchor="w")
        self.optionmenu_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="e")
        
        ## Drop down
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=values)
        self.optionmenu.grid(row=0, column=1, padx=5, pady=(10, 10), sticky="w")
        
    def set(self, value):
        self.optionmenu.set(value)

    def get(self):
        return self.optionmenu.get()


class MyEntry(customtkinter.CTkFrame):
    def __init__(self, master, placeholder_text="CTkEntry", label_text="Entry:"):
        super().__init__(master)

        ## Label
        self.entry_label = customtkinter.CTkLabel(self, text=label_text, font=customtkinter.CTkFont(size=15, weight="bold"), anchor="w")
        self.entry_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="e")
        
        ## Entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text=placeholder_text)
        self.entry.grid(row=0, column=1, padx=5, pady=(10, 10), sticky="w")

    def get(self):
        return self.entry.get()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.minsize(150, 200)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        # My Option Menu
        self.my_optionmenu = MyOptionMenu(self, values=["A", "B"])
        self.my_optionmenu.set("A")
        self.my_optionmenu.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w", columnspan=2)
        self.my_optionmenu.configure(fg_color="transparent")
        # My Entry
        self.my_entry = MyEntry(self, placeholder_text="Hello")
        self.my_entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w", columnspan=2)
        self.my_entry.configure(fg_color="transparent")


        # Button
        self.button = customtkinter.CTkButton(master=self, text="CTkButton", command=self.button_event)
        self.button.grid(row=2, column=0, padx=5, pady=(10, 0), sticky="ew", columnspan=2)


    def button_event(self):
        print("optionmenu dropdown clicked:", self.my_optionmenu.get())
        print("Entry:", self.my_entry.get())

app = App()
app.mainloop()



