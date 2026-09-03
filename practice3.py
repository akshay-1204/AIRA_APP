booking = {
  "customer_name": input("Enter customer name: "),
  "phone_number": input("Enter phone number: "),
  "gender": input("Enter gender: "),
  "bus_operator": input("Enter bus operator name: "),
  "source_city": input("Enter source city: "),
  "destination_city": input("Enter destination city: "),
  "journey_date": input("Enter journey date: "),
  "seats": int(input("Enter number of seats: ")),
  "price_per_seat": int(input("Enter price per seat (₹): "))
}
total_fare = booking["seats"] * booking["price_per_seat"]

if total_fare > 1000:
    discount = total_fare * 0.05
else:
    discount = 0

final_amount = total_fare - discount

print_db = f"""
==========================================

BUS TICKET BOOKING RECEIPT

==========================================

Passenger Name : {booking["customer_name"]}
Phone Number : {booking["phone_number"]}
Gender : {booking["gender"]}
Bus Operator : {booking["bus_operator"]}
Route : {booking["source_city"]} -> {booking["destination_city"]}
Journey Date : {booking["journey_date"]}
Seats Booked : {booking["seats"]}
Price per Seat : ₹{booking["price_per_seat"]}
Total Fare : ₹{total_fare:.0f}
Discount Applied : ₹{discount:.2f}
Final Amount : ₹{final_amount:.2f}

Thank you for booking with {booking["bus_operator"]}!

==========================================
"""

print(print_db)