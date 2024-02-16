import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
from datetime import datetime

class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")

        # Initialize variables
        self.users = self.load_users()
        self.customers = self.load_customers()
        self.prescriptions = self.load_prescriptions()
        self.medicine_inventory = self.load_medicine_inventory()
        

        # Create GUI components
        self.create_login_screen()
    
    def askstring_int(self, title, prompt, **kwargs):
        result = simpledialog.askstring(title, prompt, **kwargs)
        return str(result) if result is not None else None

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def load_medicine_inventory(self):
        try:
            with open("medicine_inventory.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_medicine_inventory(self):
        with open("medicine_inventory.json", "w") as file:
            json.dump(self.medicine_inventory, file)
    
    def save_customers(self):
        with open("customers.json", "w") as file:
            json.dump(self.customers, file)

    def load_customers(self):
        try:
            with open("customers.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_prescriptions(self):
        with open("prescription_history.json", "w") as file:
            json.dump(self.prescriptions, file)
    
    def load_prescriptions(self):
        try:
            with open("prescription_history.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def create_login_screen(self):
        # Login screen components
        self.login_label = tk.Label(self.root, text="Username:")
        self.login_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")
        self.login_button = tk.Button(self.root, text="Login", command=self.authenticate_user)

        # Place components on the screen
        self.login_label.grid(row=0, column=0, pady=10)
        self.login_entry.grid(row=0, column=1, pady=10)
        self.password_label.grid(row=1, column=0, pady=10)
        self.password_entry.grid(row=1, column=1, pady=10)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Registration components
        self.register_label = tk.Label(self.root, text="New User? Register Below:")
        self.new_username_label = tk.Label(self.root, text="New Username:")
        self.new_username_entry = tk.Entry(self.root)
        self.new_password_label = tk.Label(self.root, text="New Password:")
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.register_button = tk.Button(self.root, text="Register", command=self.register_user)

        # Place registration components on the screen
        self.register_label.grid(row=3, column=0, columnspan=2, pady=10)
        self.new_username_label.grid(row=4, column=0, pady=10)
        self.new_username_entry.grid(row=4, column=1, pady=10)
        self.new_password_label.grid(row=5, column=0, pady=10)
        self.new_password_entry.grid(row=5, column=1, pady=10)
        self.register_button.grid(row=6, column=0, columnspan=2, pady=10)

    def authenticate_user(self):
        username = self.login_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register_user(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()

        if new_username and new_password:
            self.users[new_username] = new_password
            self.save_users()
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Please enter both username and password")

    def create_main_menu(self):
        # Destroy login and registration screen components
        self.login_label.destroy()
        self.login_entry.destroy()
        self.password_label.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()
        self.register_label.destroy()
        self.new_username_label.destroy()
        self.new_username_entry.destroy()
        self.new_password_label.destroy()
        self.new_password_entry.destroy()
        self.register_button.destroy()

        # Main menu components
        self.menu_label = tk.Label(self.root, text="Pharmacy Management System")
        self.register_customer_button = tk.Button(self.root, text="Register Customer", command=self.register_customer)
        self.update_customer_button = tk.Button(self.root, text="Update Customer Information", command=self.update_customer_information)
        self.fill_prescription_button = tk.Button(self.root, text="Fill Prescription", command=self.fill_prescription)
        self.inventory_button = tk.Button(self.root, text="Inventory", command=self.view_inventory)
        self.prescription_history_button = tk.Button(self.root, text="Prescription History", command=self.check_prescription_history)

        # Place components on the screen
        self.menu_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.register_customer_button.grid(row=1, column=0, pady=10)
        self.update_customer_button.grid(row=1, column=1, pady=10)
        self.fill_prescription_button.grid(row=2, column=0, pady=10)
        self.inventory_button.grid(row=2, column=1, pady=10)
        self.prescription_history_button.grid(row=3, column=0, columnspan=2, pady=10)

    def register_customer(self):
        customer_name = simpledialog.askstring("Register Customer", "Enter customer name:")
        customer_age = simpledialog.askinteger("Register Customer", "Enter customer age:")
        customer_gender = simpledialog.askstring("Register Customer", "Enter customer gender:")
        customer_contact = simpledialog.askstring("Register Customer", "Enter customer contact:")
        customer_address = simpledialog.askstring("Register Customer", "Enter customer address:")

        if customer_name and customer_age and customer_gender and customer_contact and customer_address:
            # Assign a customer id
            customer_id = len(self.customers) + 1
            self.customers[customer_id] = {
                "Name": customer_name,
                "Age": customer_age,
                "Gender": customer_gender,
                "Contact": customer_contact,
                "Address": customer_address
            }
            self.save_customers()
            messagebox.showinfo("Success", f"Customer {customer_name} registered with ID {customer_id}!")
        else:
            messagebox.showerror("Error", "Please fill in all customer details.")

    def update_customer_information(self):
            # Load the list of customers from customers.json
            self.customers = self.load_customers()

            #print("Loaded customers:", self.customers)  # Debugging statement

            customer_list = "\n".join(f"ID: {customer_id}, Name: {customer['Name']}" for customer_id, customer in self.customers.items())
            selected_customer_id = self.askstring_int("Update Customer Information", f"Select a customer to update information for:\n{customer_list}")


            #print("Selected customer ID:", selected_customer_id)  # Debugging statement

            if selected_customer_id is not None and selected_customer_id in self.customers:
                selected_customer = self.customers[selected_customer_id]
                updated_customer = selected_customer.copy()

                # Display the current information of the selected customer
                current_info_message = f"Current Information for {selected_customer['Name']} (ID: {selected_customer_id}):\n"
                current_info_message += f"Name: {selected_customer['Name']}\nAge: {selected_customer['Age']}\nGender: {selected_customer['Gender']}\nContact: {selected_customer['Contact']}\nAddress: {selected_customer['Address']}\n"
                
                # Ask the user for updated information
                updated_name = simpledialog.askstring("Update Customer Information", "Enter updated name (leave empty to keep current):", initialvalue=selected_customer['Name'])
                updated_age = simpledialog.askinteger("Update Customer Information", "Enter updated age (leave empty to keep current):", initialvalue=selected_customer['Age'])
                updated_gender = simpledialog.askstring("Update Customer Information", "Enter updated gender (leave empty to keep current):", initialvalue=selected_customer['Gender'])
                updated_contact = simpledialog.askstring("Update Customer Information", "Enter updated contact (leave empty to keep current):", initialvalue=selected_customer['Contact'])
                updated_address = simpledialog.askstring("Update Customer Information", "Enter updated address (leave empty to keep current):", initialvalue=selected_customer['Address'])

                # Update the customer information if new values are provided
                if updated_name:
                    updated_customer['Name'] = updated_name
                if updated_age is not None:
                    updated_customer['Age'] = updated_age
                if updated_gender:
                    updated_customer['Gender'] = updated_gender
                if updated_contact:
                    updated_customer['Contact'] = updated_contact
                if updated_address:
                    updated_customer['Address'] = updated_address

                # Update the customer in the customers dictionary
                self.customers[selected_customer_id] = updated_customer

                # Save the updated customer information
                self.save_customers()

                # Display the updated information to the user
                updated_info_message = f"\nUpdated Information:\n"
                updated_info_message += f"Name: {updated_customer['Name']}\nAge: {updated_customer['Age']}\nGender: {updated_customer['Gender']}\nContact: {updated_customer['Contact']}\nAddress: {updated_customer['Address']}\n"

                messagebox.showinfo("Customer Information Updated", current_info_message + updated_info_message)
            else:
                messagebox.showerror("Error", "Invalid customer ID.")

    def view_inventory(self):
        inventory_window = tk.Toplevel(self.root)
        inventory_window.title("Medicine Inventory")

        # Create Treeview widget
        inventory_tree = ttk.Treeview(inventory_window)
        inventory_tree["columns"] = ("Medicine", "Quantity", "Price")
        inventory_tree.column("#0", width=0, stretch=tk.NO)  # Hide the default first column
        inventory_tree.heading("#1", text="Medicine")
        inventory_tree.heading("#2", text="Quantity")
        inventory_tree.heading("#3", text="Price")

        # Insert data into the Treeview
        for med, details in self.medicine_inventory.items():
            quantity = details.get("Quantity", "")
            price = details.get("Price", "")
            inventory_tree.insert("", "end", values=(med, quantity, price))

        # Pack the Treeview
        inventory_tree.pack(expand=True, fill=tk.BOTH)

    def fill_prescription(self):
        # Load the list of customers from customers.json
        self.customers = self.load_customers()

        customer_list = "\n".join(f"ID: {customer_id}, Name: {customer['Name']}" for customer_id, customer in self.customers.items())
        selected_customer_id = self.askstring_int("Fill Prescription", f"Select a customer to fill prescription for:\n{customer_list}")

        if selected_customer_id is not None and selected_customer_id in self.customers:
            selected_customer = self.customers[selected_customer_id]
            prescription_details = {}  # To store medicine and quantity details

            while True:
                # Display available medicine names in inventory
                available_medicines = "\n".join(self.medicine_inventory.keys())
                medicine_name = simpledialog.askstring("Fill Prescription", f"Enter medicine name (Available Medicines:\n{available_medicines})\nor leave empty to finish:")
                if not medicine_name:
                    break

                # Check if the entered medicine exists in the inventory
                if medicine_name not in self.medicine_inventory:
                    messagebox.showerror("Error", f"Medicine '{medicine_name}' is not in the inventory.\nAvailable Medicines:\n{available_medicines}")
                    continue

                quantity = simpledialog.askinteger("Fill Prescription", f"Enter quantity for {medicine_name} (Available Quantity: {self.medicine_inventory[medicine_name]['Quantity']}):")
                if quantity is not None:
                    # Check if the entered quantity is sufficient
                    if quantity > self.medicine_inventory[medicine_name]['Quantity']:
                        messagebox.showerror("Error", f"Insufficient quantity for '{medicine_name}'. Available Quantity: {self.medicine_inventory[medicine_name]['Quantity']}")
                        continue

                    prescription_details[medicine_name] = quantity

            # Calculate total amount
            total_amount = sum(self.medicine_inventory[med]["Price"] * qty for med, qty in prescription_details.items())

            # Display bill
            bill_message = f"Customer: {selected_customer['Name']}\nMedicines:\n"
            for med, qty in prescription_details.items():
                price = self.medicine_inventory[med]["Price"]
                subtotal = price * qty
                bill_message += f"{med}: {qty} x ${price:.2f} = ${subtotal:.2f}\n"
            
            bill_message += f"\nTotal Amount: ${total_amount:.2f}"
            
            # Create a top-level window for the bill
            bill_window = tk.Toplevel(self.root)
            bill_window.title("Bill Details")

            bill_label = tk.Label(bill_window, text=bill_message, padx=10, pady=10)
            bill_label.pack()

            # Add buttons to mark the bill as paid or cancel
            paid_button = tk.Button(bill_window, text="Mark as Paid", command=lambda: self.mark_bill_as_paid(selected_customer_id, prescription_details, total_amount))
            paid_button.pack(side=tk.LEFT, padx=5)
            
            cancel_button = tk.Button(bill_window, text="Cancel", command=bill_window.destroy)
            cancel_button.pack(side=tk.RIGHT, padx=5)
        else:
            messagebox.showerror("Error", "Invalid customer ID.")

    def mark_bill_as_paid(self, customer_id, prescription_details, total_amount):
        # Generate a unique prescription ID (you can use a timestamp or any unique identifier)
        prescription_id = len(self.prescriptions) + 1
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get customer name using the provided customer_id
        customer_name = self.customers[str(customer_id)]['Name']

        # Mark the prescription as paid
        prescription = {
            "CustomerID": str(customer_id),  # Convert to string if necessary
            "CustomerName": customer_name,
            "Medicines": prescription_details,
            "TotalAmount": total_amount,
            "Paid": True,
            "Date": current_date
        }

        # Save prescription to history using the prescription ID
        self.prescriptions[prescription_id] = prescription
        self.save_prescriptions()

        # Subtract the quantity of medicines from medicine_inventory.json
        for med, qty in prescription_details.items():
            if med in self.medicine_inventory and self.medicine_inventory[med]['Quantity'] >= qty:
                self.medicine_inventory[med]['Quantity'] -= qty
            else:
                messagebox.showerror("Error", f"Insufficient quantity for '{med}'. Cannot complete the transaction.")
                return

        # Save updated medicine_inventory.json
        self.save_medicine_inventory()

        # Close the bill window
        messagebox.showinfo("Payment Successful", "Bill marked as paid successfully.")
        self.bill_window.destroy()
        


    def check_prescription_history(self):
        # Create a new window for prescription history
        prescription_history_window = tk.Toplevel(self.root)
        prescription_history_window.title("Prescription History")

        # Create Treeview widget for the table
        prescription_tree = ttk.Treeview(prescription_history_window)
        prescription_tree["columns"] = ("Prescription_ID", "Customer_ID", "Customer_Name", "Prescription", "Total_Bill", "Date")
        prescription_tree.heading("#0", text="Prescription_ID", anchor=tk.W)
        prescription_tree.column("#0", anchor=tk.W)
        prescription_tree.heading("#1", text="Customer_ID")
        prescription_tree.heading("#2", text="Customer_Name")
        prescription_tree.heading("#3", text="Prescription")
        prescription_tree.heading("#4", text="Total_Bill")
        prescription_tree.heading("#5", text="Date")

        # Fetch prescription history from prescription_history.json
        try:
            with open("prescription_history.json", "r") as file:
                prescription_data = json.load(file)

            # Display all prescriptions in the table
            for prescription_id, prescription in prescription_data.items():
                customer_id = prescription["CustomerID"]
                customer_name = prescription["CustomerName"]
                medicines_info = "\n".join([f"{med}: {qty} x ${self.medicine_inventory[med]['Price']:.2f}" for med, qty in prescription["Medicines"].items()])
                total_bill = prescription["TotalAmount"]
                date = prescription["Date"]
                prescription_tree.insert("", "end", values=(prescription_id, customer_id, customer_name, medicines_info, total_bill, date))

        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Error reading prescription history data.")
            prescription_history_window.destroy()
            return

        # Pack the Treeview
        prescription_tree.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyApp(root)
    root.mainloop()
