

class ClassEmployee:
    def __init__(self, employee_id, name, department, job_title, salary, age, birthday_date, passport_details):
        self._employee_id = employee_id
        self._name = name
        self._department = department
        self._job_title = job_title
        self._salary = salary
        self._age = age
        self._birthday_date = birthday_date
        self._passport_details = passport_details

    # Getter and setter methods for employee_id
    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    # Getter and setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for department
    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    # Getter and setter methods for job_title
    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    # Getter and setter methods for salary
    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    # Getter and setter methods for age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Getter and setter methods for birthday_date
    def get_birthday_date(self):
        return self._birthday_date

    def set_birthday_date(self, birthday_date):
        self._birthday_date = birthday_date

    # Getter and setter methods for passport_details
    def get_passport_details(self):
        return self._passport_details

    def set_passport_details(self, passport_details):
        self._passport_details = passport_details