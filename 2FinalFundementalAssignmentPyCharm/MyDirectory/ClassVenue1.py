

class ClassVenue:
    def __init__(self, venue_id, name, address, contact_details, min_guests, max_guests):
        self._venue_id = venue_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._min_guests = min_guests
        self._max_guests = max_guests

    # Getter and setter methods for venue_id
    def get_venue_id(self):
        return self._venue_id

    def set_venue_id(self, venue_id):
        self._venue_id = venue_id

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

    # Getter and setter methods for min_guests
    def get_min_guests(self):
        return self._min_guests

    def set_min_guests(self, min_guests):
        self._min_guests = min_guests

    # Getter and setter methods for max_guests
    def get_max_guests(self):
        return self._max_guests

    def set_max_guests(self, max_guests):
        self._max_guests = max_guests