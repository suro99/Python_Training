 # Problem Statement You are asked to design a Flight Management System in Python using exception handling.
 # The system should: 
 # - Read flight information from a file called flights.txt. 
 # - Each line has: flight_number available_seats price_per_ticket Example: AI101 50 6000 Ask the user for: 
 # - Flight number 
 # - Number of tickets to book Implement the following exception rules: 
 # (Questions below) 
 # (a) Raise FlightNotFoundError (custom) if the entered flight number does not exist. 
 # (b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats. 
 # (c) Handle ValueError if user enters invalid input (like string instead of integer). 
 # (d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket). 
 # (e) Always close the file using finally. 
 # The program should print: 
 # - Flight details - Total booking cost - Discount per ticket (total / tickets) 
 # Note**: Use nested try-except: Inner block for booking operations. Outer block for file handling & re-raised exceptions
 
class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass
def book_flight():
    try:
        file = open("flights.txt", "r")
        flights = {}
        for line in file:
            parts = line.split()
            flight_number = parts[0]
            available_seats = int(parts[1])
            price_per_ticket = float(parts[2])
            flights[flight_number] = (available_seats, price_per_ticket)
        
        try:
            flight_number = input("Enter flight number: ")
            if flight_number not in flights:
                raise FlightNotFoundError(f"Flight {flight_number} not found.")
            
            available_seats, price_per_ticket = flights[flight_number]
            tickets_to_book = int(input("Enter number of tickets to book: "))
            if tickets_to_book > available_seats:
                raise SeatsUnavailableError(f"Only {available_seats} seats available.")
            if tickets_to_book == 0:
                raise ZeroDivisionError("Number of tickets cannot be zero.")
            
            total_cost = tickets_to_book * price_per_ticket
            discount_per_ticket = total_cost / tickets_to_book
            
            print(f"Flight Details: {flight_number}, Available Seats: {available_seats}, Price per Ticket: {price_per_ticket}")
            print(f"Total Booking Cost: {total_cost}")
            print(f"Discount per Ticket: {discount_per_ticket}")
        
        except ValueError:
            print("Invalid input. Please enter numeric values for number of tickets.")
        except (FlightNotFoundError, SeatsUnavailableError, ZeroDivisionError) as e:
            print(e)
        
    except FileNotFoundError:
        print("The file flights.txt was not found.")
    finally:
        try:
            file.close()
        except NameError:
            pass
book_flight()