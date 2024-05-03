

class ClassCompany:
    def __init__(self, company_id, name, address, contact_details):
        self._company_id = company_id
        self._name = name
        self._address = address
        self._contact_details = contact_details

    # Getter and setter methods for company_id
    def get_company_id(self):
        return self._company_id

    def set_company_id(self, company_id):
        self._company_id = company_id

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