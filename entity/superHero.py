from entity.metaHero import metaHero

class superHero(metaclass=metaHero):

    def __init__(self):
        self._name = 'Batman'
        self._power = 1024
        self._secretName = 'Bruce Wayne'
        self._city = 'Gotham'
        self._location = 'Batcave'

    @property
    def name(self):
        """
        Any singleton should define some business logic, which can be
        executed on its instance.
        """
        return self._name


    def __str__(self) -> str:
        return "name: " + str(self._name) + \
               ", power: " + str(self._power) + \
               ", secretName: " + str(self._secretName) + \
               ", city: " + str(self._city) + \
               ", location: " + str(self._location)


