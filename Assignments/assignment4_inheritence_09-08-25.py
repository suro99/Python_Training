# Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information. 
# Requirements: 
#     -Flight should have attributes: flight number, airline.
#     -ScheduledFlight should add departure time and arrival time.
#     -Include methods to display complete flight information.
    
# Create a base class Person, derived class CrewMember, and a further derived class Pilot. -Person contains name and ID.
#     -CrewMember adds role (e.g., "Cabin Crew", "Pilot").
#     -Pilot adds license number and rank (e.g., "Captain"). 
#     -Include methods to display full details at each level.
    
# Create a base class Service, and derive two classes: SecurityService and BaggageService.
# Requirements: 
#     -Service class has a method service_info().
#     -Derived classes override or extend this to describe their own service.

# Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
# Requirements: 
#     - PassengerDetails has name, age.
#     - TicketDetails has ticket number, seat number.
#     - Booking shows all information.

class Flight:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline

    def display_info(self):
        return f"Flight Number: {self.flight_number}, Airline: {self.airline}"
    
class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, departure_time, arrival_time):
        super().__init__(flight_number, airline)
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Departure Time: {self.departure_time}, Arrival Time: {self.arrival_time}"

# Example usage:
scheduled_flight = ScheduledFlight("IX1871", "Air India Express", "08:15 PM", "10:55 PM")
print(scheduled_flight.display_info())

##################################################################################################

class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_info(self):
        return f"Name: {self.name}, ID: {self.id_number}"

class CrewMember(Person):
    def __init__(self, name, id_number, role):
        super().__init__(name, id_number)
        self.role = role

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Role: {self.role}"

class Pilot(CrewMember):
    def __init__(self, name, id_number, role, license_number, rank):
        super().__init__(name, id_number, role)
        self.license_number = license_number
        self.rank = rank

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, License Number: {self.license_number}, Rank: {self.rank}"

# Example usage:
pilot = Pilot("John Doe", "P12345", "Pilot", "LIC67890", "Captain")
print(pilot.display_info())

##################################################################################################

class Service:
    def service_info(self):
        return "General Service Information"

class SecurityService(Service):
    def service_info(self):
        return "Security Service: Ensuring passenger safety and security."

class BaggageService(Service):
    def service_info(self):
        return "Baggage Service: Handling and transporting passenger luggage."

# Example usage:
security_service = SecurityService()
baggage_service = BaggageService()
print(security_service.service_info())
print(baggage_service.service_info())

##################################################################################################

class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def display_info(self):
        return f"Passenger Name: {self.name}, Age: {self.age}"

class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number
    def display_info(self):
        return f"Ticket Number: {self.ticket_number}, Seat Number: {self.seat_number}"

class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def display_info(self):
        return f"{PassengerDetails.display_info(self)}, {TicketDetails.display_info(self)}"
    
# Example usage:
booking = Booking("Alice Smith", 30, "T123456", "12A")
print(booking.display_info())