import customtkinter as ctk
from core import Station
from .massage import Topwindow


class Topdriver(ctk.CTkToplevel):
    def __init__(self, ui):
        super().__init__()
        self.geometry("350x400")
        self.title("Driver")
        self.attributes('-topmost', True)
        self.grab_set()
        tab = ctk.CTkTabview(self)
        tab.pack()
        tab.add("Driver")
        tab.add("Bus")
        self.gender = None

        l1 = ctk.CTkLabel(tab.tab("Driver"), text="Hire a Driver", font=ctk.CTkFont(size=25, weight='bold'))
        self.fn_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="First Name")
        self.ln_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="Last Name")
        self.id_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="ID")
        self.pn_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="Phone Number")
        self.birth_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="Birth Date")
        self.swch = ctk.CTkOptionMenu(tab.tab("Driver"), values=['Gender', 'Male', 'Female'], command=lambda choice: self.setgen(choice), width=100)
        add_btn = ctk.CTkButton(tab.tab("Driver"), text="Add", command=lambda: self.add(ui), width=120, text_color='black', fg_color='green')
        cnl_btn = ctk.CTkButton(tab.tab("Driver"), text="Cancel", command=lambda a=self: a.destroy(), width=120, text_color='black', fg_color='yellow', hover_color='red')

        l2 = ctk.CTkLabel(tab.tab("Bus"), text="Add a Bus", font=ctk.CTkFont(size=25, weight='bold'))
        self.name_ent = ctk.CTkEntry(tab.tab("Bus"), width=100, placeholder_text="Model Name")
        self.color = ctk.CTkEntry(tab.tab("Bus"), width=100, placeholder_text="Color")
        self.plate = ctk.CTkEntry(tab.tab("Bus"), width=100, placeholder_text="Bus Plate")
        self.seats = ctk.CTkEntry(tab.tab("Bus"), width=60, placeholder_text="Seats")
        self.check = ctk.CTkCheckBox(tab.tab("Bus"), text="Vip", onvalue=True, offvalue=False)

        l1.grid(row=0, column=0, padx=10, pady=40, columnspan=3)
        self.fn_ent.grid(row=1, column=0, padx=40, pady=10, sticky='w')
        self.ln_ent.grid(row=1, column=1, padx=(0,40), pady=10, sticky='w')
        self.id_ent.grid(row=2, column=1, pady=10, sticky='w')
        self.pn_ent.grid(row=2, column=0, padx=40, pady=10, sticky='w')
        self.birth_ent.grid(row=3, column=0, padx=40, pady=10, sticky='w')
        self.swch.grid(row=3, column=1, pady=10, sticky='w')
        cnl_btn.grid(row=4, column=0,padx=20, pady=20, sticky='w')
        add_btn.grid(row=4, column=1, pady=20, sticky='w')

        l2.grid(row=0, column=0, padx=10, pady=40, columnspan=2)
        self.name_ent.grid(row=1, column=0, padx=40, pady=10, sticky='w')
        self.color.grid(row=1, column=1, padx=(0,40), pady=10, sticky='w')
        self.plate.grid(row=2, column=0, padx=40, pady=10, sticky='w')
        self.seats.grid(row=2, column=1, pady=10, sticky='w')
        self.check.grid(row=3, column=0, padx=40, pady=10, sticky='w')

    def setgen(self, choice):
        if choice == 'Male':
            self.gender = 'mr'
        elif choice == 'Female':
            self.gender = 'miss'

    def add(self,ui):
        try:
            Station().add_driver(self.fn_ent.get(), self.ln_ent.get(), self.id_ent.get(), self.pn_ent.get(), self.birth_ent.get(), self.gender, self.plate.get(), self.name_ent.get(), self.color.get(), self.seats.get(), self.check.get())
        except Exception as e:
            Topwindow(geo="400x100", label=e, title="Error", color='red')
        else:
            Topwindow(win=self, ui=ui, ref="driver_btn()", label=f"The Driver is Hired Successfully✔️\nDriver ID: {self.id_ent.get()}")


