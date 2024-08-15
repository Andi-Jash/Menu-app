import tkinter as tk
from tkinter import messagebox

menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.49,
    "Salad": 3.99,
    "Chicken Wings": 6.49
}

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Ordering System")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Menu Label
        self.menu_label = tk.Label(self.root, text="Menu", font=("Arial", 16))
        self.menu_label.pack(pady=10)

        # Menu Listbox
        self.menu_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=5)
        for item in menu.keys():
            self.menu_listbox.insert(tk.END, item)
        self.menu_listbox.pack(pady=5)

        # Add Item Button
        self.add_item_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_item_button.pack(pady=5)

        # Order Entry
        self.order_label = tk.Label(self.root, text="Order List", font=("Arial", 16))
        self.order_label.pack(pady=10)

        self.order_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=5)
        self.order_listbox.pack(pady=5)

        # Calculate Total Button
        self.calculate_total_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_total_button.pack(pady=10)

    def add_item(self):
        selected_item_index = self.menu_listbox.curselection()
        if not selected_item_index:
            messagebox.showwarning("Selection Error", "Please select an item from the menu.")
            return
        selected_item = self.menu_listbox.get(selected_item_index)
        self.order_listbox.insert(tk.END, selected_item)

    def calculate_total(self):
        order_items = self.order_listbox.get(0, tk.END)
        if not order_items:
            messagebox.showinfo("Order Summary", "No items have been ordered.")
            return

        total = sum(menu[item] for item in order_items)
        summary = "\n".join(f"{item}: ${menu[item]:.2f}" for item in order_items)
        summary += f"\nTotal: ${total:.2f}"

        messagebox.showinfo("Order Summary", summary)

# Create the main window
root = tk.Tk()
app = RestaurantApp(root)
root.mainloop()