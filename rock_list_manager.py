samples = []
while True:
    rock = input('enter rock_type or done to finish. _ ').title()
    if rock == "Done":
        break
    samples.append(rock)
print(f'All samples: {samples}')
print(f'The number of sandstone sample is {samples.count("Sandstone")}')
samples.sort()
print(f'sorted sample are {samples}')