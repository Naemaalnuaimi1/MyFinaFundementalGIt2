
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EventManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")

        # Create a frame to hold the GUI elements
        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        # Label and dropdown menu for entity selection
        tk.Label(frame, text="Select Entity:").grid(row=0, column=0, padx=5, pady=5)
        self.entity_var = tk.StringVar()
        self.entity_dropdown = ttk.Combobox(frame, textvariable=self.entity_var, values=["Event", "Employee", "Venue", "Supplier", "Guest", "Client"])
        self.entity_dropdown.grid(row=0, column=1, padx=5, pady=5)
        self.entity_dropdown.bind("<<ComboboxSelected>>", self.show_entity_fields)

        # Frame to hold entity-specific fields
        self.entity_frame = tk.Frame(frame)
        self.entity_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Data repositories for entities
        self.events = []
        self.employees = []
        self.venues = []
        self.suppliers = []
        self.guests = []
        self.clients = []

    def show_entity_fields(self, event=None):
        # Clear the entity frame
        for widget in self.entity_frame.winfo_children():
            widget.destroy()

        entity = self.entity_var.get()

        if entity == "Event":
            self.create_event_fields()
        elif entity == "Employee":
            self.create_employee_fields()
        elif entity == "Venue":
            self.create_venue_fields()
        elif entity == "Supplier":
            self.create_supplier_fields()
        elif entity == "Guest":
            self.create_guest_fields()
        elif entity == "Client":
            self.create_client_fields()

    def create_event_fields(self):
        # Labels and entry fields for Event attributes
        tk.Label(self.entity_frame, text="Event ID:").grid(row=0, column=0, padx=5, pady=5)
        self.event_id_entry = tk.Entry(self.entity_frame)
        self.event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Event Type:").grid(row=1, column=0, padx=5, pady=5)
        self.event_type_entry = tk.Entry(self.entity_frame)
        self.event_type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Event Theme:").grid(row=2, column=0, padx=5, pady=5)
        self.event_theme_entry = tk.Entry(self.entity_frame)
        self.event_theme_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Event Date:").grid(row=3, column=0, padx=5, pady=5)
        self.event_date_entry = tk.Entry(self.entity_frame)
        self.event_date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Event Time:").grid(row=4, column=0, padx=5, pady=5)
        self.event_time_entry = tk.Entry(self.entity_frame)
        self.event_time_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Event Duration:").grid(row=5, column=0, padx=5, pady=5)
        self.event_duration_entry = tk.Entry(self.entity_frame)
        self.event_duration_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Event Venue:").grid(row=6, column=0, padx=5, pady=5)
        self.event_venue_entry = tk.Entry(self.entity_frame)
        self.event_venue_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Client ID:").grid(row=7, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(self.entity_frame)
        self.client_id_entry.grid(row=7, column=1, padx=5, pady=5)

        # Buttons for CRUD operations
        add_button = tk.Button(self.entity_frame, text="Add Event", command=self.add_event)
        add_button.grid(row=8, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.entity_frame, text="Delete Event", command=self.delete_event)
        delete_button.grid(row=9, column=0, columnspan=2, pady=10)

        modify_button = tk.Button(self.entity_frame, text="Modify Event", command=self.modify_event)
        modify_button.grid(row=10, column=0, columnspan=2, pady=10)

        display_button = tk.Button(self.entity_frame, text="Display Events", command=self.display_events)
        display_button.grid(row=11, column=0, columnspan=2, pady=10)

    def create_employee_fields(self):
        # Labels and entry fields for Employee attributes
        tk.Label(self.entity_frame, text="Employee ID:").grid(row=0, column=0, padx=5, pady=5)
        self.employee_id_entry = tk.Entry(self.entity_frame)
        self.employee_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Employee Name:").grid(row=1, column=0, padx=5, pady=5)
        self.employee_name_entry = tk.Entry(self.entity_frame)
        self.employee_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Employee Role:").grid(row=2, column=0, padx=5, pady=5)
        self.employee_role_entry = tk.Entry(self.entity_frame)
        self.employee_role_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Employee Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.employee_contact_entry = tk.Entry(self.entity_frame)
        self.employee_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for CRUD operations
        add_button = tk.Button(self.entity_frame, text="Add Employee", command=self.add_employee)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.entity_frame, text="Delete Employee", command=self.delete_employee)
        delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        modify_button = tk.Button(self.entity_frame, text="Modify Employee", command=self.modify_employee)
        modify_button.grid(row=6, column=0, columnspan=2, pady=10)

        display_button = tk.Button(self.entity_frame, text="Display Employees", command=self.display_employees)
        display_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_venue_fields(self):
        # Labels and entry fields for Venue attributes
        tk.Label(self.entity_frame, text="Venue ID:").grid(row=0, column=0, padx=5, pady=5)
        self.venue_id_entry = tk.Entry(self.entity_frame)
        self.venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Venue Name:").grid(row=1, column=0, padx=5, pady=5)
        self.venue_name_entry = tk.Entry(self.entity_frame)
        self.venue_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Venue Location:").grid(row=2, column=0, padx=5, pady=5)
        self.venue_location_entry = tk.Entry(self.entity_frame)
        self.venue_location_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Venue Capacity:").grid(row=3, column=0, padx=5, pady=5)
        self.venue_capacity_entry = tk.Entry(self.entity_frame)
        self.venue_capacity_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for CRUD operations
        add_button = tk.Button(self.entity_frame, text="Add Venue", command=self.add_venue)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.entity_frame, text="Delete Venue", command=self.delete_venue)
        delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        modify_button = tk.Button(self.entity_frame, text="Modify Venue", command=self.modify_venue)
        modify_button.grid(row=6, column=0, columnspan=2, pady=10)

        display_button = tk.Button(self.entity_frame, text="Display Venues", command=self.display_venues)
        display_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_supplier_fields(self):
        # Labels and entry fields for Supplier attributes
        tk.Label(self.entity_frame, text="Supplier ID:").grid(row=0, column=0, padx=5, pady=5)
        self.supplier_id_entry = tk.Entry(self.entity_frame)
        self.supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Supplier Name:").grid(row=1, column=0, padx=5, pady=5)
        self.supplier_name_entry = tk.Entry(self.entity_frame)
        self.supplier_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Supplier Service:").grid(row=2, column=0, padx=5, pady=5)
        self.supplier_service_entry = tk.Entry(self.entity_frame)
        self.supplier_service_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Supplier Contact:").grid(row=3, column=0, padx=5, pady=5)
        self.supplier_contact_entry = tk.Entry(self.entity_frame)
        self.supplier_contact_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for CRUD operations
        add_button = tk.Button(self.entity_frame, text="Add Supplier", command=self.add_supplier)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.entity_frame, text="Delete Supplier", command=self.delete_supplier)
        delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        modify_button = tk.Button(self.entity_frame, text="Modify Supplier", command=self.modify_supplier)
        modify_button.grid(row=6, column=0, columnspan=2, pady=10)

        display_button = tk.Button(self.entity_frame, text="Display Suppliers", command=self.display_suppliers)
        display_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_guest_fields(self):
        # Labels and entry fields for Guest attributes
        tk.Label(self.entity_frame, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        self.guest_id_entry = tk.Entry(self.entity_frame)
        self.guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Guest Name:").grid(row=1, column=0, padx=5, pady=5)
        self.guest_name_entry = tk.Entry(self.entity_frame)
        self.guest_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Guest Contact:").grid(row=2, column=0, padx=5, pady=5)
        self.guest_contact_entry = tk.Entry(self.entity_frame)
        self.guest_contact_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Event ID:").grid(row=3, column=0, padx=5, pady=5)
        self.guest_event_id_entry = tk.Entry(self.entity_frame)
        self.guest_event_id_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for CRUD operations
        add_button = tk.Button(self.entity_frame, text="Add Guest", command=self.add_guest)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.entity_frame, text="Delete Guest", command=self.delete_guest)
        delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        modify_button = tk.Button(self.entity_frame, text="Modify Guest", command=self.modify_guest)
        modify_button.grid(row=6, column=0, columnspan=2, pady=10)

        display_button = tk.Button(self.entity_frame, text="Display Guests", command=self.display_guests)
        display_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_client_fields(self):
        # Labels and entry fields for Client attributes
        tk.Label(self.entity_frame, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        self.client_id_entry = tk.Entry(self.entity_frame)
        self.client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Client Name:").grid(row=1, column=0, padx=5, pady=5)
        self.client_name_entry = tk.Entry(self.entity_frame)
        self.client_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Client Contact:")
        tk.Label(self.entity_frame, text="Client Contact:").grid(row=2, column=0, padx=5, pady=5)
        self.client_contact_entry = tk.Entry(self.entity_frame)
        self.client_contact_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.entity_frame, text="Client Email:").grid(row=3, column=0, padx=5, pady=5)
        self.client_email_entry = tk.Entry(self.entity_frame)
        self.client_email_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for CRUD operations
        add_button = tk.Button(self.entity_frame, text="Add Client", command=self.add_client)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        delete_button = tk.Button(self.entity_frame, text="Delete Client", command=self.delete_client)
        delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        modify_button = tk.Button(self.entity_frame, text="Modify Client", command=self.modify_client)
        modify_button.grid(row=6, column=0, columnspan=2, pady=10)

        display_button = tk.Button(self.entity_frame, text="Display Clients", command=self.display_clients)
        display_button.grid(row=7, column=0, columnspan=2, pady=10)

    # CRUD operation methods for Event
    def add_event(self):
        event_id = self.event_id_entry.get()
        event_type = self.event_type_entry.get()
        event_theme = self.event_theme_entry.get()
        event_date = self.event_date_entry.get()
        event_time = self.event_time_entry.get()
        event_duration = self.event_duration_entry.get()
        event_venue = self.event_venue_entry.get()
        client_id = self.client_id_entry.get()

        # Implement add event logic
        event = {
            "event_id": event_id,
            "event_type": event_type,
            "event_theme": event_theme,
            "event_date": event_date,
            "event_time": event_time,
            "event_duration": event_duration,
            "event_venue": event_venue,
            "client_id": client_id
        }
        self.events.append(event)
        messagebox.showinfo("Success", "Event added successfully!")

    def delete_event(self):
        event_id = self.event_id_entry.get()
        for event in self.events:
            if event["event_id"] == event_id:
                self.events.remove(event)
                messagebox.showinfo("Success", "Event deleted successfully!")
                return
        messagebox.showerror("Error", "Event not found!")

    def modify_event(self):
        event_id = self.event_id_entry.get()
        for event in self.events:
            if event["event_id"] == event_id:
                event["event_type"] = self.event_type_entry.get()
                event["event_theme"] = self.event_theme_entry.get()
                event["event_date"] = self.event_date_entry.get()
                event["event_time"] = self.event_time_entry.get()
                event["event_duration"] = self.event_duration_entry.get()
                event["event_venue"] = self.event_venue_entry.get()
                event["client_id"] = self.client_id_entry.get()
                messagebox.showinfo("Success", "Event modified successfully!")
                return
        messagebox.showerror("Error", "Event not found!")

    def display_events(self):
        if not self.events:
            messagebox.showinfo("Info", "No events to display.")
        else:
            event_info = "\n".join([f"Event ID: {event['event_id']}, Type: {event['event_type']}, Theme: {event['event_theme']}, Date: {event['event_date']}, Time: {event['event_time']}, Duration: {event['event_duration']}, Venue: {event['event_venue']}, Client ID: {event['client_id']}" for event in self.events])
            messagebox.showinfo("Events", event_info)

    # CRUD operation methods for Employee
    def add_employee(self):
        employee_id = self.employee_id_entry.get()
        employee_name = self.employee_name_entry.get()
        employee_role = self.employee_role_entry.get()
        employee_contact = self.employee_contact_entry.get()

        # Implement add employee logic
        employee = {
            "employee_id": employee_id,
            "employee_name": employee_name,
            "employee_role": employee_role,
            "employee_contact": employee_contact
        }
        self.employees.append(employee)
        messagebox.showinfo("Success", "Employee added successfully!")

    def delete_employee(self):
        employee_id = self.employee_id_entry.get()
        for employee in self.employees:
            if employee["employee_id"] == employee_id:
                self.employees.remove(employee)
                messagebox.showinfo("Success", "Employee deleted successfully!")
                return
        messagebox.showerror("Error", "Employee not found!")

    def modify_employee(self):
        employee_id = self.employee_id_entry.get()
        for employee in self.employees:
            if employee["employee_id"] == employee_id:
                employee["employee_name"] = self.employee_name_entry.get()
                employee["employee_role"] = self.employee_role_entry.get()
                employee["employee_contact"] = self.employee_contact_entry.get()
                messagebox.showinfo("Success", "Employee modified successfully!")
                return
        messagebox.showerror("Error", "Employee not found!")

    def display_employees(self):
        if not self.employees:
            messagebox.showinfo("Info", "No employees to display.")
        else:
            employee_info = "\n".join([f"Employee ID: {employee['employee_id']}, Name: {employee['employee_name']}, Role: {employee['employee_role']}, Contact: {employee['employee_contact']}" for employee in self.employees])
            messagebox.showinfo("Employees", employee_info)

    # CRUD operation methods for Venue
    def add_venue(self):
        venue_id = self.venue_id_entry.get()
        venue_name = self.venue_name_entry.get()
        venue_location = self.venue_location_entry.get()
        venue_capacity = self.venue_capacity_entry.get()

        # Implement add venue logic
        venue = {
            "venue_id": venue_id,
            "venue_name": venue_name,
            "venue_location": venue_location,
            "venue_capacity": venue_capacity
        }
        self.venues.append(venue)
        messagebox.showinfo("Success", "Venue added successfully!")

    def delete_venue(self):
        venue_id = self.venue_id_entry.get()
        for venue in self.venues:
            if venue["venue_id"] == venue_id:
                self.venues.remove(venue)
                messagebox.showinfo("Success", "Venue deleted successfully!")
                return
        messagebox.showerror("Error", "Venue not found!")

    def modify_venue(self):
        venue_id = self.venue_id_entry.get()
        for venue in self.venues:
            if venue["venue_id"] == venue_id:
                venue["venue_name"] = self.venue_name_entry.get()
                venue["venue_location"] = self.venue_location_entry.get()
                venue["venue_capacity"] = self.venue_capacity_entry.get()
                messagebox.showinfo("Success", "Venue modified successfully!")
                return
        messagebox.showerror("Error", "Venue not found!")

    def display_venues(self):
        if not self.venues:
            messagebox.showinfo("Info", "No venues to display.")
        else:
            venue_info = "\n".join([f"Venue ID: {venue['venue_id']}, Name: {venue['venue_name']}, Location: {venue['venue_location']}, Capacity: {venue['venue_capacity']}" for venue in self.venues])
            messagebox.showinfo("Venues", venue_info)

    # CRUD operation methods for Supplier
    def add_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        supplier_name = self.supplier_name_entry.get()
        supplier_service = self.supplier_service_entry.get()
        supplier_contact = self.supplier_contact_entry.get()

        # Implement add supplier logic
        supplier = {
            "supplier_id": supplier_id,
            "supplier_name": supplier_name,
            "supplier_service": supplier_service,
            "supplier_contact": supplier_contact
        }
        self.suppliers.append(supplier)
        messagebox.showinfo("Success", "Supplier added successfully!")

    def delete_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        for supplier in self.suppliers:
            if supplier["supplier_id"] == supplier_id:
                self.suppliers.remove(supplier)
                messagebox.showinfo("Success", "Supplier deleted successfully!")
                return
        messagebox.showerror("Error", "Supplier not found!")

    def modify_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        for supplier in self.suppliers:
            if supplier["supplier_id"] == supplier_id:
                supplier["supplier_name"] = self.supplier_name_entry.get()
                supplier["supplier_service"] = self.supplier_service_entry.get()
                supplier["supplier_contact"] = self.supplier_contact_entry.get()
                messagebox.showinfo("Success", "Supplier modified successfully!")
                return
        messagebox.showerror("Error", "Supplier not found!")

    def display_suppliers(self):
        if not self.suppliers:
            messagebox.showinfo("Info", "No suppliers to display.")
        else:
            supplier_info = "\n".join([f"Supplier ID: {supplier['supplier_id']}, Name: {supplier['supplier_name']}, Service: {supplier['supplier_service']}, Contact: {supplier['supplier_contact']}" for supplier in self.suppliers])
            messagebox.showinfo("Suppliers", supplier_info)

    # CRUD operation methods for Guest
    def add_guest(self):
        guest_id = self.guest_id_entry.get()
        guest_name = self.guest_name_entry.get()
        guest_contact = self.guest_contact_entry.get()
        guest_event_id = self.guest_event_id_entry.get()

        # Implement add guest logic
        guest = {
            "guest_id": guest_id,
            "guest_name": guest_name,
            "guest_contact": guest_contact,
            "guest_event_id": guest_event_id
        }
        self.guests.append(guest)
        messagebox.showinfo("Success", "Guest added successfully!")

    def delete_guest(self):
        guest_id = self.guest_id_entry.get()
        for guest in self.guests:
            if guest["guest_id"] == guest_id:
                self.guests.remove(guest)
                messagebox.showinfo("Success", "Guest deleted successfully!")
                return
        messagebox.showerror("Error", "Guest not found!")

    def modify_guest(self):
        guest_id = self.guest_id_entry.get()
        for guest in self.guests:
            if guest["guest_id"] == guest_id:
                guest["guest_name"] = self.guest_name_entry.get()
                guest["guest_contact"] = self.guest_contact_entry.get()
                guest["guest_event_id"] = self.guest_event_id_entry.get()
                messagebox.showinfo("Success", "Guest modified successfully!")
                return
        messagebox.showerror("Error", "Guest not found!")

    def display_guests(self):
        if not self.guests:
            messagebox.showinfo("Info", "No guests to display.")
        else:
            guest_info = "\n".join([f"Guest ID: {guest['guest_id']}, Name: {guest['guest_name']}, Contact: {guest['guest_contact']}, Event ID: {guest['guest_event_id']}" for guest in self.guests])
            messagebox.showinfo("Guests", guest_info)

    # CRUD operation methods for Client
    def add_client(self):
        client_id = self.client_id_entry.get()
        client_name = self.client_name_entry.get()
        client_contact = self.client_contact_entry.get()
        client_email = self.client_email_entry.get()

        # Implement add client logic
        client = {
            "client_id": client_id,
            "client_name": client_name,
            "client_contact": client_contact,
            "client_email": client_email
        }
        self.clients.append(client)
        messagebox.showinfo("Success", "Client added successfully!")

    def delete_client(self):
        client_id = self.client_id_entry.get()
        for client in self.clients:
            if client["client_id"] == client_id:
                self.clients.remove(client)
                messagebox.showinfo("Success", "Client deleted successfully!")
                return
        messagebox.showerror("Error", "Client not found!")

    def modify_client(self):
        client_id = self.client_id_entry.get()
        for client in self.clients:
            if client["client_id"] == client_id:
                client["client_name"] = self.client_name_entry.get()
                client["client_contact"] = self.client_contact_entry.get()
                client["client_email"] = self.client_email_entry.get()
                messagebox.showinfo("Success", "Client modified successfully!")
                return
        messagebox.showerror("Error", "Client not found!")

    def display_clients(self):
        if not self.clients:
            messagebox.showinfo("Info", "No clients to display.")
        else:
            client_info = "\n".join([f"Client ID: {client['client_id']}, Name: {client['client_name']}, Contact: {client['client_contact']}, Email: {client['client_email']}" for client in self.clients])
            messagebox.showinfo("Clients", client_info)

# Create the main Tkinter window
root = tk.Tk()
app = EventManagementGUI(root)
root.mainloop()
