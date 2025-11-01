import customtkinter as ctk
from core import Station
from .massage import Topwindow


class Toptrip(ctk.CTkToplevel):
    def __init__(self, ui):
        super().__init__()
        self.geometry("400x400")
        self.title("Trip")
        self.attributes('-topmost', True)
        self.grab_set()
        l1 = ctk.CTkLabel(self, text="Add a Trip", font=ctk.CTkFont(size=25, weight='bold'))
        lor = ctk.CTkLabel(self, text="From", font=ctk.CTkFont(size=20))
        ldes = ctk.CTkLabel(self, text="To", font=ctk.CTkFont(size=20))
        ldate = ctk.CTkLabel(self, text="On", font=ctk.CTkFont(size=20))
        ltm = ctk.CTkLabel(self, text="At", font=ctk.CTkFont(size=20))
        ldr = ctk.CTkLabel(self, text="Driver: ", font=ctk.CTkFont(size=20))
        lpr = ctk.CTkLabel(self, text="Price: ", font=ctk.CTkFont(size=20))

        self.or_ent = ctk.CTkEntry(self, width=100, placeholder_text="Origin")
        self.des_ent = ctk.CTkEntry(self, width=100, placeholder_text="Destination")
        self.date_ent = ctk.CTkEntry(self, width=100, placeholder_text="Date")
        self.tm_ent = ctk.CTkEntry(self, width=100, placeholder_text="Time")
        self.dr_ent = ctk.CTkEntry(self, width=100, placeholder_text="Driver(ID)")
        self.pr_ent = ctk.CTkEntry(self, width=100, placeholder_text="Price")

        add_btn = ctk.CTkButton(self, text="Add", command=lambda: self.add(ui), text_color='black', fg_color='green')
        cnl_btn = ctk.CTkButton(self, text="Cancel", command=lambda a=self: a.destroy(), text_color='black', fg_color='yellow', hover_color='red')

        l1.grid(row=0, column=0, padx=10, pady=20, columnspan=2, sticky='ew')
        lor.grid(row=1, column=0, padx=10, pady=20, sticky='w')
        ldes.grid(row=1, column=1, padx=15, pady=20, sticky='w')
        ldate.grid(row=2, column=0, padx=10, pady=20, sticky='w')
        ltm.grid(row=2, column=1, padx=15, pady=20, sticky='w')
        ldr.grid(row=3, column=0, padx=10, pady=20, sticky='w')
        lpr.grid(row=3, column=1, padx=10, pady=20, sticky='w')
        
        self.or_ent.grid(row=1, column=0, padx=(65,5), pady=20, sticky='w')
        self.des_ent.grid(row=1, column=1, padx=(50,5), pady=20, sticky='w')
        self.date_ent.grid(row=2, column=0, padx=(65,5), pady=20, sticky='w')
        self.tm_ent.grid(row=2, column=1, padx=(50,5), pady=20, sticky='w')
        self.dr_ent.grid(row=3, column=0, padx=(75,5), pady=20, sticky='w')
        self.pr_ent.grid(row=3, column=1, padx=(70,5), pady=20, sticky='w')

        add_btn.grid(row=4, column=1, padx=20, pady=20)
        cnl_btn.grid(row=4, column=0, padx=20, pady=2)

    def add(self, ui):
        try:
            id = Station().add_trip(self.or_ent.get(), self.des_ent.get(), self.date_ent.get(), self.tm_ent.get(), self.pr_ent.get(), self.dr_ent.get())
        except Exception as e:
            Topwindow(geo="400x100", label=e, title="Error", color='red')
        else:
            Topwindow(win=self, ui=ui, ref="trip_btn()", label=f"Added Successfully✔️\nTrip ID: {id}")


class Toptripcnl(ctk.CTkToplevel):
    def __init__(self, trip, ui, geo="410x100", label=None, color='red'):
        super().__init__()
        self.geometry(geo)
        self.title("Alert")
        self.attributes('-topmost', True)
        self.lift()
        self.focus_force()
        self.grab_set()
        lb = ctk.CTkLabel(self, text="Are you sure you want to Cancel this Trip?", text_color=color, font=ctk.CTkFont(size=20))
        nobtn = ctk.CTkButton(self, text="No", fg_color='red', command=lambda: self.destroy())
        yesbtn = ctk.CTkButton(self, text="Yes", fg_color='green', command=lambda: self.yes(trip,ui))

        lb.pack(pady=10)
        nobtn.pack(padx=10, pady=10, side="left")
        yesbtn.pack(padx=20, pady=10, side='right')

    def yes(self, trip, ui):
        self.destroy()
        Station().cancel_trip(trip)
        ui.trip_btn()
