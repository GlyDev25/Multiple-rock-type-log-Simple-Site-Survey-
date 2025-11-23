 def get_density(mass, volume):
    return mass/volume
def get_porosity(pore_volume, total_volume):
    return (pore_volume*total_volume)*100
def get_permeability_index (porosity,grainsize):
    return (porosity*grainsize)/10

mass = float(input('what is the mass of the rock: '))
volume = float(input('what is the volume of the rock: '))
pore_volume = float(input('what is the pore volume of the rock: '))
total_volume = float(input('what is the total volume of the rock: '))
porosity = float(input('what is the porosity of the rock: '))
grainsize = float(input('what is the grainsize of the rock: '))
print ("=== Analyzed Rock Properties are === ")
print(f"density = {get_density(mass, volume)}")
print(f"Porosity = {get_porosity(pore_volume, total_volume)}")
print(f"permability index = {get_permeability_index(porosity,grainsize)}")


 