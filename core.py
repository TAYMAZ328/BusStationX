from classes import Trip, Ticket, User, Driver, Bus
from jdatetime import datetime as jdt
from random import randint
import csv


class Station:
    def __init__(self):
        self.trips = self.load("trips")
        self.tickets = self.load("tickets")
        self.users = self.load("users")
        self.drivers = self.load("drivers")
        self.bus = self.load("bus")
        self.now = jdt.now().strftime("%Y/%m/%d")

    def load(self, arg):
        with open(f"files\\{arg}.csv", 'r') as f:
            c = csv.DictReader(f)
            lst = []
            match arg:
                case 'trips':
                    for obj in c:
                        x = Trip(obj['id'], obj['origin'], obj['des'], obj['date'], obj['time'], obj['price'], obj['driver'], obj['reserved_seats'], obj['bus_seats'], obj['status'])
                        lst.append(x)
                case 'tickets':
                    for obj in c:
                        x = Ticket(obj['id'], obj['trid'], obj['origin'], obj['des'], obj['date'], obj['time'], obj['user'], obj['name'],obj['driver'], obj['seatnum'], obj['status'])
                        lst.append(x)
                case 'users':
                    for obj in c:
                        x = User(obj['fname'], obj['lname'], obj['id'], obj['birth'], obj['gender'], obj['number'], obj['joined'])
                        lst.append(x)
                case 'drivers':
                    for obj in c:
                        x = Driver(obj['fname'], obj['lname'], obj['id'], obj['birth'], obj['gender'], obj['number'], obj['bus'], obj['status'], obj['joined'])
                        lst.append(x)
                case 'bus':
                    for obj in c:
                        x = Bus(obj['plate'], obj['name'], obj['color'], obj['seats'], obj['is_vip'])
                        lst.append(x)
            return lst


    def save_trip(self):
        with open("files\\trips.csv", 'w', newline='') as f:
            header = ["id", "origin", "des", "date", "time", "price", "driver", "reserved_seats", "bus_seats", "status"]
            c = csv.DictWriter(f, fieldnames=header)
            c.writeheader()
            for obj in self.trips:
                c.writerow({"id":obj.trid, "origin":obj.origin.lower(), "des":obj.des.lower(), "date":obj.date, "time":obj.tm, "price":obj.price, "driver":obj.driver, "reserved_seats":obj.reserved_seats, "bus_seats":obj.seats, "status":obj.status})
    
    def save_ticket(self):
        with open("files\\tickets.csv", 'w', newline='') as f:
            header = ["id", "trid", "origin", "des", "date", "time", "user", "name", "driver", "seatnum", "status"]
            c = csv.DictWriter(f, fieldnames=header)
            c.writeheader()
            for obj in self.tickets:
                c.writerow({"id":obj.tid, "trid":obj.trid, "origin":obj.origin.lower(), "des":obj.des.lower(), "date":obj.date, "time":obj.tm, "user":obj.user, "name":obj.name, "driver":obj.driver, "seatnum":obj.seatnum, "status":obj.status})
    
    def save_users(self):
        with open("files\\users.csv", 'w', newline='') as f:
            header = ["fname", "lname", "number", "id", "birth", "gender", "joined"]
            c = csv.DictWriter(f, fieldnames=header)
            c.writeheader()
            for obj in self.users:
                c.writerow({"fname":obj.fname.lower(), "lname":obj.lname.lower(), "number":obj.number, "id":obj.id, "birth":obj.birth, "gender":obj.gender, "joined":obj.joined})

    def save_drivers(self):
        with open("files\\drivers.csv", 'w', newline='') as f:
            header = ["fname", "lname", "number", "id", "birth", "gender", "bus", "status", "joined"]
            c = csv.DictWriter(f, fieldnames=header)
            c.writeheader()
            for obj in self.drivers:
                c.writerow({"fname":obj.fname.lower(), "lname":obj.lname.lower(), "number":obj.number, "id":obj.id, "birth":obj.birth, "gender":obj.gender, "bus":obj.bus, "status":obj.status, "joined":obj.joined})
    def save_bus(self):
        with open("files\\bus.csv", 'w', newline='') as f:
            header = ["plate", "name", "color", "seats", "is_vip"]
            c = csv.DictWriter(f, fieldnames=header)
            c.writeheader()
            for obj in self.bus:
                c.writerow({"plate":obj.plate, "name":obj.name.lower(), "color":obj.color.lower(), "seats":obj.seats, "is_vip":obj.is_vip})


    def check_name(self, name, arg):
        if not name.isalpha:
            raise Exception(f"Enter only Alphabet in {arg}")
        elif not 2 < len(name) < 15:
            raise Exception(f"Invalid {arg}.")

    def generate_trid(self):
        ids = []
        for trp in self.trips:
            ids.append(int(trp.trid))

        while True:
            r = randint(100000,999999)
            if r not in ids:
                return r

    def generate_tid(self):
        ids = []
        for tkt in self.tickets:
            ids.append(int(tkt.tid))
        while True:
            r = randint(10000000,99999999)
            if r not in ids:
                return r

    def check_id(self, id, chl=False):
        if not id.isdigit():
            raise Exception("ID is Not a Number")
        elif len(id) != 10:
            raise Exception("ID must be 10 Digits")
        if chl:
            for usr in self.load("users"):
                if usr.id == id:
                    raise Exception("User already exists.")

    def check_idd(self, id, chl=False):
        if len(id) != 10:
            raise Exception("ID must be 10 Digits")
        elif not id.isdigit():
            raise Exception("ID is Not a Number")
        if chl:    
            for drv in self.load("drivers"):
                if drv.id == id:
                    raise Exception("Driver already exists.")

    def check_interuption(self, org, des, date, time):
        if org == des:
            raise Exception("Origin and Destination can't be the same.")
        for trp in self.trips:
            if trp.date == date and trp.tm == time and trp.status == 'active':
                raise Exception("One Trips exists in this Time.")

    def check_driver(self, driver):
        bus_seats = 0
        for drv in self.drivers:
            if drv.id == driver:
                for j in self.bus:
                    if drv.bus == j.plate:
                        bus_seats = j.seats
                        if drv.status != 'on_duty' and drv.status!='in_progress':
                            raise Exception(f"This Driver is corrently {drv.status.capitalize()}")
                        return bus_seats
        else:
            raise Exception("Driver Not Found")

    def date_format(self, date):
        date = map(lambda a: f"{int(a):02}", date.split('/'))
        return '/'.join(list(date))

    def check_date(self, date, arg=None):
        try:
            year, month, day = map(int, date.split('/'))
        except Exception:
            raise Exception("Invalid date format.\nCorrect: YYYY/MM/DD")

        if len(str(year)) != 4:
            raise Exception("Year must be 4 digits")
        elif not 1300 < year <1410:
            raise Exception("Invalid Year")
        elif len(str(month)) > 2 or len(str(day)) > 2:
            raise Exception("Month/Day can be mostly 2 digits")

        elif not 0 < month < 13:
            raise Exception("Month must be 1-12")
        elif month < 7:
            max_day = 31
        elif 6 < month < 12:
            max_day = 30
        elif month == 12: # سال کبیثه
            if year%4 == 3:
                max_day = 30
            else:
                max_day = 29
        if not 0 < day <= max_day:
            raise Exception(f"Invalid day for Month {month}.\nValid: 1-{max_day}")

        date = self.date_format(date)

        if arg == "trip" and date < self.now:
                raise Exception(f"Trip Date must be After {self.now}")
        elif arg == "birth" and date > self.now:
                raise Exception(f"The individual is not borned!")

        return date

    def check_time(self, time):
        try:
            time = time.split(':')
            if not -1 < int(time[0]) <24:
                raise Exception("0-23 Hours")
            elif not -1 < int(time[1]) < 60:
                raise Exception("0-60 Minuts")
        except IndexError:
            raise Exception("Invaild Time Format.\nCorrect: HH:MM")
        except ValueError:
            raise Exception("Enter a Number for Time")
        else:
            time = list(map(lambda a: f"{int(a):02}", time))
            return ':'.join(time)

    def check_num(self, num, chl=False, file="users"):
        if not num.isdigit():
            raise Exception("Phone Number must be numeric")
        elif len(num) != 11:
            raise Exception("Phone Number must be 11 Digits")
        elif num[:2] != '09':
            raise Exception("Inavild Phone Number Format.\nCorrect: 09xx xxx xxxx")
        if chl:        
            for i in self.load(file):
                if i.number == num:
                    raise Exception("This Phone Number already exists.")

    def gen(self, swch):
        if swch == 'Male':
            return 'mr'
        elif swch == 'mr':
            return 'Male'
        elif swch == 'Female':
            return 'miss'
        elif swch == 'miss':
            return 'Female'

    def check_price(self, price):
        if price:
            if not price.isdigit:
                raise Exception("Price must be Numeric")
            elif not (100000 < int(price) < 2000000):
                raise Exception("Price range 100,000-2,000,000")
        else:
            raise Exception("Enter the price")

    def check_plate(self, plate):
        if len(plate) != 9:
            raise Exception("Plate must be 9 Characters.")
        try:
            plate = plate.split('|')
            if not (len(plate[0]) == 6 and len(plate[1]) == 2 and plate[0][2].isalpha and plate[0][:2].isdigit and plate[0][2:6].isdigit and plate[1].isdigit):
                raise
        except:
            raise Exception("Invalid Plate Format.\nCorrect: xxyxxx|xx")


    def add_trip(self,origin, des, date, time, price, driver):
        id = self.generate_trid()
        self.check_name(origin, "Origin")
        self.check_name(des, "Destination")
        self.check_interuption(origin, des, date, time)
        date = self.check_date(date, "trip")
        time = self.check_time(time)
        self.check_price(price)
        bus_seats = self.check_driver(driver)

        new = Trip(id, origin, des, date, time, price, driver, reserved_seats=0, bus_seats=bus_seats, status='active')
        self.trips.append(new)
        self.save_trip()
        return id

    def add_ticket(self, trid, origin, des, date, tm, user, driver, seat):
        id = self.generate_tid()
        self.check_id(user)
        if seat == 0:
            raise Exception("Choose your Seat")

        for j in self.load("users"):
            if j.id == user:
                break
        else:
            raise KeyError

        new = Ticket(id, trid, origin, des, date, tm, user, f"{j.fname} {j.lname}", driver, seat, status="active")
        self.tickets.append(new)
        self.save_ticket()

        trips = self.load("trips")
        for i in trips:
            if i.trid == trid:
                i.reserved_seats = int(i.reserved_seats) + 1
        self.trips = trips
        self.save_trip()

        return id

    def add_user(self, fn, ln, id, pn, birth, swch):
        self.check_name(fn, "First Name")
        self.check_name(ln, "Last Name")
        self.check_num(pn, True)
        self.check_id(id, True)
        birth = self.check_date(birth, "birth")

        if not swch:
            raise Exception("Select your Gender.")
        joined = self.now

        new = User(fn, ln, id, birth, swch, pn, joined)
        self.users.append(new)
        self.save_users()

    def add_driver(self, fn, ln, id, pn, birth, swch, bus_plate, busname, color, seats, is_vip):
        self.check_name(fn, "First Name")
        self.check_name(ln, "Last Name")
        self.check_name(busname, "Model Name")
        self.check_name(color, "Color")
        self.check_num(pn, True, 'drivers')
        self.check_idd(id, True)
        birth = self.check_date(birth, "birth")
        if int(self.now.split('/')[0])-int(birth.split('/')[0]) < 18:
            raise Exception("Drive must be at least 18 years old")
        self.check_plate(bus_plate)
        if not swch:
            raise Exception("Select your Gender.")
        if not seats.isdigit():
            raise Exception("Enter a Number for seats")
        elif not 9 < int(seats) < 41:
            raise Exception("10-40 Seats")

        new = Driver(fn, ln, id, birth, swch, pn, bus_plate, status="on_duty", joined=self.now)
        self.drivers.append(new)
        self.save_drivers()

        newbus = Bus(bus_plate, busname, color, seats, is_vip)
        self.bus.append(newbus)
        self.save_bus()


    def cancel_trip(self, trip, arg="canceled"):
        trips = self.load("trips")
        for i in trips:
            if i.trid == trip:
                i.status = arg
                break

        tickets = self.load("tickets")
        for i in tickets:
            if i.trid == trip:
                i.status = arg

        self.trips = trips
        self.save_trip()
        self.tickets = tickets
        self.save_ticket()

    def cancel_ticket(self, ticket):
        tickets = self.load("tickets")
        for i in tickets:
            if i.tid == ticket:
                i.status = "canceled"
                trip = i.trid

        trips = self.load("trips")
        for i in trips:
            if i.trid == trip:
                i.reserved_seats = int(i.reserved_seats) - 1
                break

        self.tickets = tickets
        self.save_ticket()
        self.trips = trips
        self.save_trip()
        
    def del_user(self, user):
        users = self.load("users")
        for usr in users:
            if usr.id == user:
                users.remove(usr)
                break

        tickets = self.load("tickets")
        for tkt in tickets:
            if tkt.user == user:
                self.cancel_ticket(tkt.tid)

        self.users = users
        self.save_users()
     
    def del_driver(self, driver):
        drivers = self.load("drivers")
        for drv in drivers:
            if drv.id == driver:
                drv.status = "fired"
                break

        trips = self.load("trips")
        for trp in trips:
            if trp.driver == driver and trp.status == "active":
                self.cancel_trip(trp.trid)

        self.drivers = drivers
        self.save_drivers()


    def edit_user(self, fn, ln, id, pn, birth, swch):
        self.check_name(fn, "First Name")
        self.check_name(ln, "Last Name")
        self.check_num(pn)
        self.check_id(id)
        birth = self.check_date(birth, "birth")

        users = self.load("users")
        for usr in users:
            if usr.id == id:
                usr.fname = fn
                usr.lname = ln
                usr.id = id
                usr.number = pn
                usr.birth = birth
                usr.gender = self.gen(swch)
                break
        self.users = users
        self.save_users()

    def edit_driver(self, fn, ln, id, pn, birth, swch, bus_plate, busname, color, seats, is_vip, status):
        self.check_name(fn, "First Name")
        self.check_name(ln, "Last Name")
        self.check_name(busname, "Model Name")
        self.check_name(color, "Color")
        self.check_num(pn)
        self.check_idd(id)
        birth = self.check_date(birth, "birth")
        if int(self.now.split('/')[0])-int(birth.split('/')[0]) < 18:
            raise Exception("Drive must be at least 18 years old")
        self.check_plate(bus_plate)
        drivers = self.load("drivers")
        for drv in drivers:
            if drv.id == id:
                drv.fname = fn
                drv.lname = ln
                drv.id = id
                drv.number = pn
                drv.birth = birth
                drv.gender = self.gen(swch)
                drv.bus_plate = bus_plate
                drv.status = status
                break

        bus = self.load("bus")
        for bs in bus:
            if bs.plate == bus_plate:
                bs.bus_plate = bus_plate
                bs.name = busname
                bs.color = color
                bs.seats = seats
                bs.is_vip = is_vip
                break

        self.drivers = drivers
        self.save_drivers()
        self.bus = bus
        self.save_bus()


    def search(self, arg, filters):
        records = self.load(arg)
        results = []
        for record in records:
            match = all(getattr(record,k) == v for k,v in filters.items())
            if match:
                results.append(record)
        return results

    def search_trips(self, id, origin, destination, date, driver_id, state):
        if state == "Show All":
            state = None
        filters = {}
        if id: filters['trid'] = id
        if origin: filters['origin'] = origin
        if destination: filters['des'] = destination
        if date: filters['date'] = self.date_format(date)
        if driver_id: filters['driver'] = driver_id
        if state: filters['status'] = state
        return self.search('trips', filters)

    def search_tickets(self, tid, trid, origin, destination, date, user_id, driver_id, seat_num, state):
        if state == "Show All":
            state = None
        filters = {}
        if tid: filters['tid'] = tid
        if trid: filters['trid'] = trid
        if origin: filters['origin'] = origin
        if destination: filters['des'] = destination
        if date: filters['date'] = self.date_format(date)
        if user_id: filters['user'] = user_id
        if driver_id: filters['driver'] = driver_id
        if seat_num: filters['seatnum'] = seat_num
        if state: filters['status'] = state
        return self.search('tickets', filters)

    def search_users(self, name, number, id, birth, joined):
        filters = {}
        n = name.split()
        if len(n) > 1:
            if name: filters['fname'] = n[0]
            if name: filters['lname'] = n[1]
        else:
            if name: filters['lname'] = n[0]
        if number: filters['number'] = number
        if id: filters['id'] = id
        if birth: filters['birth'] = self.date_format(birth)
        if joined: filters['joined'] = self.date_format(joined)
        return self.search('users', filters)

    def search_drivers(self, name, number, id, birth, bus, state, joined):
        if state == "Show All":
            state = None
        filters = {}
        n = name.split()
        if len(n) > 1:
            if name: filters['fname'] = n[0]
            if name: filters['lname'] = n[1]
        else:
            if name: filters['lname'] = n[0]
        if number: filters['number'] = number
        if id: filters['id'] = id
        if birth: filters['birth'] = self.date_format(birth)
        if bus: filters['bus'] = bus
        if state: filters['status'] = state
        if joined: filters['joined'] = self.date_format(joined)
        return self.search('drivers', filters)

