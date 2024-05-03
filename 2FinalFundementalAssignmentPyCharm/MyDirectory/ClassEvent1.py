

class ClassEvent:
    def __init__(self, event_id, type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, decoration_company, entertainment_company, furniture_company, invoice):
        self._event_id = event_id
        self._type = type
        self._theme = theme
        self._date = date
        self._time = time
        self._duration = duration
        self._venue_address = venue_address
        self._client_id = client_id
        self._guest_list = guest_list
        self._catering_company = catering_company
        self._decoration_company = decoration_company
        self._entertainment_company = entertainment_company
        self._furniture_company = furniture_company
        self._invoice = invoice

    # Getter and setter methods for event_id
    def get_event_id(self):
        return self._event_id

    def set_event_id(self, event_id):
        self._event_id = event_id

    # Getter and setter methods for type
    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    # Getter and setter methods for theme
    def get_theme(self):
        return self._theme

    def set_theme(self, theme):
        self._theme = theme

    # Getter and setter methods for date
    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    # Getter and setter methods for time
    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    # Getter and setter methods for duration
    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    # Getter and setter methods for venue_address
    def get_venue_address(self):
        return self._venue_address

    def set_venue_address(self, venue_address):
        self._venue_address = venue_address

    # Getter and setter methods for client_id
    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    # Getter and setter methods for guest_list
    def get_guest_list(self):
        return self._guest_list

    def set_guest_list(self, guest_list):
        self._guest_list = guest_list

    # Getter and setter methods for catering_company
    def get_catering_company(self):
        return self._catering_company

    def set_catering_company(self, catering_company):
        self._catering_company = catering_company

    # Getter and setter methods for decoration_company
    def get_decoration_company(self):
        return self._decoration_company

    def set_decoration_company(self, decoration_company):
        self._decoration_company = decoration_company

    # Getter and setter methods for entertainment_company
    def get_entertainment_company(self):
        return self._entertainment_company

    def set_entertainment_company(self, entertainment_company):
        self._entertainment_company = entertainment_company

    # Getter and setter methods for furniture_company
    def get_furniture_company(self):
        return self._furniture_company

    def set_furniture_company(self, furniture_company):
        self._furniture_company = furniture_company

    # Getter and setter methods for invoice
    def get_invoice(self):
        return self._invoice

    def set_invoice(self, invoice):
        self._invoice = invoice

