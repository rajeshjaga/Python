class planet:

    def __init__(self,name,gravity,radius,system):
        self.name=name
        self.garvity=gravity
        self.radius=radius
        self.system=system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

hoth=planet('hotho',9.8,6400,'solarsystem')
print(f'name is {hoth.name}')
print(f'gravit is {hoth.garvity}')
#print(hoth.orbit())


planetx=planet('plan',5,5000,'plan')
print(f'name of the planet is {planetx.name}')
print(f'gravity of the planet {planetx.garvity}')
print(f'radius of the planet is {planetx.radius}')
#print(planetx.orbit())
