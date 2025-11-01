class User:
    def __init__(self, fname, lname, id, birth, gender, number, joined):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.birth = birth
        self.gender = gender
        self.number = number
        self.joined = joined

class Bus:
    def __init__(self, plate, name, color, seats, is_vip):
        self.plate = plate
        self.name = name
        self.color = color
        self.seats = seats
        self.is_vip = is_vip

class Driver(User):
    def __init__(self, fname, lname, id, birth, gender, number, bus, status, joined, photo=None):
        super().__init__(fname, lname, id, birth, gender, number, joined)
        self.bus = bus
        self.status = status
        self.joined = joined
        self.photo = photo

class Trip:
    def __init__(self, trid, origin, des, date, time, price, driver, reserved_seats, bus_seats, status):
        self.trid = trid
        self.origin = origin
        self.des = des
        self.date = date
        self.tm = time
        self.price = price
        self.driver = driver
        self.reserved_seats = reserved_seats
        self.seats = bus_seats
        self.status = status

class Ticket:
    def __init__(self, tid, trid, origin, des, date, time, user, name, driver, seatnum, status):
        self.tid = tid
        self.trid = trid
        self.origin = origin
        self.des = des
        self.date = date
        self.tm = time
        self.user = user
        self.name = name
        self.driver = driver
        self.seatnum = seatnum
        self.status = status