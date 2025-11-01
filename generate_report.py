from fpdf import FPDF
from toplevels import Topwindow
from jdatetime import datetime as jdt


class Pdf(FPDF):
    def __init__(self, lists):
        super().__init__()
        file = f"reports\\{lists[0].trid}.pdf"
        r = 1 if len(lists)//6 == 1 else len(lists)//6+1

        ticket = 0
        for i in range(r):
            self.add_page()
            self.set_y(10)
            self.set_font("Arial",size=18)
            self.cell(0, 10, f"TAYMAZ Bus Staion", "B", align='C')
            y=30
            n=0
            while n < 6:
                if ticket > len(lists)-1:
                    break
                self.add_ticket(lists[ticket], y=y)
                y += 40
                n += 1
                ticket += 1

        self.output(file)
        Topwindow(label=f"Report Generated.✔️\nFile Name: {file}", color="green")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", size=13)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

        self.set_y(-10)
        self.set_font("Times", "UI", size=10)
        self.cell(0, 10, jdt.now().strftime("%Y/%m/%d %H:%M"), align='R')
    
    def add_ticket(self, ticket, x=10, y=10, box_width=190, box_height=35):
        self.set_xy(x, y)
        self.rect(x, y, box_width, box_height)
        self.line(x+box_width/2, y, x+box_width/2, y+box_height)

        self.set_font("Arial", size=15)

        self.set_xy(x+2, y+2)
        self.multi_cell(box_width/2-4, 8, f"Trip ID: {ticket.trid}\nFrom: {ticket.origin.capitalize()}        To: {ticket.des.capitalize()}\nDate: {ticket.date}\nTime: {ticket.tm}")

        self.set_xy(x+box_width/2+2, y+2)
        self.multi_cell(box_width/2-4, 8, f"Ticket ID: {ticket.tid}\nName: {ticket.name.title()}\nSeat: {ticket.seatnum}       Bus: {ticket.driver}")
