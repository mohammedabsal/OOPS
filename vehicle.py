# Create a class called 'Vehicle' with 3 private instance variables: 'cost', 'type' and 'premium' where cost is the cost of the vehicle, type is the type of the vehicle and 'premium' is the premium amount to be calculated for the vehicle.  
# Vehicle type values can be 1, 2 or 3 where:
#  1 - for two wheeler
#  2 - for four wheeler
# 3 - for other types
# Create a parameterized constructor with 2 arguments: cost and type.  Set the instance variable 'premium as 'None'.
# The 'Vehicle' class also contain a method: calculate_premium().  This method is used to calculate the premium amount and set it to the instance variable 'premium'.
# Apply the following rules to calculate the vehicle premium:
# 1.       If the type of the vehicle is type 1 ("Two Wheeler") then 2% of cost is the premium.
# 2.       If the type of the vehicle is type 2 ("Four Wheeler") then 6% of cost is the premium.
# 3.       If then type of the vehicle is type 3 ("Other") then 8% of cost is the premium.
# Write a getter method for the private variable to return the premium amount.  The method definition should be: 'get_premium(self)'.
# Get the cost and type of the vehicles from the users and store those values into the variables with the names: 'vehicle_cost' and 'vehicle_type' respectively and they should be in global scope.
# Then create an object of 'Vehicle' class by invoking the 2 argument parameterized constructor by passing 'vehicle_cost' and 'vehicle_type' as arguments.  
# Store this vehicle object into a reference variable with the name : "vehicle_obj" which should be in global scope.  Using 'vehicle_obj' , calculate the premium amount by invoking the method 'calculate_premium().  After this display the vehicle object's (vehicle_obj)  premium amount as shown in the sample output.

# Note:
# The vehicle cost and premium amount should be  float values and type should be an integer value. So, necessary conversion is required.
# Use the same attribute names, class name, object name and method names as given in the question description.

# Sample input :
# Enter the vehicle cost: 30000
# Enter the type of the vehicles (1 for 2 wheeler, 2 for 4 wheeler and 3 for other types):1
# Sample output :
# The premium amount is: 600.0
class Vehicle:
    def __init__(self, vehicle_cost, vehicle_type):
        self.__vehicle_cost = vehicle_cost
        self.__vehicle_type = vehicle_type
        self.__premium = None

    def calculate_premium(self):
        if self.__vehicle_type == 1:
            self.__premium = self.__vehicle_cost * 0.02
        elif self.__vehicle_type == 2:
            self.__premium = self.__vehicle_cost * 0.06
        elif self.__vehicle_type == 3:
            self.__premium = self.__vehicle_cost * 0.08

    def get_premium(self):
        return self.__premium
#global variables
vehicle_cost = float(input("Enter the vehicle cost: "))
vehicle_type = int(input("Enter the type of the vehicle (1 for 2 wheeler, 2 for 4 wheeler and 3 for other types): "))
#create object
vehicle_obj = Vehicle(vehicle_cost, vehicle_type)  #reference variable
vehicle_obj.calculate_premium()
print("The premium amount is:", vehicle_obj.get_premium())
