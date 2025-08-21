def multiplier_generator(base):
    def multiplier(x):
        if base == 0:   
            return x * x
        return base * x
    return multiplier
 


doubler = multiplier_generator(2)
tripler = multiplier_generator(3)
squarer = multiplier_generator(0)


print("Doubler:", doubler(4))   
print("Tripler:", tripler(4))   
print("Squarer:", squarer(4))   