class Topbus(ctk.CTkToplevel):
    def __init__(self, bus):
        super().__init__()
        self.geometry("350x400")
        self.title("Bus Details")
        self.attributes('-topmost', True)
        for i in Station().load("bus"):
            if i.plate == bus:
                break
        else:
            raise Exception("Bus Not Found")

        l1 = ctk.CTkLabel(self, text=f"Bus Info", font=ctk.CTkFont(size=30))
        ln = ctk.CTkLabel(self, text=f"Model Name: ", font=ctk.CTkFont(size=20))
        lc = ctk.CTkLabel(self, text=f"Color: ", font=ctk.CTkFont(size=20))
        lp = ctk.CTkLabel(self, text=f"plate: ", font=ctk.CTkFont(size=20))
        ls = ctk.CTkLabel(self, text=f"Seats: ", font=ctk.CTkFont(size=20))
        
        lnshow = ctk.CTkLabel(self, text=f" {i.name.upper()}", font=ctk.CTkFont(size=20, weight='bold'))
        lcshow = ctk.CTkLabel(self, text=f" {i.color.capitalize()}", text_color=i.color, font=ctk.CTkFont(size=20, weight='bold'))
        lpshow = ctk.CTkLabel(self, text=f" {i.plate}", text_color="gray50", font=ctk.CTkFont(size=20, weight='bold'))
        lsshow = ctk.CTkLabel(self, text=f" {i.seats}", text_color="gray50", font=ctk.CTkFont(size=20, weight='bold'))
        lvshow = ctk.CTkLabel(self, text=f" {'' if eval(i.is_vip) else 'Not'} Vip", text_color="#203A69" if eval(i.is_vip) else 'red', font=ctk.CTkFont(size=20, weight='bold'))
        
        l1.grid(row=0, column=0, padx=40, pady=30, columnspan=2)
        ln.grid(row=1, column=0, padx=10, pady=10)
        lc.grid(row=2, column=0, pady=10)
        lp.grid(row=3, column=0, pady=10)
        ls.grid(row=4, column=0, pady=10)

        lnshow.grid(row=1, column=1, padx=10, pady=10)
        lcshow.grid(row=2, column=1, pady=10)
        lpshow.grid(row=3, column=1, pady=10)
        lsshow.grid(row=4, column=1, pady=10)
        lvshow.grid(row=5, column=0, padx=20, pady=10)


class Topdeldriver(ctk.CTkToplevel):
    def __init__(self, driver, ui, geo="500x150", label=None, color='red'):
        super().__init__()
        self.geometry(geo)
        self.title("Alert")
        self.attributes('-topmost', True)
        self.lift()
        self.focus_force()
        self.grab_set()
        lb = ctk.CTkLabel(self, text="Are you sure you want to Delete this Driver?\nAll related Trips to this Driver will be Canclled.", text_color=color, font=ctk.CTkFont(size=20))
        nobtn = ctk.CTkButton(self, text="No", fg_color='red', command=lambda: self.destroy())
        yesbtn = ctk.CTkButton(self, text="Yes", fg_color='green', command=lambda: self.yes(driver,ui))

        lb.pack(pady=10)
        nobtn.pack(padx=10, pady=10, side="left")
        yesbtn.pack(padx=20, pady=10, side='right')

    def yes(self, driver, ui):
        self.destroy()
        Station().del_driver(driver)
        ui.driver_btn()


