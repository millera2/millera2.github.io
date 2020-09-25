def fishPop(p, rate, totalCatch): 
    population = p   #starting population


    #Look at population for next 10 years

    print("Year|Population")

    year = 0
    while (population >0 and year < 100):
        formatString = "{0:^4}|{1:^10.2f}"
        print(  formatString.format(year,population)   )
        population = population*(1+rate)-totalCatch

        year = year+1
    
