

from ClassEmployee1 import ClassEmployee

class ClassManager(ClassEmployee):
    def __init__(self, manager_id, employee_id, name, department, job_title, salary, age, birthday_date, passport_details):
        super().__init__(employee_id, name, department, job_title, salary, age, birthday_date, passport_details)
        self._manager_id = manager_id

    # Getter and setter methods for manager_id
    def get_manager_id(self):
        return self._manager_id

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id