class Topdriveredit(ctk.CTkToplevel):
    def __init__(self, dr, ui):
        super().__init__()
        self.geometry("350x430")
        self.title("Driver")
        self.attributes('-topmost', True)
        self.grab_set()
        tab = ctk.CTkTabview(self)
        tab.pack()
        tab.add("Driver")
        tab.add("Bus")

        l1 = ctk.CTkLabel(tab.tab("Driver"), text="Edit a Driver", font=ctk.CTkFont(size=25, weight='bold'))
        self.fn_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="First Name")
        self.ln_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="Last Name")
        self.id_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="ID")
        self.pn_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="Phone Number")
        self.birth_ent = ctk.CTkEntry(tab.tab("Driver"), width=100, placeholder_text="Birth Date")
        self.swch = ctk.CTkOptionMenu(tab.tab("Driver"), values=['Gender', 'Male', 'Female'], width=100)
        self.option = ctk.CTkOptionMenu(tab.tab("Driver"), width=100, values=['on_duty', 'in_progress', 'off_duty', 'fired'])
        add_btn = ctk.CTkButton(tab.tab("Driver"), text="Edit", command=lambda: self.add(ui), width=120, text_color='black', fg_color='green')
        cnl_btn = ctk.CTkButton(tab.tab("Driver"), text="Cancel", command=lambda a=self: a.destroy(), width=120, text_color='black', fg_color='yellow', hover_color='red')

        l2 = ctk.CTkLabel(tab.tab("Bus"), text="Edit a Bus", font=ctk.CTkFont(size=25, weight='bold'))
        self.name_ent = ctk.CTkEntry(tab.tab("Bus"), width=100, placeholder_text="Model Name")
        self.color = ctk.CTkEntry(tab.tab("Bus"), width=100, placeholder_text="Color")
        self.plate = ctk.CTkEntry(tab.tab("Bus"), width=100, placeholder_text="Bus Plate")
        self.seats = ctk.CTkEntry(tab.tab("Bus"), width=60, placeholder_text="Seats")
        self.check = ctk.CTkCheckBox(tab.tab("Bus"), text="Vip", onvalue=True, offvalue=False)

        l1.grid(row=0, column=0, padx=10, pady=40, columnspan=3)
        self.fn_ent.grid(row=1, column=0, padx=40, pady=10, sticky='w')
        self.ln_ent.grid(row=1, column=1, padx=(0,40), pady=10, sticky='w')
        self.id_ent.grid(row=2, column=1, pady=10, sticky='w')
        self.pn_ent.grid(row=2, column=0, padx=40, pady=10, sticky='w')
        self.birth_ent.grid(row=3, column=0, padx=40, pady=10, sticky='w')
        self.swch.grid(row=3, column=1, pady=10, sticky='w')
        self.option.grid(row=4, column=0, padx=40, pady=10, sticky='w')
        cnl_btn.grid(row=5, column=0,padx=20, pady=20, sticky='w')
        add_btn.grid(row=5, column=1, pady=20, sticky='w')

        l2.grid(row=0, column=0, padx=10, pady=40, columnspan=2)
        self.name_ent.grid(row=1, column=0, padx=40, pady=10, sticky='w')
        self.color.grid(row=1, column=1, padx=(0,40), pady=10, sticky='w')
        self.plate.grid(row=2, column=0, padx=40, pady=10, sticky='w')
        self.seats.grid(row=2, column=1, pady=10, sticky='w')
        self.check.grid(row=3, column=0, padx=40, pady=10, sticky='w')

        self.insert_vals(dr)

    def insert_vals(self, driver):
        for i in Station().load("drivers"):
            if i.id == driver:
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
        self.gender = ctk.StringVar(value="Male" if i.gender == "mr" else "Female")
        self.swch.configure(variable=self.gender)
        
        self.val = ctk.StringVar(value=i.status)
        self.option.configure(variable=self.val)

        self.name_ent.delete(0,'end')
        self.color.delete(0,'end')
        self.plate.delete(0,'end')
        self.seats.delete(0,'end')
        for j in Station().load("bus"):
            if j.plate == i.bus:
                break
        self.name_ent.insert(0,j.name)
        self.color.insert(0,j.color)
        self.plate.insert(0,j.plate)
        self.seats.insert(0,j.seats)
        if eval(j.is_vip):
            self.check.select()

    def add(self,ui):
        try:
            Station().edit_driver(self.fn_ent.get(), self.ln_ent.get(), self.id_ent.get(), self.pn_ent.get(), self.birth_ent.get(), self.swch.get(), self.plate.get(), self.name_ent.get(), self.color.get(), self.seats.get(), self.check.get(), self.option.get())
        except Exception as e:
            Topwindow(geo="400x100", label=e, color='red')
        else:
            Topwindow(win=self, ui=ui, ref="driver_btn()", label=f"Edited Successfully✔️\nDriver ID: {self.id_ent.get()}")


