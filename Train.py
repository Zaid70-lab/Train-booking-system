code 
TOTAL SEATS = 10
bookings = 0
def view_available_seats:
print("Available Seats:")
available = [str(seat) for seat in range(1, TOTAL_SEATS + 1) if seat not in bookings]
if available:
print(", join(available))
else:
print ("No seats available.")
def book_ticket:
view_available_seats
if len(bookings) == TOTAL SEATS:
print("All seats are booked.")
return
name = input("Enter passenger name:")
for seat in range(1, TOTAL_SEATS + 1):
if seat not in bookings:
bookings[seat) = name
print(f"Ticket booked for (name) at seat (seat).")
break
def cancel_ticket:
name = input("Enter name to cancel booking: ")
found = False
for seat, passenger in list(bookings.items0):
if passenger == name: del bookings[seat]
print(f"Booking cancelled for (name) from seat {seat).")
found = True
break
if not found:
print(f"No booking found for (name).')
def view_bookings):
if bookings:
rint Booked Seats:" or seat in sorted(bookings)
print(f"Seat (seat): (bookings[seat)))
else:
print("No current bookings.")
while True:
rint(*\n1. Book Ticket\n2. Cancel Ticket\n3. View Bookings\n4. View Available Seats\n5. Exit"
choice = input(*Enter choice: "
if choice == '1': book_ticket
elif choice == '2': ancel ticket( lif choice == '3' view_bookings elif choice == '4':
view_available_seats elif choice == '5':
print("Exiting...")
break else:
print("Invalid choice. Please try again.")
