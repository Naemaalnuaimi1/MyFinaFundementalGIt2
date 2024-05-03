
import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle

class EventManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")

        # Load data
        self.load_data()

        # Create and place widgets
        self.label = tk.Label(self.root, text="Welcome to Event Management System")
        self.label.pack(pady=10)

        # Event buttons
        self.btn_add_event = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.btn_add_event.pack()

        self.btn_delete_event = tk.Button(self.root, text="Delete Event", command=self.delete_event)
        self.btn_delete_event.pack()

        self.btn_modify_event = tk.Button(self.root, text="Modify Event", command=self.modify_event)
        self.btn_modify_event.pack()

        self.btn_display_events = tk.Button(self.root, text="Display Events", command=self.display_events)
        self.btn_display_events.pack()

        # Client buttons
        self.btn_add_client = tk.Button(self.root, text="Add Client", command=self.add_client)
        self.btn_add_client.pack()

        self.btn_delete_client = tk.Button(self.root, text="Delete Client", command=self.delete_client)
        self.btn_delete_client.pack()

        self.btn_modify_client = tk.Button(self.root, text="Modify Client", command=self.modify_client)
        self.btn_modify_client.pack()

        self.btn_display_clients = tk.Button(self.root, text="Display Clients", command=self.display_clients)
        self.btn_display_clients.pack()

        # Supplier buttons
        self.btn_add_supplier = tk.Button(self.root, text="Add Supplier", command=self.add_supplier)
        self.btn_add_supplier.pack()

        self.btn_delete_supplier = tk.Button(self.root, text="Delete Supplier", command=self.delete_supplier)
        self.btn_delete_supplier.pack()

        self.btn_modify_supplier = tk.Button(self.root, text="Modify Supplier", command=self.modify_supplier)
        self.btn_modify_supplier.pack()

        self.btn_display_suppliers = tk.Button(self.root, text="Display Suppliers", command=self.display_suppliers)
        self.btn_display_suppliers.pack()

        # Employee buttons
        self.btn_add_employee = tk.Button(self.root, text="Add Employee", command=self.add_employee)
        self.btn_add_employee.pack()

        self.btn_delete_employee = tk.Button(self.root, text="Delete Employee", command=self.delete_employee)
        self.btn_delete_employee.pack()

        self.btn_modify_employee = tk.Button(self.root, text="Modify Employee", command=self.modify_employee)
        self.btn_modify_employee.pack()

        self.btn_display_employees = tk.Button(self.root, text="Display Employees", command=self.display_employees)
        self.btn_display_employees.pack()

        # Venue buttons
        self.btn_add_venue = tk.Button(self.root, text="Add Venue", command=self.add_venue)
        self.btn_add_venue.pack()

        self.btn_delete_venue = tk.Button(self.root, text="Delete Venue", command=self.delete_venue)
        self.btn_delete_venue.pack()

        self.btn_modify_venue = tk.Button(self.root, text="Modify Venue", command=self.modify_venue)
        self.btn_modify_venue.pack()

        self.btn_display_venues = tk.Button(self.root, text="Display Venues", command=self.display_venues)
        self.btn_display_venues.pack()

        # Guest buttons
        self.btn_add_guest = tk.Button(self.root, text="Add Guest", command=self.add_guest)
        self.btn_add_guest.pack()

        self.btn_delete_guest = tk.Button(self.root, text="Delete Guest", command=self.delete_guest)
        self.btn_delete_guest.pack()

        self.btn_modify_guest = tk.Button(self.root, text="Modify Guest", command=self.modify_guest)
        self.btn_modify_guest.pack()

        self.btn_display_guests = tk.Button(self.root, text="Display Guests", command=self.display_guests)
        self.btn_display_guests.pack()

    def load_data(self):
        try:
            with open("events_data.pkl", "rb") as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = []

        try:
            with open("clients_data.pkl", "rb") as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = []

        try:
            with open("suppliers_data.pkl", "rb") as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = []

        try:
            with open("employees_data.pkl", "rb") as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []

        try:
            with open("venues_data.pkl", "rb") as file:
                self.venues = pickle.load(file)
        except FileNotFoundError:
            self.venues = []

        try:
            with open("guests_data.pkl", "rb") as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = []

    def save_data(self):
        with open("events_data.pkl", "wb") as file:
            pickle.dump(self.events, file)

        with open("clients_data.pkl", "wb") as file:
            pickle.dump(self.clients, file)

        with open("suppliers_data.pkl", "wb") as file:
            pickle.dump(self.suppliers, file)

        with open("employees_data.pkl", "wb") as file:
            pickle.dump(self.employees, file)

        with open("venues_data.pkl", "wb") as file:
            pickle.dump(self.venues, file)

        with open("guests_data.pkl", "wb") as file:
            pickle.dump(self.guests, file)

    # Event functions
    def add_event(self):
        event_name = simpledialog.askstring("Event Name", "Enter event name:")
        if event_name:
            self.events.append(event_name)
            self.save_data()
            messagebox.showinfo("Success", f"Event '{event_name}' added successfully!")

    def delete_event(self):
        pass

    def modify_event(self):
        pass

    def display_events(self):
        if self.events:
            messagebox.showinfo("Events", "\n".join(self.events))
        else:
            messagebox.showinfo("Events", "No events found!")

    # Client functions
    def add_client(self):
        client_name = simpledialog.askstring("Client Name", "Enter client name:")
        if client_name:
            self.clients.append(client_name)
            self.save_data()
            messagebox.showinfo("Success", f"Client '{client_name}' added successfully!")

    def delete_client(self):
        pass

    def modify_client(self):
        pass

    def display_clients(self):
        if self.clients:
            messagebox.showinfo("Clients", "\n".join(self.clients))
        else:
            messagebox.showinfo("Clients", "No clients found!")

    # Supplier functions
    def add_supplier(self):
        supplier_name = simpledialog.askstring("Supplier Name", "Enter supplier name:")
        if supplier_name:
            self.suppliers.append(supplier_name)
            self.save_data()
            messagebox.showinfo("Success", f"Supplier '{supplier_name}' added successfully!")

    def delete_supplier(self):
        pass

    def modify_supplier(self):
        pass

    def display_suppliers(self):
        if self.suppliers:
            messagebox.showinfo("Suppliers", "\n".join(self.suppliers))
        else:
            messagebox.showinfo("Suppliers", "No suppliers found!")

    # Employee functions
    def add_employee(self):
        employee_name = simpledialog.askstring("Employee Name", "Enter employee name:")
        if employee_name:
            self.employees.append(employee_name)
            self.save_data()
            messagebox.showinfo("Success", f"Employee '{employee_name}' added successfully!")

    def delete_employee(self):
        pass

    def modify_employee(self):
        pass

    def display_employees(self):
        if self.employees:
            messagebox.showinfo("Employees", "\n".join(self.employees))
        else:
            messagebox.showinfo("Employees", "No employees found!")

    # Venue functions
    def add_venue(self):
        venue_name = simpledialog.askstring("Venue Name", "Enter venue name:")
        if venue_name:
            self.venues.append(venue_name)
            self.save_data()
            messagebox.showinfo("Success", f"Venue '{venue_name}' added successfully!")

    def delete_venue(self):
        pass

    def modify_venue(self):
        pass

    def display_venues(self):
        if self.venues:
            messagebox.showinfo("Venues", "\n".join(self.venues))
        else:
            messagebox.showinfo("Venues", "No venues found!")

    # Guest functions
    def add_guest(self):
        guest_name = simpledialog.askstring("Guest Name", "Enter guest name:")
        if guest_name:
            self.guests.append(guest_name)
            self.save_data()
            messagebox.showinfo("Success", f"Guest '{guest_name}' added successfully!")

    def delete_guest(self):
        pass

    def modify_guest(self):
        pass

    def display_guests(self):
        if self.guests:
            messagebox.showinfo("Guests", "\n".join(self.guests))
        else:
            messagebox.showinfo("Guests", "No guests found!")


if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementGUI(root)
    root.mainloop()

