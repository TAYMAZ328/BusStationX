import customtkinter as ctk
from core import Station
from .massage import Topask, Topwindow

class Topticket(ctk.CTkToplevel):
    def __init__(self, trip, ui):
        super().__init__()
        self.geometry("480x600")
        self.title("Trip")
        self.attributes('-topmost', True)
        self.grab_set()
        self.seats = 0
        self.station = Station()

        tab = ctk.CTkTabview(self, width=100)
        tab.pack()
        tab.add("Passenger Info")
        tab.add("Seat Number")

        for i in self.station.load("trips"):
            if i.trid == trip:
                self.trid = i.trid
                self.org = i.origin
                self.des = i.des
                self.date = i.date
                self.time = i.tm
                self.driver = i.driver
                break
        for j in self.station.load("drivers"):
            if j.id == self.driver:
                for k in Station().load("bus"):
                    if k.plate == j.bus:
                        self.seats = int(k.seats)
                        self.vip = k.is_vip
                        
        l1 = ctk.CTkLabel(tab.tab("Passenger Info"), text="Ticket Reservation", font=ctk.CTkFont(size=30, weight='bold'))
        lid = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"Ticket ID:   {self.trid}", font=ctk.CTkFont(size=20, weight='bold'))
        lor = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"From:   {{{self.org}}}", font=ctk.CTkFont(size=20, weight='bold'))
        ldes = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"To:   {{{self.des}}}", font=ctk.CTkFont(size=20, weight='bold'))
        ldate = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"On:   {self.date}", font=ctk.CTkFont(size=20, weight='bold'))
        ltm = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"At:   {self.time}", font=ctk.CTkFont(size=20, weight='bold'))
        ldr = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"Driver ID: {self.driver}", font=ctk.CTkFont(size=20, weight='bold'))
        lbus = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"Bus {'is' if self.vip == 'True' else 'is Not'} VIP", font=ctk.CTkFont(size=20, weight='bold'))
        luser = ctk.CTkLabel(tab.tab("Passenger Info"), text=f"Passenger:", font=ctk.CTkFont(size=20, weight='bold'))
        self.user_ent = ctk.CTkEntry(tab.tab("Passenger Info"), placeholder_text="Passenger ID", height=40, font=ctk.CTkFont(size=15))

        add_btn = ctk.CTkButton(tab.tab("Passenger Info"), text="Reserve", command=lambda: self.add(ui), text_color='black', fg_color='green')
        cnl_btn = ctk.CTkButton(tab.tab("Passenger Info"), text="Cancel", command=lambda a=self: a.destroy(), text_color='black', fg_color='yellow', hover_color='red')

        l2 = ctk.CTkLabel(tab.tab("Seat Number"), text="Choose your Seat", font=ctk.CTkFont(size=25, weight='bold'))

        l1.grid(row=0, column=0, pady=10, columnspan=2, sticky='ew')
        lid.grid(row=1, column=0, padx=10, pady=20, sticky='w')
        lor.grid(row=2, column=0, padx=10, pady=20, sticky='w')
        ldes.grid(row=2, column=1, pady=10, sticky='w')
        ldate.grid(row=3, column=0, padx=20, pady=20, sticky='w')
        ltm.grid(row=3, column=1, pady=20, sticky='w')
        ldr.grid(row=4, column=0, padx=10, pady=20, sticky='w')
        lbus.grid(row=4, column=1, pady=20, sticky='w')
        luser.grid(row=5, column=0, padx=10, pady=20, sticky='w')
        self.user_ent.grid(row=5, column=0, padx=(130,0), pady=20, sticky='w')

        cnl_btn.grid(row=6, column=0,padx=20, pady=20,sticky='w')
        add_btn.grid(row=6, column=1, padx=20, pady=20, sticky='w')

        l2.grid(row=0, column=0, padx=10, pady=20, columnspan=4, sticky='ew')

        self.res_seats = [int(t.seatnum) for t in self.station.load("tickets") if trip == t.trid and t.status != 'canceled']

        self.seat = 0
        n = row = 1
        while n < self.seats:
            if self.seats < 26:
                span = 2
                cols = 3
            else:
                cols = 4
                span = 4
            col = 0
            for c in range(cols):
                state = "normal"
                if n in self.res_seats:
                    color = "red"
                    state = "disabled"
                else:
                    color = "green"

                s = ctk.CTkButton(tab.tab("Seat Number"), text=n, fg_color=color, state=state, command=lambda sn=n: self.setseat(sn), width=35, font=ctk.CTkFont(size=15, weight='bold'))
                s.grid(row=row, column=col, padx=10, pady=10)
                n += 1
                col += 1
            row += 1

        self.stn = ctk.CTkLabel(tab.tab("Seat Number"), text=f"Chosen Seat: {self.seat}", font=ctk.CTkFont(size=20, weight='bold'))
        self.stn.grid(padx=40, pady=30, sticky='s', columnspan=span)

    def setseat(self, sn):
        self.stn.configure(text=f"Chosen Seat: {sn}")
        self.seat = sn

    def add(self, ui):
        try:
            id = Station().add_ticket(self.trid, self.org, self.des, self.date, self.time, self.user_ent.get(), self.driver, self.seat)
        except KeyError:
            Topask()
        except Exception as e:
            Topwindow(geo="400x100", label=e, title="Error", color='red')
        else:
            Topwindow(win=self, ui=ui, ref="ticket_btn()", label=f"Successfully Reserved✔️\nTicket ID: {id}")

class Topticketcnl(ctk.CTkToplevel):
    def __init__(self, ticket, ui, geo="400x100", label=None, color='red'):
        super().__init__()
        self.geometry(geo)
        self.title("Alert")
        self.attributes('-topmost', True)
        self.lift()
        self.focus_force()
        self.grab_set()
        lb = ctk.CTkLabel(self, text="Are you sure you want to Cancel this Ticket?", text_color=color, font=ctk.CTkFont(size=20))
        nobtn = ctk.CTkButton(self, text="No", fg_color='red', command=lambda: self.destroy())
        yesbtn = ctk.CTkButton(self, text="Yes", fg_color='green', command=lambda: self.yes(ticket,ui))

        lb.pack(pady=10)
        nobtn.pack(padx=10, pady=10, side="left")
        yesbtn.pack(padx=20, pady=10, side='right')

    def yes(self,ticket,ui):
        self.destroy()
        Station().cancel_ticket(ticket)
        ui.ticket_btn()
