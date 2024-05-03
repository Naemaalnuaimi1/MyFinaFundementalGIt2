

from ClassCatering1 import ClassCatering
from ClassClient1 import ClassClient
from ClassCompany1 import ClassCompany
from ClassEmployee1 import ClassEmployee
from ClassEvent1 import ClassEvent
from ClassGuest1 import ClassGuest
from ClassManager1 import ClassManager
from ClassVenue1 import ClassVenue

def test_classes():
    # Test ClassCatering
    catering = ClassCatering(1, "Catering Company", "123 Main St", "050-111-1111", "Italian Cusine", 50, 200)
    print("Catering Company Name:", catering.get_name())
    print("Minimum Guests:", catering.get_min_guests())
    print("Maximum Guests:", catering.get_max_guests())

    # Test ClassClient
    client = ClassClient(1, "Mohammed", "Abu dhabi", "050-444-7777", 5000.0)
    print("Client Name:", client.get_name())
    print("Budget:", client.get_budget())

    # Test ClassCompany
    company = ClassCompany(1, "XYZ Company ", "UAE", "050-000-0000")
    print("Company Name:", company.get_name())

    # Test ClassEmployee
    employee = ClassEmployee(1, "Sultan", "Sales", "Sales Manager", 3000.0, 30, "2000-01-01", "AB123456")
    print("Employee Name:", employee.get_name())
    print("Job Title:", employee.get_job_title())

    # Test ClassEvent
    event = ClassEvent(1, "Wedding", "Outdoor", "2024-05-01", "15:00", 4, "Abu Dhabi", 1, [], None, None, None, None, 0.0)
    print("Event Type:", event.get_type())
    print("Date:", event.get_date())

    # Test ClassGuest
    guest = ClassGuest(1, "Sara", "Dubai", "123-456-7890")
    print("Guest Name:", guest.get_name())

    # Test ClassManager
    manager = ClassManager(1, 1, "Manager Name", "Sales", "Sales Manager", 3000.0, 30, "2000-01-01", "AB123456")
    print("Manager Name:", manager.get_name())
    print("Manager ID:", manager.get_manager_id())

    # Test ClassVenue
    venue = ClassVenue(1, "Venue Name", "123 Venue St", "123-456-7890", 50, 200)
    print("Venue Name:", venue.get_name())
    print("Minimum Guests:", venue.get_min_guests())
    print("Maximum Guests:", venue.get_max_guests())

if __name__ == "__main__":
    test_classes()