from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox


class Member(ABC):
    def __init__(self, name):
        self._name = name
        self._discount = 0

    @abstractmethod
    def get_discount(self):
        pass

    def __str__(self):
        return f"Member: {self._name}, Discount: {self.get_discount()}%"



class BasicMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self._discount = 10


    def get_discount(self):
        return self._discount

class EliteSilverMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self._discount = 20

    def get_discount(self):
        return self._discount

class EliteGoldMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self._discount = 30

    def get_discount(self):
        return self._discount


class NoMember:
    def __init__(self, name):
        self.name = name

    def get_discount(self):
        return 0

    def __str__(self):
        return f"Customer: {self.name}, Discount: {self.get_discount()}%"


def calculate_price(price, discount):
    return price - (price * discount / 100)



class VistaflyerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Vistaflyer Loyalty Program')
        self.create_widgets()
        self.members = []

    def create_widgets(self):
        self.welcome_label = tk.Label(self.root, text="Welcome to Vistaflyer Loyalty Program", font=("Helvetica", 16))
        self.welcome_label.pack(pady=10)


        self.membership_label = tk.Label(self.root, text="Select Membership Type:")
        self.membership_label.pack(pady=5)

        self.membership_var = tk.StringVar(value="None")

        self.basic_radio = tk.Radiobutton(self.root, text= "Basic Membership", variable=self.membership_var, value="Basic")
        self.basic_radio.pack()

        self.silver_radio = tk.Radiobutton(self.root, text="Elite Silver Membership", variable=self.membership_var, value="Silver")
        self.silver_radio.pack()

        self.gold_radio = tk.Radiobutton(self.root, text="Elite Gold Membership", variable=self.membership_var, value="Gold")
        self.gold_radio.pack()

        self.none_radio = tk.Radiobutton(self.root, text="Non-Member", variable=self.membership_var, value="None")
        self.none_radio.pack()

        self.name_label = tk.Label(self.root, text="Enter your name:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

        self.show_button = tk.Button(self.root, text="Show All", command=self.show_members)
        self.show_button.pack(pady = 20)

    def submit(self):
        print(self.membership_var.get(), self.name_entry.get())

        name = self.name_entry.get()
        type = self.membership_var.get()

        if not name:
            messagebox.showwarning("Input Error", "Please provide your name")

        if type == "None":
            self.member = NoMember(name)
        elif type == "Basic":
            self.member = BasicMember(name)
            self.members.append(self.member)
        elif type == "Silver":
            self.member = EliteSilverMember(name)
            self.members.append(self.member)
        elif type == "Gold":
            self.member = EliteGoldMember(name)
            self.members.append(self.member)

        message = (f"Hello {name}!\n"
                   f"You have registered as a {type} member.\n"
                   f"You are eligible for a {self.member.get_discount()}% discount.")

        messagebox.showinfo("Registration Complete", message)

        with open("vistaflyer_members.txt", "a") as file:
            file.write(f"Name: {name}, Membership Type: {type}, Discount: {self.member.get_discount()}%\n")

        self.name_entry.delete(0, 'end')



    def show_members(self):
        secondary_window = tk.Toplevel(root)
        secondary_window.title("Secondary Window")

        read_text = tk.Text(secondary_window, wrap=tk.WORD)
        read_text.pack(pady=10, padx=10)

        with open("vistaflyer_members.txt", "r") as file:
            self.content = file.read()
            read_text.insert(tk.END, self.content)



        #tk.Label(secondary_window, text=self.content, font=("Helvetica", 16)).pack(pady=10)

        # for member in self.members:
        #     tk.Label(secondary_window, text=f"{member}",
        #                                   font=("Helvetica", 16)).pack(pady=10)






if __name__ == '__main__':
    root = tk.Tk()
    app = VistaflyerApp(root)
    root.mainloop()

