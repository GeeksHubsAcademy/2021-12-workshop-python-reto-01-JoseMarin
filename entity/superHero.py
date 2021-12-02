from entity.metaHero import metaHero

class superHero(metaclass=metaHero):
    """
    Any singleton should define some business logic, which can be
    executed on its instance.
    """

    def __init__(self):
        self.name = 'Batman'
        self.power = 1024
        self.secretName = 'Bruce Wayne'
        self.city = 'Gotham'
        self.location = 'Batcave'

    def maxPower(self, max):
        self.power += max
        return self.power

    def minPower(self, min):
        if min >= 0:
            if self.power < min:
                self.power = 0
            else:
                self.power -= min
        else:
            self.power = 0
        return self.power


    def __str__(self) -> str:
        return "name: " + str(self.name) + \
               ", power: " + str(self.power) + \
               ", secretName: " + str(self.secretName) + \
               ", city: " + str(self.city) + \
               ", location: " + str(self.location)


