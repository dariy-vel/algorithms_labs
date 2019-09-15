class Helicopter:

    def __init__(self, max_mass, name, max_height):
        self.max_mass = int(max_mass)
        self.name = name
        self.max_height = int(max_height)

    def __repr__(self):
        return str(self.__dict__)
