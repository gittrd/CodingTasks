'''
The aim of the function's is to calculate a user's total holiday cost, which includes the following:
1) Plane cost
2) Hotel cost
3) Car-rental cost

First step is to get the user to enter the following:
1) The city they will be flying to
2) Number of nights they will want to stay at the hotel
3) Number of days for which they will be hiring a car

The functions logic should be as follows:
1) hotel cost - to calculate the total cost for the hotel stay based on user input
2) plane cost - to calculate the cost for the flight based on user input
3) car rental - to calculate the cost for the car rental based on user input
4) total cost - to utilise the result of the three functions above and return the total cost

To also print out each cost, including the total
'''

# prompting the user for inputs
# city flight
city_flight = input("Which city would you like to fly to? (London, Paris or Lyon) ")

# number of nights staying at the hotel
num_nights = int(input("How many nights do you want to stay at the hotel? "))

# number of days of car hire
rental_days = int(input("How many days do you want to hire a car? "))


def hotel_cost(num_nights):
    """Calculate the cost of the hotel."""
    total_cost = round(num_nights * 150.78,2)
    return total_cost

print(f"The total cost for the hotel is: {hotel_cost(num_nights)}")


def plane_cost(city_flight):
    """Calculate the cost of the flight based on City selected by user."""
    if city_flight == "London":
        return 250.00
    elif city_flight == "Paris":
        return 55.00
    else:
        return 150

print (f"The total cost for the flight to {city_flight} is {plane_cost(city_flight)}")


def car_cost(rental_days):
    """Calculate the cost of the car hire."""
    total_cost = round(rental_days * 126.98,2)
    return total_cost

print(f"The total cost for the car hire is: {car_cost(rental_days)}")


def holiday_cost():
    """Calculate total cost of the holiday."""
    return round(hotel_cost(num_nights) + plane_cost(city_flight) + car_cost(rental_days),2)

print(f"The total cost for the holiday is: {holiday_cost()}")
