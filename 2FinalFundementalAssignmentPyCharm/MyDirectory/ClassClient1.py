

class ClassClient:
    def __init__(self, client_id, name, address, contact_details, budget):
        self._client_id = client_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._budget = budget

    # Getter and setter methods for client_id
    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    # Getter and setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Getter and setter methods for contact_details
    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    # Getter and setter methods for budget
    def get_budget(self):
        return self._budget

    def set_budget(self, budget):
        self._budget = budget