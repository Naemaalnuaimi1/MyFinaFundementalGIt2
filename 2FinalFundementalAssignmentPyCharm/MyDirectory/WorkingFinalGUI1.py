import tkinter as tk
from ClassEmployee1 import ClassEmployee
from ClassClient1 import ClassClient
from ClassEvent1 import ClassEvent
from ClassGuest1 import ClassGuest

class ManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Management System")

        self.label = tk.Label(master, text="Management System")
        self.label.pack()

        self.employee_button = tk.Button(master, text="Employee Management", command=self.employee_management)
        self.employee_button.pack()

        self.client_button = tk.Button(master, text="Client Management", command=self.client_management)
        self.client_button.pack()

        self.event_button = tk.Button(master, text="Event Management", command=self.event_management)
        self.event_button.pack()

        self.guest_button = tk.Button(master, text="Guest Management", command=self.guest_management)
        self.guest_button.pack()

        self.employee_list = []
        self.client_list = []
        self.event_list = []
        self.guest_list = []

    def employee_management(self):
        self.employee_window = tk.Toplevel(self.master)
        self.employee_window.title("Employee Management")

        self.employee_label = tk.Label(self.employee_window, text="Employee Management")
        self.employee_label.pack()

        self.add_emp_button = tk.Button(self.employee_window, text="Add Employee", command=self.add_employee)
        self.add_emp_button.pack()

        self.display_emp_button = tk.Button(self.employee_window, text="Display Employees", command=self.display_employees)
        self.display_emp_button.pack()

        self.delete_emp_button = tk.Button(self.employee_window, text="Delete Employee", command=self.delete_employee)
        self.delete_emp_button.pack()

        self.modify_emp_button = tk.Button(self.employee_window, text="Modify Employee", command=self.modify_employee)
        self.modify_emp_button.pack()


    def add_employee(self):
        self.add_emp_window = tk.Toplevel(self.employee_window)
        self.add_emp_window.title("Add Employee")

        # Create entry fields
        tk.Label(self.add_emp_window, text="Employee ID:").grid(row=0, column=0)
        self.emp_id_entry = tk.Entry(self.add_emp_window)
        self.emp_id_entry.grid(row=0, column=1)

        tk.Label(self.add_emp_window, text="Name:").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.add_emp_window)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.add_emp_window, text="Department:").grid(row=2, column=0)
        self.dept_entry = tk.Entry(self.add_emp_window)
        self.dept_entry.grid(row=2, column=1)

        tk.Label(self.add_emp_window, text="Job Title:").grid(row=3, column=0)
        self.job_title_entry = tk.Entry(self.add_emp_window)
        self.job_title_entry.grid(row=3, column=1)

        tk.Label(self.add_emp_window, text="Salary:").grid(row=4, column=0)
        self.salary_entry = tk.Entry(self.add_emp_window)
        self.salary_entry.grid(row=4, column=1)

        tk.Label(self.add_emp_window, text="Age:").grid(row=5, column=0)
        self.age_entry = tk.Entry(self.add_emp_window)
        self.age_entry.grid(row=5, column=1)

        tk.Label(self.add_emp_window, text="Birthday Date:").grid(row=6, column=0)
        self.birthday_entry = tk.Entry(self.add_emp_window)
        self.birthday_entry.grid(row=6, column=1)

        tk.Label(self.add_emp_window, text="Passport Details:").grid(row=7, column=0)
        self.passport_entry = tk.Entry(self.add_emp_window)
        self.passport_entry.grid(row=7, column=1)

        # Add employee button
        tk.Button(self.add_emp_window, text="Add", command=self.save_employee).grid(row=8, columnspan=2)

    def save_employee(self):
        employee_id = self.emp_id_entry.get()
        name = self.name_entry.get()
        department = self.dept_entry.get()
        job_title = self.job_title_entry.get()
        salary = self.salary_entry.get()
        age = self.age_entry.get()
        birthday_date = self.birthday_entry.get()
        passport_details = self.passport_entry.get()

        new_employee = ClassEmployee(employee_id, name, department, job_title, salary, age, birthday_date, passport_details)
        self.employee_list.append(new_employee)

        # Save the employee to a database or perform necessary operations

        self.add_emp_window.destroy()

    def display_employees(self):
        self.display_emp_window = tk.Toplevel(self.employee_window)
        self.display_emp_window.title("Display Employees")

        for i, employee in enumerate(self.employee_list):
            tk.Label(self.display_emp_window, text=f"Employee {i+1}: {employee.get_name()}").pack()

    def delete_employee(self):
        self.delete_emp_window = tk.Toplevel(self.employee_window)
        self.delete_emp_window.title("Delete Employee")

        tk.Label(self.delete_emp_window, text="Enter Employee ID to Delete:").pack()
        self.del_emp_entry = tk.Entry(self.delete_emp_window)
        self.del_emp_entry.pack()

        tk.Button(self.delete_emp_window, text="Delete", command=self.delete_emp_confirm).pack()

    def delete_emp_confirm(self):
        del_emp_id = self.del_emp_entry.get()
        for employee in self.employee_list:
            if employee.get_employee_id() == del_emp_id:
                self.employee_list.remove(employee)
                break

        self.delete_emp_window.destroy()

    def modify_employee(self):
        self.modify_emp_window = tk.Toplevel(self.employee_window)
        self.modify_emp_window.title("Modify Employee")

        tk.Label(self.modify_emp_window, text="Enter Employee ID to Modify:").pack()
        self.mod_emp_entry = tk.Entry(self.modify_emp_window)
        self.mod_emp_entry.pack()

        tk.Button(self.modify_emp_window, text="Modify", command=self.modify_emp_fields).pack()

    def modify_emp_fields(self):
        mod_emp_id = self.mod_emp_entry.get()
        for employee in self.employee_list:
            if employee.get_employee_id() == mod_emp_id:
                self.mod_emp = employee
                break

        # Create entry fields with existing employee data for modification
        tk.Label(self.modify_emp_window, text="Name:").pack()
        self.mod_name_entry = tk.Entry(self.modify_emp_window)
        self.mod_name_entry.insert(0, self.mod_emp.get_name())
        self.mod_name_entry.pack()

        tk.Label(self.modify_emp_window, text="Department:").pack()
        self.mod_dept_entry = tk.Entry(self.modify_emp_window)
        self.mod_dept_entry.insert(0, self.mod_emp.get_department())
        self.mod_dept_entry.pack()

        tk.Label(self.modify_emp_window, text="Job Title:").pack()
        self.mod_job_title_entry = tk.Entry(self.modify_emp_window)
        self.mod_job_title_entry.insert(0, self.mod_emp.get_job_title())
        self.mod_job_title_entry.pack()

        tk.Label(self.modify_emp_window, text="Salary:").pack()
        self.mod_salary_entry = tk.Entry(self.modify_emp_window)
        self.mod_salary_entry.insert(0, self.mod_emp.get_salary())
        self.mod_salary_entry.pack()

        tk.Label(self.modify_emp_window, text="Age:").pack()
        self.mod_age_entry = tk.Entry(self.modify_emp_window)
        self.mod_age_entry.insert(0, self.mod_emp.get_age())
        self.mod_age_entry.pack()

        tk.Label(self.modify_emp_window, text="Birthday Date:").pack()
        self.mod_birthday_entry = tk.Entry(self.modify_emp_window)
        self.mod_birthday_entry.insert(0, self.mod_emp.get_birthday_date())
        self.mod_birthday_entry.pack()

        tk.Label(self.modify_emp_window, text="Passport Details:").pack()
        self.mod_passport_entry = tk.Entry(self.modify_emp_window)
        self.mod_passport_entry.insert(0, self.mod_emp.get_passport_details())
        self.mod_passport_entry.pack()

        # Modify employee button
        tk.Button(self.modify_emp_window, text="Save Changes", command=self.save_modified_employee).pack()

    def save_modified_employee(self):
        self.mod_emp.set_name(self.mod_name_entry.get())
        self.mod_emp.set_department(self.mod_dept_entry.get())
        self.mod_emp.set_job_title(self.mod_job_title_entry.get())
        self.mod_emp.set_salary(self.mod_salary_entry.get())
        self.mod_emp.set_age(self.mod_age_entry.get())
        self.mod_emp.set_birthday_date(self.mod_birthday_entry.get())
        self.mod_emp.set_passport_details(self.mod_passport_entry.get())

        self.modify_emp_window.destroy()
    def client_management(self):
        self.client_window = tk.Toplevel(self.master)
        self.client_window.title("Client Management")

        self.client_label = tk.Label(self.client_window, text="Client Management")
        self.client_label.pack()

        self.add_client_button = tk.Button(self.client_window, text="Add Client", command=self.add_client)
        self.add_client_button.pack()

        self.display_client_button = tk.Button(self.client_window, text="Display Clients", command=self.display_clients)
        self.display_client_button.pack()

        self.delete_client_button = tk.Button(self.client_window, text="Delete Client", command=self.delete_client)
        self.delete_client_button.pack()

        self.modify_client_button = tk.Button(self.client_window, text="Modify Client", command=self.modify_client)
        self.modify_client_button.pack()


    def add_client(self):
        self.add_client_window = tk.Toplevel(self.client_window)
        self.add_client_window.title("Add Client")

        # Create entry fields
        tk.Label(self.add_client_window, text="Client ID:").grid(row=0, column=0)
        self.client_id_entry = tk.Entry(self.add_client_window)
        self.client_id_entry.grid(row=0, column=1)

        tk.Label(self.add_client_window, text="Name:").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.add_client_window)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.add_client_window, text="Address:").grid(row=2, column=0)
        self.address_entry = tk.Entry(self.add_client_window)
        self.address_entry.grid(row=2, column=1)

        tk.Label(self.add_client_window, text="Contact Details:").grid(row=3, column=0)
        self.contact_details_entry = tk.Entry(self.add_client_window)
        self.contact_details_entry.grid(row=3, column=1)

        tk.Label(self.add_client_window, text="Budget:").grid(row=4, column=0)
        self.budget_entry = tk.Entry(self.add_client_window)
        self.budget_entry.grid(row=4, column=1)

        # Add client button
        tk.Button(self.add_client_window, text="Add", command=self.save_client).grid(row=5, columnspan=2)

    def save_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()

        new_client = ClassClient(client_id, name, address, contact_details, budget)
        self.client_list.append(new_client)

        # Save the client to a database or perform necessary operations

        self.add_client_window.destroy()

    def display_clients(self):
        self.display_client_window = tk.Toplevel(self.client_window)
        self.display_client_window.title("Display Clients")

        for i, client in enumerate(self.client_list):
            tk.Label(self.display_client_window, text=f"Client {i+1}: {client.get_name()}").pack()

    def delete_client(self):
        self.delete_client_window = tk.Toplevel(self.client_window)
        self.delete_client_window.title("Delete Client")

        tk.Label(self.delete_client_window, text="Enter Client ID to Delete:").pack()
        self.del_client_entry = tk.Entry(self.delete_client_window)
        self.del_client_entry.pack()

        tk.Button(self.delete_client_window, text="Delete", command=self.delete_client_confirm).pack()

    def delete_client_confirm(self):
        del_client_id = self.del_client_entry.get()
        for client in self.client_list:
            if client.get_client_id() == del_client_id:
                self.client_list.remove(client)
                break

        self.delete_client_window.destroy()

    def modify_client(self):
        self.modify_client_window = tk.Toplevel(self.client_window)
        self.modify_client_window.title("Modify Client")

        tk.Label(self.modify_client_window, text="Enter Client ID to Modify:").pack()
        self.mod_client_entry = tk.Entry(self.modify_client_window)
        self.mod_client_entry.pack()

        tk.Button(self.modify_client_window, text="Modify", command=self.modify_client_fields).pack()

    def modify_client_fields(self):
        mod_client_id = self.mod_client_entry.get()
        for client in self.client_list:
            if client.get_client_id() == mod_client_id:
                self.mod_client = client
                break

        # Create entry fields with existing client data for modification
        tk.Label(self.modify_client_window, text="Name:").pack()
        self.mod_name_entry = tk.Entry(self.modify_client_window)
        self.mod_name_entry.insert(0, self.mod_client.get_name())
        self.mod_name_entry.pack()

        tk.Label(self.modify_client_window, text="Address:").pack()
        self.mod_address_entry = tk.Entry(self.modify_client_window)
        self.mod_address_entry.insert(0, self.mod_client.get_address())
        self.mod_address_entry.pack()

        tk.Label(self.modify_client_window, text="Contact Details:").pack()
        self.mod_contact_details_entry = tk.Entry(self.modify_client_window)
        self.mod_contact_details_entry.insert(0, self.mod_client.get_contact_details())
        self.mod_contact_details_entry.pack()

        tk.Label(self.modify_client_window, text="Budget:").pack()
        self.mod_budget_entry = tk.Entry(self.modify_client_window)
        self.mod_budget_entry.insert(0, self.mod_client.get_budget())
        self.mod_budget_entry.pack()

        # Modify client button
        tk.Button(self.modify_client_window, text="Save Changes", command=self.save_modified_client).pack()

    def save_modified_client(self):
        self.mod_client.set_name(self.mod_name_entry.get())
        self.mod_client.set_address(self.mod_address_entry.get())
        self.mod_client.set_contact_details(self.mod_contact_details_entry.get())
        self.mod_client.set_budget(self.mod_budget_entry.get())

        self.modify_client_window.destroy()

    def event_management(self):
        self.event_window = tk.Toplevel(self.master)
        self.event_window.title("Event Management")

        self.event_label = tk.Label(self.event_window, text="Event Management")
        self.event_label.pack()

        self.add_event_button = tk.Button(self.event_window, text="Add Event", command=self.add_event)
        self.add_event_button.pack()

        self.display_event_button = tk.Button(self.event_window, text="Display Events", command=self.display_events)
        self.display_event_button.pack()

        self.delete_event_button = tk.Button(self.event_window, text="Delete Event", command=self.delete_event)
        self.delete_event_button.pack()

        self.modify_event_button = tk.Button(self.event_window, text="Modify Event", command=self.modify_event)
        self.modify_event_button.pack()

    def event_management(self):
        self.event_window = tk.Toplevel(self.master)
        self.event_window.title("Event Management")

        self.event_label = tk.Label(self.event_window, text="Event Management")
        self.event_label.pack()

        self.add_event_button = tk.Button(self.event_window, text="Add Event", command=self.add_event)
        self.add_event_button.pack()

        self.display_event_button = tk.Button(self.event_window, text="Display Events", command=self.display_events)
        self.display_event_button.pack()

        self.delete_event_button = tk.Button(self.event_window, text="Delete Event", command=self.delete_event)
        self.delete_event_button.pack()

        self.modify_event_button = tk.Button(self.event_window, text="Modify Event", command=self.modify_event)
        self.modify_event_button.pack()

    def add_event(self):
        self.add_event_window = tk.Toplevel(self.event_window)
        self.add_event_window.title("Add Event")

        # Create entry fields
        tk.Label(self.add_event_window, text="Event ID:").grid(row=0, column=0)
        self.event_id_entry = tk.Entry(self.add_event_window)
        self.event_id_entry.grid(row=0, column=1)

        tk.Label(self.add_event_window, text="Type:").grid(row=1, column=0)
        self.type_entry = tk.Entry(self.add_event_window)
        self.type_entry.grid(row=1, column=1)

        tk.Label(self.add_event_window, text="Theme:").grid(row=2, column=0)
        self.theme_entry = tk.Entry(self.add_event_window)
        self.theme_entry.grid(row=2, column=1)

        tk.Label(self.add_event_window, text="Date:").grid(row=3, column=0)
        self.date_entry = tk.Entry(self.add_event_window)
        self.date_entry.grid(row=3, column=1)

        tk.Label(self.add_event_window, text="Time:").grid(row=4, column=0)
        self.time_entry = tk.Entry(self.add_event_window)
        self.time_entry.grid(row=4, column=1)

        tk.Label(self.add_event_window, text="Duration:").grid(row=5, column=0)
        self.duration_entry = tk.Entry(self.add_event_window)
        self.duration_entry.grid(row=5, column=1)

        tk.Label(self.add_event_window, text="Venue Address:").grid(row=6, column=0)
        self.venue_entry = tk.Entry(self.add_event_window)
        self.venue_entry.grid(row=6, column=1)

        tk.Label(self.add_event_window, text="Client ID:").grid(row=7, column=0)
        self.client_id_entry = tk.Entry(self.add_event_window)
        self.client_id_entry.grid(row=7, column=1)

        tk.Label(self.add_event_window, text="Guest List:").grid(row=8, column=0)
        self.guest_list_entry = tk.Entry(self.add_event_window)
        self.guest_list_entry.grid(row=8, column=1)

        tk.Label(self.add_event_window, text="Catering Company:").grid(row=9, column=0)
        self.catering_company_entry = tk.Entry(self.add_event_window)
        self.catering_company_entry.grid(row=9, column=1)

        tk.Label(self.add_event_window, text="Decoration Company:").grid(row=10, column=0)
        self.decoration_company_entry = tk.Entry(self.add_event_window)
        self.decoration_company_entry.grid(row=10, column=1)

        tk.Label(self.add_event_window, text="Entertainment Company:").grid(row=11, column=0)
        self.entertainment_company_entry = tk.Entry(self.add_event_window)
        self.entertainment_company_entry.grid(row=11, column=1)

        tk.Label(self.add_event_window, text="Furniture Company:").grid(row=12, column=0)
        self.furniture_company_entry = tk.Entry(self.add_event_window)
        self.furniture_company_entry.grid(row=12, column=1)

        tk.Label(self.add_event_window, text="Invoice:").grid(row=13, column=0)
        self.invoice_entry = tk.Entry(self.add_event_window)
        self.invoice_entry.grid(row=13, column=1)

        # Add event button
        tk.Button(self.add_event_window, text="Add", command=self.save_event).grid(row=14, columnspan=2)

    def save_event(self):
        event_id = self.event_id_entry.get()
        type = self.type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_address = self.venue_entry.get()
        client_id = self.client_id_entry.get()
        guest_list = self.guest_list_entry.get()
        catering_company = self.catering_company_entry.get()
        decoration_company = self.decoration_company_entry.get()
        entertainment_company = self.entertainment_company_entry.get()
        furniture_company = self.furniture_company_entry.get()
        invoice = self.invoice_entry.get()

        new_event = ClassEvent(event_id, type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, decoration_company, entertainment_company, furniture_company, invoice)
        self.event_list.append(new_event)

        # Save the event to a database or perform necessary operations

        self.add_event_window.destroy()

    def display_events(self):
        self.display_event_window = tk.Toplevel(self.event_window)
        self.display_event_window.title("Display Events")

        for i, event in enumerate(self.event_list):
            tk.Label(self.display_event_window, text=f"Event {i+1}: {event.get_theme()}").pack()

    def delete_event(self):
        self.delete_event_window = tk.Toplevel(self.event_window)
        self.delete_event_window.title("Delete Event")

        tk.Label(self.delete_event_window, text="Enter Event ID to Delete:").pack()
        self.del_event_entry = tk.Entry(self.delete_event_window)
        self.del_event_entry.pack()

        tk.Button(self.delete_event_window, text="Delete", command=self.delete_event_confirm).pack()

    def delete_event_confirm(self):
        del_event_id = self.del_event_entry.get()
        for event in self.event_list:
            if event.get_event_id() == del_event_id:
                self.event_list.remove(event)
                break

        self.delete_event_window.destroy()

    def modify_event(self):
        self.modify_event_window = tk.Toplevel(self.event_window)
        self.modify_event_window.title("Modify Event")

        tk.Label(self.modify_event_window, text="Enter Event ID to Modify:").pack()
        self.mod_event_entry = tk.Entry(self.modify_event_window)
        self.mod_event_entry.pack()

        tk.Button(self.modify_event_window, text="Modify", command=self.modify_event_fields).pack()

    def modify_event_fields(self):
        mod_event_id = self.mod_event_entry.get()
        for event in self.event_list:
            if event.get_event_id() == mod_event_id:
                self.mod_event = event
                break

    def guest_management(self):
        self.guest_window = tk.Toplevel(self.master)
        self.guest_window.title("Guest Management")

        self.guest_label = tk.Label(self.guest_window, text="Guest Management")
        self.guest_label.pack()

        self.add_guest_button = tk.Button(self.guest_window, text="Add Guest", command=self.add_guest)
        self.add_guest_button.pack()

        self.display_guest_button = tk.Button(self.guest_window, text="Display Guests", command=self.display_guests)
        self.display_guest_button.pack()

        self.delete_guest_button = tk.Button(self.guest_window, text="Delete Guest", command=self.delete_guest)
        self.delete_guest_button.pack()

        self.modify_guest_button = tk.Button(self.guest_window, text="Modify Guest", command=self.modify_guest)
        self.modify_guest_button.pack()

    def add_guest(self):
        self.add_guest_window = tk.Toplevel(self.guest_window)
        self.add_guest_window.title("Add Guest")

        # Create entry fields
        tk.Label(self.add_guest_window, text="Guest ID:").grid(row=0, column=0)
        self.guest_id_entry = tk.Entry(self.add_guest_window)
        self.guest_id_entry.grid(row=0, column=1)

        tk.Label(self.add_guest_window, text="Name:").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.add_guest_window)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.add_guest_window, text="Address:").grid(row=2, column=0)
        self.address_entry = tk.Entry(self.add_guest_window)
        self.address_entry.grid(row=2, column=1)

        tk.Label(self.add_guest_window, text="Contact Details:").grid(row=3, column=0)
        self.contact_details_entry = tk.Entry(self.add_guest_window)
        self.contact_details_entry.grid(row=3, column=1)

        # Add guest button
        tk.Button(self.add_guest_window, text="Add", command=self.save_guest).grid(row=4, columnspan=2)

    def save_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()

        new_guest = ClassGuest(guest_id, name, address, contact_details)
        self.guest_list.append(new_guest)

        # Save the guest to a database or perform necessary operations

        self.add_guest_window.destroy()

    def display_guests(self):
        self.display_guest_window = tk.Toplevel(self.guest_window)
        self.display_guest_window.title("Display Guests")

        for i, guest in enumerate(self.guest_list):
            tk.Label(self.display_guest_window, text=f"Guest {i+1}: {guest.get_name()}").pack()

    def delete_guest(self):
        self.delete_guest_window = tk.Toplevel(self.guest_window)
        self.delete_guest_window.title("Delete Guest")

        tk.Label(self.delete_guest_window, text="Enter Guest ID to Delete:").pack()
        self.del_guest_entry = tk.Entry(self.delete_guest_window)
        self.del_guest_entry.pack()

        tk.Button(self.delete_guest_window, text="Delete", command=self.delete_guest_confirm).pack()

    def delete_guest_confirm(self):
        del_guest_id = self.del_guest_entry.get()
        for guest in self.guest_list:
            if guest.get_guest_id() == del_guest_id:
                self.guest_list.remove(guest)
                break

        self.delete_guest_window.destroy()

    def modify_guest(self):
        self.modify_guest_window = tk.Toplevel(self.guest_window)
        self.modify_guest_window.title("Modify Guest")

        tk.Label(self.modify_guest_window, text="Enter Guest ID to Modify:").pack()
        self.mod_guest_entry = tk.Entry(self.modify_guest_window)
        self.mod_guest_entry.pack()

        tk.Button(self.modify_guest_window, text="Modify", command=self.modify_guest_fields).pack()

    def modify_guest_fields(self):
        mod_guest_id = self.mod_guest_entry.get()
        for guest in self.guest_list:
            if guest.get_guest_id() == mod_guest_id:
                self.mod_guest = guest
                break

        # Create entry fields with existing guest data for modification
        tk.Label(self.modify_guest_window, text="Name:").pack()
        self.mod_name_entry = tk.Entry(self.modify_guest_window)
        self.mod_name_entry.insert(0, self.mod_guest.get_name())
        self.mod_name_entry.pack()

        tk.Label(self.modify_guest_window, text="Address:").pack()
        self.mod_address_entry = tk.Entry(self.modify_guest_window)
        self.mod_address_entry.insert(0, self.mod_guest.get_address())
        self.mod_address_entry.pack()

        tk.Label(self.modify_guest_window, text="Contact Details:").pack()
        self.mod_contact_details_entry = tk.Entry(self.modify_guest_window)
        self.mod_contact_details_entry.insert(0, self.mod_guest.get_contact_details())
        self.mod_contact_details_entry.pack()

        # Modify guest button
        tk.Button(self.modify_guest_window, text="Save Changes", command=self.save_modified_guest).pack()

    def save_modified_guest(self):
        self.mod_guest.set_name(self.mod_name_entry.get())
        self.mod_guest.set_address(self.mod_address_entry.get())
        self.mod_guest.set_contact_details(self.mod_contact_details_entry.get())

        self.modify_guest_window.destroy()

def main():
    root = tk.Tk()
    app = ManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()