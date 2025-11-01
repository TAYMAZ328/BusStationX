import customtkinter as ctk
from jdatetime import datetime as jdt
from generate_report import Pdf
from core import Station
from toplevels import *





class Ui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.switch = "Show All"
        self.radio = "earliest"
        self.station = Station()
        self.sr = self.station.load("trips")

        self.geometry("1300x600")
        self.title("Station")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky='nsew')

        self.mainpage = ctk.CTkFrame(self, corner_radius=20)
        self.mainpage.grid(row=0, column=1, sticky='nsew', pady=15, padx=15)

        labelmain = ctk.CTkLabel(self.mainpage, text="Welcome to\n Bus Station Management", font=ctk.CTkFont(size=50, weight='bold'))
        labelmain.grid(pady=(150))

        label= ctk.CTkLabel(self.sidebar, text= "Dashboard", font=ctk.CTkFont(size=20, weight='bold'))
        label.pack(pady=20, padx=40)


        btn1 = ctk.CTkButton(self.sidebar,text='Trips🛫', command=self.trip_btn, fg_color='gray20', hover_color='gray10' , height=70, font=ctk.CTkFont(size=25))
        btn2 = ctk.CTkButton(self.sidebar,text='Tickets📰', command=self.ticket_btn, fg_color='gray20', hover_color='gray10', height=70,font=ctk.CTkFont(size=25))
        btn3 = ctk.CTkButton(self.sidebar,text='Passengers👤', command=self.psngr_btn, fg_color='gray20', hover_color='gray10', height=70, font=ctk.CTkFont(size=25))
        btn4 = ctk.CTkButton(self.sidebar,text='Drivers👮', command=self.driver_btn, fg_color='gray20', hover_color='gray10', height=70, font=ctk.CTkFont(size=25))
        btn5 = ctk.CTkButton(self.sidebar, text='Contact Developer🔧', command=self.contact, fg_color= "gray25", hover_color='gray10' , font=ctk.CTkFont(size=20))
        self.swt = ctk.CTkSwitch(self.sidebar, text='Light Mode', button_color='gray10', onvalue="Dark", offvalue="Light", command=self.dark_mode,font=ctk.CTkFont(size=15))
        self.swt.select()

        btn1.pack(fill='x', pady=10, padx=10)
        btn2.pack(fill='x', pady=10, padx=10)
        btn3.pack(fill='x', pady=10, padx=10)
        btn4.pack(fill='x', pady=10, padx=10)
        self.swt.pack(side='bottom', pady=20, padx=20)
        btn5.pack(fill='x', side='bottom', pady=10, padx=10)

        self.mainpage.grid_columnconfigure(0, weight=1)


    def trip_searchbox(self, f, ent_info=None):
        id = ctk.CTkEntry(self.mainpage, placeholder_text='ID', width=100, font=ctk.CTkFont(size=13))
        driver = ctk.CTkEntry(self.mainpage, placeholder_text='Driver(ID)',width=100, font=ctk.CTkFont(size=13))
        org = ctk.CTkEntry(self.mainpage, placeholder_text='Origin', font=ctk.CTkFont(size=13))
        des = ctk.CTkEntry(self.mainpage, placeholder_text='Destination', font=ctk.CTkFont(size=13))
        date = ctk.CTkEntry(self.mainpage, placeholder_text='Date', width=100, font=ctk.CTkFont(size=13))
        srbtn = ctk.CTkButton(self.mainpage, text='🔎', width=100, command=lambda: self.srtr(id.get(), org.get(), des.get(), date.get(), driver.get(), self.switch), font=ctk.CTkFont('bold',20))
        date_pre = ctk.CTkButton(self.mainpage, text='<', width=15, height=30, corner_radius=10, font=ctk.CTkFont(size=15))
        date_nxt = ctk.CTkButton(self.mainpage, text='>', width=15, height=30, corner_radius=10, font=ctk.CTkFont(size=15))

        if ent_info:
            for key, value in ent_info.items():
                if value:
                    eval(key).insert(0, value)
        
        if f:
            self.switch = "Show All"
            self.radio = "earliest"
        swchval = ctk.StringVar(value=self.switch)
        swch = ctk.CTkOptionMenu(self.mainpage, values=['Show All','active', 'in_progress','arrived', 'canceled'],variable=swchval, command=lambda choice: self.setval(choice), width=100)

        self.radiovar = ctk.StringVar(value="earliest")
        radio1 = ctk.CTkRadioButton(self.mainpage, text="Earliest", variable=self.radiovar, command=lambda: self.setradio("earliest"))
        radio2 = ctk.CTkRadioButton(self.mainpage, text="Oldest", variable=self.radiovar, command=lambda: self.setradio("oldest"))
        radio3 = ctk.CTkRadioButton(self.mainpage, text="Most Expensive", variable=self.radiovar, command=lambda: self.setradio("ms"))
        radio4 = ctk.CTkRadioButton(self.mainpage, text="Cheapest", variable=self.radiovar, command=lambda: self.setradio("chp"))
        radio5 = ctk.CTkRadioButton(self.mainpage, text="Empty Seats", variable=self.radiovar, command=lambda: self.setradio("es"))
        
        addbtn = ctk.CTkButton(self.mainpage, text='Add +', width=100, command=lambda :Toptrip(self), font=ctk.CTkFont(size=20))

        id.grid(row=0, column=0, sticky='w')
        driver.grid(row=1, column=0, sticky='w', pady=(0,20))
        org.grid(row=0, column=0, sticky='w', padx=105)
        des.grid(row=1, column=0, sticky='w', padx=105, pady=(0,20))
        date.grid(row=0, column=0, sticky='w', padx=250)
        srbtn.grid(row=1, column=0, sticky='w', padx=250, pady=(0,20))
        date_pre.grid(row=0, column=0, padx=353, sticky='w')
        date_nxt.grid(row=0, column=0, padx=385, sticky="w")
        swch.grid(row=1, column=0, sticky='w', padx=360, pady=(0,20))
        radio1.grid(row=0, column=0, sticky='w', padx=(500,0))
        radio2.grid(row=0, column=0, sticky='w', padx=(580,0))
        radio3.grid(row=1, column=0, sticky='w', padx=(500,0))
        radio4.grid(row=1, column=0, sticky='w', padx=(630,0))
        radio5.grid(row=1, column=0, sticky='w', padx=(730,0))
        addbtn.grid(row=0, column=0, sticky='e', pady=(3, 20), padx=20)
        
        swch.configure(variable=swchval)
        radio1.select()
        match self.radio:
            case "oldest":
                radio2.select()
            case "ms":
                radio3.select()
            case "chp":
                radio4.select()
            case "es":
                radio5.select()

    def ticket_searchbox(self, f, ent_info=None):
        id = ctk.CTkEntry(self.mainpage, placeholder_text='ID', width=100)
        trid = ctk.CTkEntry(self.mainpage, placeholder_text='Trip (ID)',width=100)
        org = ctk.CTkEntry(self.mainpage, placeholder_text='Origin')
        des = ctk.CTkEntry(self.mainpage, placeholder_text='Destination')
        date = ctk.CTkEntry(self.mainpage, placeholder_text='Date', width=100)
        seat_num = ctk.CTkEntry(self.mainpage, placeholder_text='Seat Number', width=100)
        usr = ctk.CTkEntry(self.mainpage, placeholder_text='User(ID)', width=100)
        driver = ctk.CTkEntry(self.mainpage, placeholder_text='Driver(ID)',width=100)
        srbtn = ctk.CTkButton(self.mainpage, text='🔎', width=120, command=lambda: self.srt(id.get(), trid.get(), org.get(), des.get(), date.get(), usr.get(), driver.get(), seat_num.get(), self.switch), font=ctk.CTkFont('bold',20))
        date_pre = ctk.CTkButton(self.mainpage, text='<', width=15, height=30, corner_radius=10)
        date_nxt = ctk.CTkButton(self.mainpage, text='>', width=15, height=30, corner_radius=10)
        
        if ent_info:
            for key, value in ent_info.items():
                if value:
                    eval(key).insert(0, value)
        
        if f:
            self.switch = "Show All"
            self.radio = "earliest"

        self.radiovar = ctk.StringVar(value="earliest")
        radio1 = ctk.CTkRadioButton(self.mainpage, text="Earliest", variable=self.radiovar, command=lambda: self.setradio("earliest"))
        radio2 = ctk.CTkRadioButton(self.mainpage, text="Oldest", variable=self.radiovar, command=lambda: self.setradio("oldest"))
        radio3 = ctk.CTkRadioButton(self.mainpage, text="Seat Number", variable=self.radiovar, command=lambda: self.setradio("seat"))

        swchval = ctk.StringVar(value=self.switch)
        swch = ctk.CTkOptionMenu(self.mainpage, values=['Show All','active', 'in_progress', 'arrived', 'canceled'], command=lambda choice: self.setval(choice), width=100)

        id.grid(row=0, column=0, sticky='w')
        trid.grid(row=1, column=0, sticky='w', pady=(0,20))
        org.grid(row=0, column=0, sticky='w', padx=105)
        des.grid(row=1, column=0, sticky='w', padx=105, pady=(0,20))
        seat_num.grid(row=0, column=0, sticky='w', padx=250)
        date.grid(row=0, column=0, sticky='w', padx=355)
        driver.grid(row=1, column=0, sticky='w', padx=250, pady=(0,20))
        usr.grid(row=1, column=0, sticky='w', padx=355, pady=(0,20))
        srbtn.grid(row=1, column=0, sticky='w', padx=(460,0), pady=(3,20))
        date_pre.grid(row=0, column=0, padx=460, sticky='w')
        date_nxt.grid(row=0, column=0, padx=490, sticky="w")
        swch.grid(row=0, column=0, sticky='w', padx=(520,0))
        radio1.grid(row=0, column=0, sticky='e', padx=(0,270))
        radio2.grid(row=0, column=0, sticky='e', padx=(0,170))
        radio3.grid(row=1, column=0, sticky='e', padx=(0,270))

        swch.configure(variable=swchval)
        radio1.select()
        match self.radio:
            case "oldest":
                radio2.select()
            case "seat":
                radio3.select()

    def psngr_searchbox(self, f, ent_info=None):
        id = ctk.CTkEntry(self.mainpage, placeholder_text='ID', width=100)
        name = ctk.CTkEntry(self.mainpage, placeholder_text='Name')
        num = ctk.CTkEntry(self.mainpage, placeholder_text='Number', width=100)
        birth = ctk.CTkEntry(self.mainpage, placeholder_text='Birth Date', width=100)
        jd = ctk.CTkEntry(self.mainpage, placeholder_text='Joined Date', width=100)
        
        if ent_info:
            for key, value in ent_info.items():
                if value:
                    eval(key).insert(0, value)
        
        if f:
            self.radio = "lj"

        self.radiovar = ctk.StringVar(value="lj")
        radio1 = ctk.CTkRadioButton(self.mainpage, text="Latest Join", variable=self.radiovar, command=lambda: self.setradio("lj"))
        radio2 = ctk.CTkRadioButton(self.mainpage, text="Oldest join", variable=self.radiovar, command=lambda: self.setradio("oj"))
        radio3 = ctk.CTkRadioButton(self.mainpage, text="Youngest", variable=self.radiovar, command=lambda: self.setradio("young"))
        radio4 = ctk.CTkRadioButton(self.mainpage, text="Oldest", variable=self.radiovar, command=lambda: self.setradio("old"))

        srbtn = ctk.CTkButton(self.mainpage, text='🔎', command=lambda: self.srp(name.get(), num.get(), id.get(), birth.get(), jd.get()), width=100, font=ctk.CTkFont('bold',20))
        addbtn = ctk.CTkButton(self.mainpage, text='Add +',command=lambda : Topuser(self), width=100, font=ctk.CTkFont(size=20))

        id.grid(row=0, column=0, sticky='w')
        name.grid(row=1, column=0, sticky='w', pady=(0,20))
        num.grid(row=0, column=0, sticky='w', padx=105)
        birth.grid(row=1, column=0, sticky='w', padx=150, pady=(0,20))
        jd.grid(row=0, column=0, sticky='w', padx=210)
        radio1.grid(row=0, column=0, sticky='w', padx=(450,0))
        radio2.grid(row=0, column=0, sticky='w', padx=(570,0))
        radio3.grid(row=1, column=0, sticky='w', padx=(450,0))
        radio4.grid(row=1, column=0, sticky='w', padx=(575,0))
        srbtn.grid(row=1, column=0, sticky='w', padx=260, pady=(0,20))
        addbtn.grid(row=0, column=0, sticky='e', pady=(3, 20), padx=20)

        radio1.select()
        match self.radio:
            case "oj":
                radio2.select()
            case "young":
                radio3.select()
            case "old":
                radio4.select()

    def driver_searchbox(self, f, ent_info=None):
        id = ctk.CTkEntry(self.mainpage, placeholder_text='ID')
        name = ctk.CTkEntry(self.mainpage, placeholder_text='Name')
        num = ctk.CTkEntry(self.mainpage, placeholder_text='Number', width=100)
        plt = ctk.CTkEntry(self.mainpage, placeholder_text='Bus Plate', width=100)
        jd = ctk.CTkEntry(self.mainpage, placeholder_text='Joined Date', width=100)
        birth = ctk.CTkEntry(self.mainpage, placeholder_text='Birth Date', width=100)

        if ent_info:
            for key, value in ent_info.items():
                if value:
                    eval(key).insert(0, value)

        if f:
            self.switch = "Show All"
            self.radio = "lj"

        self.radiovar = ctk.StringVar(value="lj")
        radio1 = ctk.CTkRadioButton(self.mainpage, text="Latest Join", variable=self.radiovar, command=lambda: self.setradio("lj"))
        radio2 = ctk.CTkRadioButton(self.mainpage, text="Oldest join", variable=self.radiovar, command=lambda: self.setradio("oj"))
        radio3 = ctk.CTkRadioButton(self.mainpage, text="Youngest", variable=self.radiovar, command=lambda: self.setradio("young"))
        radio4 = ctk.CTkRadioButton(self.mainpage, text="Oldest", variable=self.radiovar, command=lambda: self.setradio("old"))
        
        swchval = ctk.StringVar(value=self.switch)
        swch = ctk.CTkOptionMenu(self.mainpage, values=['Show All', 'on_duty', 'in_progress', 'off_duty', 'fired'], command=lambda choice: self.setval(choice), width=100)
        srbtn = ctk.CTkButton(self.mainpage, text='🔎',command=lambda: self.srd(name.get(), num.get(), id.get(), plt.get(), birth.get(), self.switch, jd.get()), width=100, font=ctk.CTkFont('bold',20))
        addbtn = ctk.CTkButton(self.mainpage, text='Hire +', command=lambda : Topdriver(self), width=100, font=ctk.CTkFont(size=20))

        id.grid(row=0, column=0, sticky='w')
        name.grid(row=1, column=0, sticky='w', pady=(0,20))
        num.grid(row=0, column=0, sticky='w', padx=145)
        plt.grid(row=1, column=0, sticky='w', padx=145, pady=(0,20))
        jd.grid(row=0, column=0, sticky='w', padx=250)
        birth.grid(row=1, column=0, sticky='w', padx=250, pady=(0,20))
        radio1.grid(row=0, column=0, sticky='w', padx=(550,0))
        radio2.grid(row=0, column=0, sticky='w', padx=(670,0))
        radio3.grid(row=1, column=0, sticky='w', padx=(550,0))
        radio4.grid(row=1, column=0, sticky='w', padx=(675,0))
        swch.grid(row=0, column=0, sticky='w', padx=360)
        srbtn.grid(row=1, column=0, sticky='w', padx=360, pady=(0,20))
        addbtn.grid(row=0, column=0, sticky='e', pady=(3, 20), padx=20)

        swch.configure(variable=swchval)
        radio1.select()
        match self.radio:
            case "oj":
                radio2.select()
            case "young":
                radio3.select()
            case "old":
                radio4.select()


    def trip_btn(self, ent_info=None, arg=None):
        f=True
        if arg:
            lists = arg
            f=False
        else:
            lists = self.station.load("trips")
        self.clear()
        self.trip_searchbox(f, ent_info)

        rev = True
        k = "a.date"
        match self.radio:
            case "oldest":
                rev = False
            case "ms":
                k = "int(a.price)"
            case "chp":
                k = "int(a.price)"
                rev = False
            case "es":
                k = "int(a.seats)-int(a.reserved_seats)"

        lists.sort(key=lambda a: eval(k), reverse=rev)
        for i, trp in enumerate(lists, start=2):
            ticket_frame = ctk.CTkFrame(self.mainpage, fg_color=('gray60', 'gray20'))
            ticket_frame.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

            if (f"{trp.date}/{trp.tm}" <= jdt.now().strftime("%Y/%m/%d/%H:%M")) and trp.status == "active":
                self.station.cancel_trip(trp.trid, "in_progress")
                trp.status = "in_progress"

            l1 = ctk.CTkLabel(ticket_frame, text=f"\t       From   {{{trp.origin.capitalize()}}}   To   {{{trp.des.capitalize()}}}   On   {{{trp.date}}}   At   {{{trp.tm}}}", font=ctk.CTkFont(size=20))
            idbtn = ctk.CTkButton(ticket_frame, text=f" ID: {trp.trid}", width=70, fg_color=('gray60', 'gray20'), command=lambda trip=trp.trid: self.srt(trid=trip), font=ctk.CTkFont(size=18, weight='bold'))
            l2 = ctk.CTkLabel(ticket_frame, text=f"  Empty Seats: <{int(trp.seats)-int(trp.reserved_seats)}>\t\t\t\tPrice: {int(trp.price):,}    Status: {trp.status.capitalize()}", font=ctk.CTkFont(size=20))
            drbtn = ctk.CTkButton(ticket_frame, text=f"Driver ID: {trp.driver}", width=70, fg_color=('gray60', 'gray20'), command=lambda dr=trp.driver: self.srd(id=dr), font=ctk.CTkFont(size=18, weight='bold'))

            l1.grid(row=0, column=0)
            l2.grid(row=1, column=0, sticky='w')
            idbtn.grid(row=0, column=0, sticky='w')
            drbtn.grid(row=1, column=0, sticky='w', padx=(200,0))

            ticket_frame.grid_columnconfigure(1, weight=1)
            rsrv_btn = ctk.CTkButton(ticket_frame, text_color='green', fg_color='gray20', border_color='green', border_width=1, hover_color='green', text="Reserve", command= lambda t=trp.trid: Topticket(t, self), width=100)
            cancel_btn = ctk.CTkButton(ticket_frame, text_color='red', fg_color='gray20', border_color='red', border_width=1, hover_color='yellow', text="Cancel", command=lambda trip=trp.trid: Toptripcnl(trip, self), width=100)

            rsrv_btn.grid(row=0, column=1, padx=10, pady=5, sticky='e')
            cancel_btn.grid(row=0, column=2, padx=10, pady=5, sticky='e')


            if trp.status != 'active':
                cancel_btn.configure(state='disabled')
                rsrv_btn.configure(state='disabled')
            if int(trp.reserved_seats) >= int(trp.seats):
                rsrv_btn.configure(state='disabled')

    def ticket_btn(self, ent_info=None, arg=None):
        f=True
        if arg:
            lists = arg
            f=False
        else:
            lists = self.station.load("tickets")

        self.clear()
        self.ticket_searchbox(f, ent_info)
                
        rev = True
        k = "a.date"
        match self.radio:
            case "oldest":
                rev = False
            case "seat":
                k = "int(a.seatnum)"
                rev = False

        lists.sort(key=lambda a: eval(k), reverse=rev)

        report = ctk.CTkButton(self.mainpage,text="Generate Report🖨", command=lambda: Pdf(lists), font=ctk.CTkFont(size=18))
        report.grid(row=0, column=0, padx=10, sticky='e')
        
        for i, ticket in enumerate(lists, start=2):
            ticket_frame = ctk.CTkFrame(self.mainpage, fg_color=('gray60', 'gray20'))
            ticket_frame.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

            l1 = ctk.CTkLabel(ticket_frame, text=f"\tFrom   {{{ticket.origin.capitalize()}}}   To   {{{ticket.des.capitalize()}}}   On   {{{ticket.date}}}   At   {{{ticket.tm}}}", font=ctk.CTkFont(size=20))
            idbtn = ctk.CTkButton(ticket_frame, text=f" ID: {ticket.tid}", width=70, command=lambda trip=ticket.trid: self.srtr(id=trip), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18, weight='bold'))
            l2 = ctk.CTkLabel(ticket_frame, text=f"Seat: {ticket.seatnum}     Status: {ticket.status.capitalize()}", font=ctk.CTkFont(size=20))
            tridbtn = ctk.CTkButton(ticket_frame, text=f" Trip ID: {ticket.trid}", width=70, command=lambda trip=ticket.trid: self.srt(trid=trip), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18, weight='bold'))
            usbtn = ctk.CTkButton(ticket_frame, text=f"Name: {' '.join(i.capitalize() for i in ticket.name.split())} -> ID: {ticket.user}", width=70, command=lambda usr=ticket.user: self.srp(id=usr), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18, weight='bold'))

            l1.grid(row=0, column=0)
            idbtn.grid(row=0, column=0, sticky='w')
            tridbtn.grid(row=1, column=0, sticky='w')
            l2.grid(row=1, column=0, sticky='w', padx=(600,0))
            usbtn.grid(row=1, column=0, sticky='w', padx=(170,0))

            ticket_frame.grid_columnconfigure(1, weight=1)
            cancel_btn = ctk.CTkButton(ticket_frame, text_color='red', fg_color='gray20', border_color='red', border_width=1, hover_color='yellow', text="Cancel", command=lambda tckt=ticket.tid: Topticketcnl(tckt,self), width=100)
            cancel_btn.grid(row=0, column=1, padx=10, pady=5, sticky='e')

            if ticket.status != 'active':
                cancel_btn.configure(state='disabled')

    def psngr_btn(self, ent_info=None, arg=None):
        f=True
        if arg:
            lists = arg
            f=False
        else:
            lists = self.station.load("users")

        self.clear()
        self.psngr_searchbox(f, ent_info)

        rev = True
        k = "a.joined"
        match self.radio:
            case "oj":
                rev = False
            case "young":
                k = "a.birth"
            case "old":
                k = "a.birth"
                rev = False


        lists.sort(key=lambda a: eval(k), reverse=rev)
        for i, psngr in enumerate(lists, start=2):
            ticket_frame = ctk.CTkFrame(self.mainpage, fg_color=('gray60', 'gray20'))
            ticket_frame.grid(row=i, column=0, pady=5, padx=5, sticky="ew")

            l1 = ctk.CTkLabel(ticket_frame, text=f"{psngr.gender.capitalize()}  {psngr.fname.capitalize()} {psngr.lname.capitalize()}       Phone Number:   {psngr.number}", font=ctk.CTkFont(size=20))
            idbtn = ctk.CTkButton(ticket_frame, text=f" ID: {psngr.id}", width=70, command=lambda id=psngr.id: self.srt(user_id=id), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18, weight='bold'))
            l2 = ctk.CTkLabel(ticket_frame, text=f"Joined Date: {psngr.joined}", font=ctk.CTkFont(size=20))
            agebtn = ctk.CTkButton(ticket_frame)
            age = 1404-int(psngr.birth.split('/')[0])
            agebtn.configure(ticket_frame, text=f" Age: {age}", width=70, command=lambda btn=agebtn, brith=psngr.birth, age=age: self.birthdate(btn,brith,age), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18))

            l1.grid(row=0, column=0, padx=(200,0))
            idbtn.grid(row=0, column=0, sticky='w', padx=5)
            agebtn.grid(row=1, column=0, sticky='w', padx=5)
            l2.grid(row=1, column=0)

            ticket_frame.grid_columnconfigure(1, weight=1)
            e_btn = ctk.CTkButton(ticket_frame, text_color='green', fg_color='gray20', border_color='green', border_width=1, hover_color='green', text="Edit", command=lambda user=psngr.id: Topuseredit(user,ui=self), width=100)
            c_btn = ctk.CTkButton(ticket_frame, text_color='red', fg_color='gray20', border_color='red', border_width=1, hover_color='yellow', text="Delete", command=lambda user=psngr.id: Topdeluser(user, ui=self), width=100)

            e_btn.grid(row=0, column=1, padx=10, pady=5, sticky='e')
            c_btn.grid(row=0, column=2, padx=10, pady=5, sticky='e')

    def driver_btn(self, ent_info=None, arg=None):
        f=True
        if arg:
            lists = arg
            f=False
        else:
            lists = self.station.load("drivers")

        self.clear()
        self.driver_searchbox(f, ent_info)

        rev = True
        k = "a.joined"
        match self.radio:
            case "oj":
                rev = False
            case "young":
                k = "a.birth"
            case "old":
                k = "a.birth"
                rev = False

        lists.sort(key=lambda a: eval(k), reverse=rev)
        for i, drv in enumerate(lists, start=2):
            ticket_frame = ctk.CTkFrame(self.mainpage, fg_color=('gray60', 'gray20'))
            ticket_frame.grid(row=i, column=0, pady=5, padx=5, sticky="ew")
            l1 = ctk.CTkLabel(ticket_frame, text=f"{drv.gender.capitalize()}  {drv.fname.capitalize()} {drv.lname.capitalize()}", font=ctk.CTkFont(size=20))
            lp = ctk.CTkLabel(ticket_frame, text=f"Phone Number:   {drv.number}", font=ctk.CTkFont(size=20))
            idbtn = ctk.CTkButton(ticket_frame, text=f" ID: {drv.id}", width=70, command=lambda id=drv.id: self.srtr(driver_id=id), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18, weight='bold'))
            l2 = ctk.CTkLabel(ticket_frame, text=f"Joined Date: {drv.joined}      Status: {drv.status.capitalize()}", font=ctk.CTkFont(size=20))
            agebtn = ctk.CTkButton(ticket_frame)
            age = 1404-int(drv.birth.split('/')[0])
            agebtn.configure(ticket_frame, text=f" Age: {age}", width=70, command=lambda btn=agebtn, birth=drv.birth, age=age: self.birthdate(btn,birth,age), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18))
            busbtn = ctk.CTkButton(ticket_frame, text=f" Bus: {drv.bus}", width=70, command=lambda bus=drv.bus: Topbus(bus), fg_color=('gray60', 'gray20'), font=ctk.CTkFont(size=18, weight='bold'))

            l1.grid(row=0, column=0, padx=(200,0))
            lp.grid(row=0, column=1, sticky='w', padx=50)
            idbtn.grid(row=0, column=0, sticky='w', padx=5)
            agebtn.grid(row=1, column=0, sticky='w', padx=5)
            busbtn.grid(row=1, column=0, sticky='w', padx=(200,0))
            l2.grid(row=1, column=1, sticky='w', padx=10)

            ticket_frame.grid_columnconfigure(1, weight=1)
            e_btn = ctk.CTkButton(ticket_frame, text_color='green', fg_color='gray20', border_color='green', border_width=1, hover_color='green', text="Edit", command=lambda dr=drv.id: Topdriveredit(dr, ui=self), width=100)
            f_btn = ctk.CTkButton(ticket_frame, text_color='red', fg_color='gray20', border_color='red', border_width=1, hover_color='yellow', text="Fire", command=lambda driver=drv.id: Topdeldriver(driver, ui=self), width=100)

            e_btn.grid(row=0, column=1, padx=10, pady=5, sticky='e')
            f_btn.grid(row=0, column=2, padx=10, pady=5, sticky='e')

            if drv.status == "fired":
                f_btn.configure(state='disabled')


    def setradio(self, choice):
        self.radio = choice

    def setval(self, choice):
        if choice == 'Show All':
            self.switch = "Show All"
        else:
            self.switch = choice

    def srtr(self, id=None, origin=None, destination=None, date=None, driver_id=None, state=None):
        s = self.station.search_trips(id, origin, destination, date, driver_id, state)
        ent_info = {'id':id, 'org':origin, 'des':destination, 'date':date, 'driver':driver_id}
        if s:
            self.trip_btn(ent_info, s)
        else:
            self.notfound_trip(ent_info)

    def srt(self, tid=None, trid=None, origin=None, destination=None, date=None, user_id=None, driver_id=None, seat_num=None, state=None):
        s = self.station.search_tickets(tid, trid, origin, destination, date, user_id, driver_id, seat_num, state)
        ent_info = {'id':tid, 'trid':trid, 'org':origin, 'des':destination, 'date':date, 'usr':user_id, 'driver':driver_id, 'seat_num':seat_num}
        if s:
            self.ticket_btn(ent_info, s)
        else:
            self.notfound_ticket(ent_info)

    def srp(self, name='', number=None, id=None, birth=None, joined=None):
        s = self.station.search_users(name, number, id, birth, joined)
        ent_info = {'name': name, 'num':number, 'id':id, 'birth':birth, 'jd':joined}
        if s:
            self.psngr_btn(ent_info, s)
        else:
            self.notfound_user(ent_info)

    def srd(self, name='', number=None, id=None, birth=None, bus=None, state=None, joined=None):
        s = self.station.search_drivers(name, number, id, bus, birth, state, joined)
        ent_info = {'name': name, 'num':number, 'id':id, 'plt':bus, 'birth':birth, 'jd':joined}
        if s:
            self.driver_btn(ent_info, s)
        else:
            self.notfound_driver(ent_info)


    def notfound_trip(self, ent):
        self.clear()
        self.trip_searchbox(False, ent)

        label = ctk.CTkLabel(self.mainpage, text="Not Found", font=ctk.CTkFont(size=50, weight='bold'))
        label.grid(pady=(150))

    def notfound_ticket(self, ent):
        self.clear()
        self.ticket_searchbox(False, ent)

        label = ctk.CTkLabel(self.mainpage, text="Not Found", font=ctk.CTkFont(size=50, weight='bold'))
        label.grid(pady=(150))

    def notfound_user(self, ent):
        self.clear()
        self.psngr_searchbox(False, ent)

        label = ctk.CTkLabel(self.mainpage, text="Not Found", font=ctk.CTkFont(size=50, weight='bold'))
        label.grid(pady=(150))

    def notfound_driver(self, ent):
        self.clear()
        self.driver_searchbox(False, ent)

        label = ctk.CTkLabel(self.mainpage, text="Not Found", font=ctk.CTkFont(size=50, weight='bold'))
        label.grid(pady=(150))
        

    def birthdate(self, btn, birth, age):
        if "Age" not in btn.cget("text"):
            btn.configure(text=f"Age: {age}")
        else:
            btn.configure(text=f"Birth Date: {birth}")
    
    def clear(self):
        self.mainpage.destroy()
        self.mainpage = ctk.CTkScrollableFrame(self, corner_radius=20)
        self.mainpage.grid(row=0, column=1, sticky='nsew', pady=15, padx=15)
        self.mainpage.grid_columnconfigure(0, weight=1)
        self.mainpage.grid_rowconfigure(0, weight=1)

    def contact(self):
        top = ctk.CTkToplevel(self)
        top.geometry("200x50")
        txt = ctk.CTkLabel(top, text="Let me sleep...", font=ctk.CTkFont(size=20))
        txt.pack(pady=10)
        top.attributes('-topmost', True)
        top.mainloop()

    def dark_mode(self):
        ctk.set_appearance_mode(self.swt.get())
        if self.swt.cget('text') == "Dark Mode":
            self.swt.configure(text='Light Mode')
        else:
            self.swt.configure(text='Dark Mode')


if __name__ == "__main__":
    Ui().mainloop()