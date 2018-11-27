import random
population = 1000
year = 1
print("Welcome to the Gopher Population Simulator")
print("Starting population: ", population)
print("Year ", year)

for i in range(2, 11, 1):
    born = int(population*random.randint(10, 20) / 100);
    die = int(population*random.randint(5, 25) / 100)
    year = i
    population = population + born - die
    print("{} gophers were born. {} died.".format(born, die))
    print("Population: {}".format(population))
    print("Year: {}".format(year))
