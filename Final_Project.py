import tkinter as tk
from tkinter import messagebox

class CoffeeShopManager:
    MAX_COFFEE_BEANS = 1000  # Adjust the maximum coffee beans as needed

    def __init__(self, master):
        self.master = master
        self.master.title("Coffee Shop Manager")

        # Variables for input validation and coffee beans tracking
        self.quantity_var = tk.StringVar()
        self.quantity_var.trace_add("write", self.validate_quantity)
        self.coffee_beans = 0  # Initial coffee beans value

        # Create a Frame for the background
        self.background_frame = tk.Frame(self.master, width=800, height=600, bg="#c0ffee")
        self.background_frame.pack_propagate(False)
        self.background_frame.pack()

        # Create a Frame for main widgets on top of the background
        self.main_frame = tk.Frame(self.background_frame)
        self.main_frame.pack(expand=True)

        # Create widgets on top of the main Frame
        self.create_widgets()

    def create_widgets(self):
        # Main Window
        self.label1 = tk.Label(self.main_frame, text="Coffee Shop Manager", font=("Helvetica", 16, "bold"))
        self.label1.pack(pady=10)

        self.button1 = tk.Button(self.main_frame, text="Manage Coffee Beans", command=self.open_coffee_beans_manager)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.main_frame, text="Use Coffee Beans", command=self.use_coffee_beans)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self.main_frame, text="Exit", command=self.exit_application)
        self.button3.pack(pady=10)

        # Coffee Beans Tracker Label
        self.coffee_beans_label = tk.Label(self.main_frame, text=f"Current Coffee Beans: {self.coffee_beans}")
        self.coffee_beans_label.pack(pady=10)

    def open_coffee_beans_manager(self):
        coffee_beans_window = tk.Toplevel(self.master)
        coffee_beans_window.title("Coffee Beans Manager")

        self.label2 = tk.Label(coffee_beans_window, text="Manage Coffee Beans", font=("Helvetica", 16, "bold"))
        self.label2.pack(pady=10)

        self.quantity_label = tk.Label(coffee_beans_window, text="Enter Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(coffee_beans_window, textvariable=self.quantity_var)
        self.quantity_entry.pack()

        self.button4 = tk.Button(coffee_beans_window, text="Update Coffee Beans", command=self.update_coffee_beans)
        self.button4.pack(pady=10)

        self.button5 = tk.Button(coffee_beans_window, text="Exit", command=coffee_beans_window.destroy)
        self.button5.pack(pady=10)

    def use_coffee_beans(self):
        use_window = tk.Toplevel(self.master)
        use_window.title("Use Coffee Beans")

        self.label3 = tk.Label(use_window, text="Use Coffee Beans", font=("Helvetica", 16, "bold"))
        self.label3.pack(pady=10)

        self.use_quantity_label = tk.Label(use_window, text="Enter Quantity to Use:")
        self.use_quantity_label.pack()

        self.use_quantity_entry = tk.Entry(use_window, textvariable=self.quantity_var)
        self.use_quantity_entry.pack()

        self.button6 = tk.Button(use_window, text="Use", command=self.subtract_coffee_beans)
        self.button6.pack(pady=10)

        self.button7 = tk.Button(use_window, text="Exit", command=use_window.destroy)
        self.button7.pack(pady=10)

    def update_coffee_beans(self):
        try:
            quantity = int(self.quantity_var.get())
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")

            # Placeholder logic to update coffee beans
            if 0 <= quantity <= (self.MAX_COFFEE_BEANS - self.coffee_beans):
                self.coffee_beans += quantity
                updated_quantity_message = f"Coffee beans updated by {quantity} units. Current Coffee Beans: {self.coffee_beans}"
                self.coffee_beans_label.config(text=f"Current Coffee Beans: {self.coffee_beans}")
                messagebox.showinfo("Success", updated_quantity_message)
            else:
                messagebox.showerror("Error", f"Invalid quantity. Maximum allowed: {self.MAX_COFFEE_BEANS - self.coffee_beans}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid non-negative integer quantity.")

    def subtract_coffee_beans(self):
        try:
            quantity_to_use = int(self.quantity_var.get())
            if quantity_to_use < 0:
                raise ValueError("Quantity to use cannot be negative")

            # Placeholder logic to subtract coffee beans
            if 0 <= quantity_to_use <= self.coffee_beans:
                self.coffee_beans -= quantity_to_use
                used_quantity_message = f"Used {quantity_to_use} units from coffee beans. Current Coffee Beans: {self.coffee_beans}"
                self.coffee_beans_label.config(text=f"Current Coffee Beans: {self.coffee_beans}")
                messagebox.showinfo("Success", used_quantity_message)
            else:
                messagebox.showerror("Error", f"Invalid quantity. Current Coffee Beans: {self.coffee_beans}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid non-negative integer quantity.")

    def exit_application(self):
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if result == 'yes':
            self.master.destroy()

    def validate_quantity(self, *args):
        current_text = self.quantity_var.get()
        if current_text and (not current_text.isdigit() or int(current_text) < 0):
            self.quantity_var.set(''.join(filter(str.isdigit, current_text)))

def main():
    root = tk.Tk()
    app = CoffeeShopManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
