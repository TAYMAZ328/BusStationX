import customtkinter as ctk
from core import Station
from .massage import Topwindow

class Topuser(ctk.CTkToplevel):
    def __init__(self, ui):
        super().__init__()
        self.geometry("350x400")
        self.title("Passenger")
        self.attributes('-topmost', True)
        self.grab_set()

        self.gender = None

        l1 = ctk.CTkLabel(self, text="Add a User", font=ctk.CTkFont(size=25, weight='bold'))
        self.fn_ent = ctk.CTkEntry(self, width=100, placeholder_text="First Name")
        self.ln_ent = ctk.CTkEntry(self, width=100, placeholder_text="Last Name")
        self.id_ent = ctk.CTkEntry(self, width=100, placeholder_text="ID")
        self.pn_ent = ctk.CTkEntry(self, width=100, placeholder_text="Phone Number")
        self.birth_ent = ctk.CTkEntry(self, width=100, placeholder_text="Birth Date")
        self.swch = ctk.CTkOptionMenu(self, values=['Gender', 'Male', 'Female'], command=lambda choice: self.setgen(choice), width=100)

        add_btn = ctk.CTkButton(self, text="Add", command=lambda: self.add(ui), width=120, text_color='black', fg_color='green')
        cnl_btn = ctk.CTkButton(self, text="Cancel", command=lambda a=self: a.destroy(), width=120, text_color='black', fg_color='yellow', hover_color='red')


        l1.grid(row=0, column=0, padx=10, pady=40, columnspan=3)
        self.fn_ent.grid(row=1, column=0, padx=40, pady=10, sticky='w')
        self.ln_ent.grid(row=1, column=1, padx=(0,40), pady=10, sticky='w')
        self.id_ent.grid(row=2, column=1, pady=10, sticky='w')
        self.pn_ent.grid(row=2, column=0, padx=40, pady=10, sticky='w')
        self.birth_ent.grid(row=3, column=0, padx=40, pady=10, sticky='w')
        self.swch.grid(row=3, column=1, pady=10, sticky='w')

        cnl_btn.grid(row=4, column=0,padx=20, pady=20, sticky='w')
        add_btn.grid(row=4, column=1, pady=20, sticky='w')

    def setgen(self, choice):
        if choice == 'Male':
            self.gender = 'mr'
        elif choice == 'Female':
            self.gender = 'miss'

    def add(self,ui):
        try:
            Station().add_user(self.fn_ent.get(), self.ln_ent.get(), self.id_ent.get(), self.pn_ent.get(), self.birth_ent.get(), self.gender)
        except Exception as e:
            Topwindow(geo="400x100", label=e, title="Error", color='red')
        else:
            Topwindow(win=self, ui=ui, ref="psngr_btn()", label=f"Added Successfully✔️\nPassenger ID: {self.id_ent.get()}")




class Topdeluser(ctk.CTkToplevel):
    def __init__(self, user, ui, geo="500x150", label=None, color='red'):
        super().__init__()
        self.geometry(geo)
        self.title("Alert")
        self.attributes('-topmost', True)
        self.lift()
        self.focus_force()
        self.grab_set()
        lb = ctk.CTkLabel(self, text="Are you sure you want to Delete this Passenger?\nAll related Tickets to this Passenger will be Canclled.", text_color=color, font=ctk.CTkFont(size=20))
        nobtn = ctk.CTkButton(self, text="No", fg_color='red', command=lambda: self.destroy())
        yesbtn = ctk.CTkButton(self, text="Yes", fg_color='green', command=lambda: self.yes(user,ui))

        lb.pack(pady=10)
        nobtn.pack(padx=10, pady=10, side="left")
        yesbtn.pack(padx=20, pady=10, side='right')

    def yes(self, user,ui):
        self.destroy()
        Station().del_user(user)
        ui.psngr_btn()


class Topuseredit(ctk.CTkToplevel):
    def __init__(self, user, ui):
        super().__init__()
        self.geometry("350x400")
        self.title("Passenger")
        self.attributes('-topmost', True)
        self.grab_set()
        self.gender = None

        l1 = ctk.CTkLabel(self, text="Edit a User", font=ctk.CTkFont(size=25, weight='bold'))
        self.fn_ent = ctk.CTkEntry(self, width=100, placeholder_text="First Name")
        self.ln_ent = ctk.CTkEntry(self, width=100, placeholder_text="Last Name")
        self.id_ent = ctk.CTkEntry(self, width=100, placeholder_text="ID")
        self.pn_ent = ctk.CTkEntry(self, width=100, placeholder_text="Phone Number")
        self.birth_ent = ctk.CTkEntry(self, width=100, placeholder_text="Birth Date")
        self.swch = ctk.CTkOptionMenu(self, values=['Gender', 'Male', 'Female'], width=100)

        add_btn = ctk.CTkButton(self, text="Edit", command=lambda: self.add(ui), width=120, text_color='black', fg_color='green')
        cnl_btn = ctk.CTkButton(self, text="Cancel", command=lambda a=self: a.destroy(), width=120, text_color='black', fg_color='yellow', hover_color='red')


        l1.grid(row=0, column=0, padx=10, pady=40, columnspan=3)
        self.fn_ent.grid(row=1, column=0, padx=40, pady=10, sticky='w')
        self.ln_ent.grid(row=1, column=1, padx=(0,40), pady=10, sticky='w')
        self.id_ent.grid(row=2, column=1, pady=10, sticky='w')
        self.pn_ent.grid(row=2, column=0, padx=40, pady=10, sticky='w')
        self.birth_ent.grid(row=3, column=0, padx=40, pady=10, sticky='w')
        self.swch.grid(row=3, column=1, pady=10, sticky='w')

        cnl_btn.grid(row=4, column=0,padx=20, pady=20, sticky='w')
        add_btn.grid(row=4, column=1, pady=20, sticky='w')

        self.insertvals(user)

    def insertvals(self, user):
        for i in Station().load("users"):
            if i.id == user:
                break

        self.fn_ent.delete(0,'end')
        self.ln_ent.delete(0,'end')
        self.id_ent.delete(0,'end')
        self.pn_ent.delete(0,'end')
        self.birth_ent.delete(0,'end')
        
        self.fn_ent.insert(0, i.fname)
        self.ln_ent.insert(0, i.lname)
        self.id_ent.insert(0, i.id)
        self.pn_ent.insert(0, i.number)
        self.birth_ent.insert(0, i.birth)
        val = ctk.StringVar(value= "Male" if i.gender == "mr" else "Female")
        self.swch.configure(variable=val)

    def add(self, ui):
        try:
            Station().edit_user(self.fn_ent.get(), self.ln_ent.get(), self.id_ent.get(), self.pn_ent.get(), self.birth_ent.get(), self.swch.get())
        except Exception as e:
            Topwindow(geo="400x100", label=e, color='red')
        else:
            Topwindow(win=self, ui=ui, ref="psngr_btn()", label=f"Edited Successfully✔️\nPassenger ID: {self.id_ent.get()}")

