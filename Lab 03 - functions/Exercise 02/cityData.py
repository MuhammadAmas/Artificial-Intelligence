# (i). You have collected information about cities in your province. You decide to store each city’s name, population, and mayor in a file. Write a python program to accept the data for a number of cities from the keyboard and store the data in a file in the order in which they’re entered.

# opening a file
with open("cityData.txt", "w") as f:

    # getting the number of cities
    citiesNum = int(input("Enter umber of cities: "))

    # looping through the number of cities
    for i in range(citiesNum):
        cityName = input("Enter city name: ")
        cityPopulation = input("Enter city population: ")
        cityMayor = input("Enter city mayor: ")

        # Writing the message to the file
        f.write(f"City Name: {cityName} City Population: {cityPopulation} City Mayor: {cityMayor} \n")   
