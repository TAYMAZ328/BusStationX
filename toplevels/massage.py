import customtkinter as ctk


class Topwindow(ctk.CTkToplevel):
    def __init__(self, win=None, ui=None, ref=None, geo="300x120", title="Message", label=None, color=None):
        super().__init__()
        self.geometry(geo)
        self.title(title)
        self.attributes('-topmost', True)
        self.lift()
        self.focus_force()
        self.grab_set()
        lb = ctk.CTkLabel(self, text=label, text_color=color, font=ctk.CTkFont(size=20, weight='bold'))
        btn = ctk.CTkButton(self, text="Ok", command=lambda: self.des(win,ui,ref))

        lb.pack(pady=10)
        btn.pack()

    def des(self,win,ui,ref):
        self.destroy()
        if win:
            win.destroy()
        if ui:
            eval(f"ui.{ref}")

class Topask(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Massage")
        self.attributes('-topmost', True)
        self.lift()
        self.focus_force()
        self.grab_set()
        lb = ctk.CTkLabel(self, text="This Passenger dous not exists\nWould you like to add a new Passenger?", font=ctk.CTkFont(size=20))
        nobtn = ctk.CTkButton(self, text="Cancel", fg_color='red', command=lambda: self.destroy())
        yesbtn = ctk.CTkButton(self, text="Yes", fg_color='green', command=self.yes)

        lb.pack(pady=10)
        nobtn.pack(padx=10, pady=10, side="left")
        yesbtn.pack(padx=20, pady=10, side='right')

    def yes(self):
        self.destroy()
        from .users import Topuser
        Topuser(ui=None)
