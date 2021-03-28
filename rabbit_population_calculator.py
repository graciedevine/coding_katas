def rabbit_population_growth ():
    """A population of rabbits doubles every 3 months. Ask the user to input the number of rabbits and the time period after which s/he wants to know the rabbit population."""

    starting_population = int(input("Please enter the starting rabbit population."))
    user_time_period = int(input("Please enter the time period (in years) after which you want to know the rabbit population"))
    #Formula for population growth is A=A(growth) ** (t/k)

    growth = 2
    #population doubles

    growth_rate = 3
    #every 3 months

    months_in_year = 12

    time = user_time_period*months_in_year
    #converts user input years to months

    exponential_time = time/growth_rate
    #this is our exponent

    total_rabbit_population = starting_population * (growth ** exponential_time)
    return total_rabbit_population

print ("The total rabbit population will be ", rabbit_population_growth())